from fastapi import HTTPException
from sqlmodel import Session, select
from controller.generic import create_crud_router, Hooks
from model.models import Endereco, Pessoa
from model.dto import EnderecoCreate, EnderecoRead, EnderecoUpdate

#hook serve para adicionar regras antes de fazer alguma operação nas classes
class EnderecoHooks(Hooks[Endereco, EnderecoCreate, EnderecoUpdate]):
    #hooks para validar se a pessoa existe antes de criar ou atualizar um endereço
    def pre_create(self, payload: EnderecoCreate, session: Session) -> None:
        if payload.id_pessoa is not None:
            pessoa = session.get(Pessoa, payload.id_pessoa) #verifica se a pessoa existe
            if not pessoa:
                raise HTTPException(400, "Pessoa não encontrada!")
    
    def pre_update(self, payload: EnderecoUpdate, session: Session) -> None: #mesma lógica do pre_create, mas pra atualizar o endereço
        if payload.id_pessoa is not None:
            pessoa = session.get(Pessoa, payload.id_pessoa)
            if not pessoa:
                raise HTTPException(400, "Pessoa não encontrada!")
        

#usa o router genérico pra criar os endpoints do CRUD
endereco_router = create_crud_router(
    model=Endereco,
    create_schema=EnderecoCreate, #DTO para criar um endereço do model
    update_schema=EnderecoUpdate, #DTO para atualizar um endereço do model
    read_schema=EnderecoRead, #DTO para ler um endereço do model
    prefix="/enderecos",
    tags=["enderecos"],
    hooks=EnderecoHooks(), #passa a classe de hooks para validar se a pessoa existe antes de criar ou atualizar um endereço
)