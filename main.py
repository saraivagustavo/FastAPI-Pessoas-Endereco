from fastapi import FastAPI
from util.database import init_db
from controller.pessoa import router as pessoas_router
from controller.endereco import endereco_router as enderecos_router

description = """
## 📖 Visão Geral do Projeto
Esta API foi desenvolvida como uma solução acadêmica para o cadastro de **Pessoas** e seus múltiplos **Endereços**. O projeto demonstra a aplicação de uma arquitetura robusta e desacoplada, utilizando Python e o framework FastAPI.

---

### 🏛️ Arquitetura e Padrões

A aplicação segue uma estrutura inspirada no padrão **MVC (Model-View-Controller)**, adaptada para o contexto de APIs:

* **Model (`/model`)**: Utiliza `SQLModel` para definir a estrutura dos dados e o mapeamento objeto-relacional (ORM) com o banco de dados. É a camada que representa a nossa base de dados em código Python.

* **Controller (`/controller`)**: Implementado com os `APIRouter` do FastAPI. Esta camada é responsável por expor os *endpoints*, receber as requisições HTTP e retornar as respostas ao cliente.

* **Service & Repository (`/service`, `/repository`)**: Para um maior desacoplamento, a lógica de negócio (`Service`) foi separada da lógica de acesso a dados (`Repository`). Isso torna o código mais limpo, testável e fácil de manter.

### ✨ Uso de Generics

Um dos pilares deste projeto é a reutilização de código através de **Generics** do Python (`TypeVar`). As classes `Repository`, `Service` e a fábrica de rotas `create_crud_router` são genéricas, o que significa que podem operar com qualquer modelo (`Pessoa` ou `Endereco`) sem a necessidade de reescrever código repetitivo para cada entidade.

---

### 💾 Banco de Dados

Conforme os requisitos, a API utiliza um banco de dados **SQLite**. Ele é configurado para rodar em memória (ou em um arquivo `app.db`), garantindo que a aplicação seja leve, autônoma e fácil de executar em qualquer ambiente, sem a necessidade de um servidor de banco de dados externo.

---

### 🚀 Funcionalidades

* ✅ **Pessoas**: CRUD completo para o cadastro de usuários.
* ✅ **Endereços**: CRUD completo para os endereços, sempre vinculados a uma pessoa.
* ✅ **Documentação Automática**: Interface interativa em `/docs` e `/redoc`.

"""

app = FastAPI(
    title="API Acadêmica de Pessoas e Endereços",
    description=description,
    version="1.1.0",
    contact={
        "name": "Gustavo Saraiva",
        "url": "https://github.com/saraivagustavo",
        "email": "gsaraivam10@gmail.com",
    }
)

init_db()

app.include_router(pessoas_router)
app.include_router(enderecos_router)

@app.get('/')
def health():
    return{"status":"ok"}
#uvicorn main:app --reload #comando para rodar o servidor localmente
#teste do codewise
#segundo teste do codewise, commit e push