from fastapi import HTTPException
from sqlmodel import Session, select
from controller.generic import create_crud_router, Hooks
from model.models import Endereco, Pessoa
from model.dto import EnderecoCreate, EnderecoRead, EnderecoUpdate

class EnderecoHooks(Hooks[Endereco, EnderecoCreate, EnderecoUpdate]):
    
    def pre_create(self, payload: EnderecoCreate, session: Session) -> None:
        if payload.id_pessoa is not None:
            pessoa = session.get(Pessoa, payload.id_pessoa)
            if not pessoa:
                raise HTTPException(400, "Pessoa não encontrada!")
    
    def pre_update(self, payload: EnderecoUpdate, session: Session, obj: Endereco) -> None:

        if payload.id_pessoa is not None and payload.id_pessoa != obj.id_pessoa:
            pessoa = session.get(Pessoa, payload.id_pessoa)
            if not pessoa:
                raise HTTPException(400, "Pessoa não encontrada!")
        

# Router para Endereços
endereco_router = create_crud_router(
    model=Endereco,
    create_schema=EnderecoCreate,
    update_schema=EnderecoUpdate,
    read_schema=EnderecoRead,
    prefix="/enderecos",
    tags=["enderecos"],
    hooks=EnderecoHooks(),
)