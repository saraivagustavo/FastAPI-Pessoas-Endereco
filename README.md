# API de Pessoas e Endereços 🧑‍🤝‍🧑

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.118.0-green?style=for-the-badge&logo=fastapi)
![SQLModel](https://img.shields.io/badge/SQLModel-0.0.25-blueviolet?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

<div align="center">
  <img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI" width="250"/>
</div>

## 📖 Visão Geral

Este projeto é uma API RESTful desenvolvida como parte de uma atividade acadêmica para demonstrar a implementação de uma arquitetura de software limpa, robusta e reutilizável. A aplicação permite o gerenciamento completo (CRUD) de **Pessoas** e seus respectivos **Endereços**, estabelecendo um relacionamento de um-para-muitos entre eles.

A documentação interativa da API, gerada automaticamente pelo FastAPI, pode ser acessada em `/docs` após a inicialização do servidor.

---

## ✨ Principais Features

-   [x] **CRUD Completo para Pessoas**: Crie, leia, atualize e delete registros de pessoas.
-   [x] **CRUD Completo para Endereços**: Gerencie endereços, sempre associados a uma pessoa.
-   [x] **Relacionamento de Dados**: Uma pessoa pode ter múltiplos endereços.
-   [x] **Validação de Dados**: Validação automática de e-mails únicos e regras de negócio.
-   [x] **Arquitetura em Camadas**: Código organizado em `Controller`, `Service` e `Repository`.
-   [x] **Reutilização com Generics**: Componentes genéricos para evitar repetição de código.
-   [x] **Banco de Dados SQLite**: Leve, rápido e não requer um servidor externo.
-   [x] **Documentação Automática**: Endpoints `/docs` (Swagger UI) e `/redoc` prontos para uso.

---

## 🏛️ Arquitetura e Design

A aplicação foi estruturada seguindo os princípios de desacoplamento e separação de responsabilidades, resultando em um código mais testável e de fácil manutenção.

`Controller` → `Service` → `Repository`

1.  **Controller (`/controller`)**: A camada mais externa, responsável por receber as requisições HTTP, validar os dados de entrada usando os DTOs e retornar as respostas. Ela delega a lógica para a camada de serviço.

2.  **Service (`/service`)**: Contém a lógica de negócio da aplicação. Orquestra as operações, executa validações e se comunica com a camada de repositório.

3.  **Repository (`/repository`)**: A camada de acesso a dados. É a única que "conversa" diretamente com o banco de dados, abstraindo as queries e a lógica de persistência.

O uso de **Generics** (`TypeVar`) foi fundamental para criar uma base de código enxuta, onde as classes `Service`, `Repository` e a fábrica `create_crud_router` são reutilizadas para ambas as entidades (`Pessoa` e `Endereco`).

---

## 🛠️ Tecnologias Utilizadas

-   **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
-   **ORM e Validação**: [SQLModel](https://sqlmodel.tiangolo.com/) (baseado em Pydantic e SQLAlchemy)
-   **Servidor ASGI**: [Uvicorn](https://www.uvicorn.org/)
-   **Banco de Dados**: [SQLite](https://www.sqlite.org/index.html)

---

## 🚀 Como Executar o Projeto

Siga os passos abaixo para configurar e executar o projeto em seu ambiente local.

**1. Clone o repositório:**

```bash
git clone [https://github.com/saraivagustavo/FastAPI-Pessoas-Endereco.git](https://github.com/saraivagustavo/FastAPI-Pessoas-Endereco.git)
cd nome-do-diretorio
```

**2. Crie e ative um ambiente virtual:**

```bash
# Para Windows
python -m venv venv
.\venv\Scripts\activate

# Para macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

**3. Instale as dependências:**

O projeto utiliza um arquivo `requirements.txt` para gerenciar as dependências.

```bash
pip install -r requirements.txt
```

**4. Inicie a aplicação:**

Use o `uvicorn` para iniciar o servidor ASGI. A flag `--reload` reinicia o servidor automaticamente a cada alteração no código.

```bash
uvicorn main:app --reload
```

**5. Acesse a API:**

-   **Aplicação**: `http://127.0.0.1:8000`
-   **Documentação Interativa (Swagger)**: `http://127.0.0.1:8000/docs`
-   **Documentação Alternativa (ReDoc)**: `http://127.0.0.1:8000/redoc`

---

## 🗺️ Endpoints da API

| Método | Rota                     | Descrição                                         |
| :----- | :----------------------- | :------------------------------------------------ |
| `POST` | `/pessoas`               | Cria uma nova pessoa.                             |
| `GET`  | `/pessoas`               | Lista todas as pessoas (sem endereços).           |
| `GET`  | `/pessoas/{item_id}`     | Busca uma pessoa específica e seus endereços.     |
| `PATCH`| `/pessoas/{item_id}`     | Atualiza os dados de uma pessoa.                  |
| `DELETE`| `/pessoas/{item_id}`    | Deleta uma pessoa.                                |
| `POST` | `/enderecos`             | Cria um novo endereço para uma pessoa.            |
| `GET`  | `/enderecos`             | Lista todos os endereços.                         |
| `GET`  | `/enderecos/{item_id}`   | Busca um endereço específico.                     |
| `PATCH`| `/enderecos/{item_id}`   | Atualiza os dados de um endereço.                 |
| `DELETE`| `/enderecos/{item_id}`  | Deleta um endereço.                               |

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE.md) para mais detalhes.

---

## 👨‍💻 Autor

Desenvolvido por **Gustavo Saraiva**.

[![GitHub](https://img.shields.io/badge/GitHub-saraivagustavo-181717?style=for-the-badge&logo=github)](https://github.com/saraivagustavo)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-0A66C2?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/gustavo-saraiva-mariano/)