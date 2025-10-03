from fastapi import HTTPException
from sqlmodel import Session, select
from controller.generic import create_crud_router, Hooks
from model.models import Pessoa
from model.dto import PessoaCreate, PessoaRead , PessoaUpdate

class PessoaHooks(Hooks[Pessoa, PessoaCreate, PessoaUpdate]):
    def pre_create(self, payload: PessoaCreate, session: Session) -> None:
        if payload.email is not None:
            exists = session.exec(select(Pessoa).where(Pessoa.email == payload.email)).first() # sem esse first seria sempre true
            if exists:
                raise HTTPException(400, "E-mail ja ta cadastrado abençoado!")
        
    def pre_update(self, payload: PessoaUpdate, session: Session, obj: Pessoa) -> None:
        if payload.email is not None and payload.email != obj.email:
            exists = session.exec(select(Pessoa).where(Pessoa.email == payload.email, Pessoa.id != obj.id)).first() # tinha problema de encontrar ela mesma
            if exists:
                raise HTTPException(400,"E-mail já em uso!")

router = create_crud_router(
    model=Pessoa,
    create_schema=PessoaCreate,
    update_schema=PessoaUpdate,
    read_schema=PessoaRead,
    prefix="/pessoas",
    tags=["pessoas"],
    hooks=PessoaHooks(),
)