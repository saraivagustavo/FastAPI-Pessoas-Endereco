from fastapi import HTTPException, Depends
from repository.generic import Repository
from service.generic import Service
from sqlmodel import Session, select
from controller.generic import create_crud_router, Hooks
from model.models import Pessoa
from model.dto import PessoaCreate, PessoaRead, PessoaReadComEndereco , PessoaUpdate
from util.database import get_session

#hooks de validação para o email da pessoa ser único
class PessoaHooks(Hooks[Pessoa, PessoaCreate, PessoaUpdate]):
    def pre_create(self, payload: PessoaCreate, session: Session) -> None:
        if payload.email is not None:
            exists = session.exec(select(Pessoa).where(Pessoa.email == payload.email)).first() #o .first() é para caso haja mais de um resultado, ele pegar só o primeiro e não retornar uma lista
            if exists:
                raise HTTPException(400, "E-mail jáa tá cadastrado abençoado!") #paulo sérgio style
        
    #mesma lógica do pre_create, mas para atualizar a pessoa
    def pre_update(self, payload: PessoaUpdate, session: Session, obj: Pessoa) -> None:
        if payload.email is not None and payload.email != obj.email:
            exists = session.exec(select(Pessoa).where(Pessoa.email == payload.email, Pessoa.id != obj.id)).first() 
            if exists:
                raise HTTPException(400,"E-mail já em uso!")

router = create_crud_router(
    model=Pessoa,
    create_schema=PessoaCreate,
    update_schema=PessoaUpdate,
    read_schema=PessoaRead, #DTO para ler uma pessoa >>>sem<<< os endereços
    prefix="/pessoas",
    tags=["pessoas"],
    hooks=PessoaHooks(),
)

#como na rotaa de pessoas não puxa os endereços juntos, tem que criar uma segunda rota para buscar a pessoa com os endereços
#como tá criando fora do create_crud_router (que já cria o service e o repository) tem que criar manualmente
repo = Repository(Pessoa) 
service = Service(repo) 

@router.get("/{item_id}/enderecos", response_model=PessoaReadComEndereco) #sobreescreve a definição que foi criada dentro do create_crud_router usando o modelo de PessoaReadComEndereco que puxa os endereços
def get_pessoa_com_enderecos(item_id: int, session: Session = Depends(get_session)):
    pessoa = service.get(session, item_id) #puxa a pessoa pelo id
    if not pessoa:
        raise HTTPException(status_code=404, detail="Pessoa não encontrada")
    return pessoa


