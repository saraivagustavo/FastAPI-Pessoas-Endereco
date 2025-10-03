from fastapi import FastAPI
from util.database import init_db
from controller.pessoa import router as pessoas_router
from controller.endereco import endereco_router as enderecos_router

app = FastAPI()

init_db()

app.include_router(pessoas_router)
app.include_router(enderecos_router)

@app.get('/')
def health():
    return{"status":"ok"}