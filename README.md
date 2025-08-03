# Projeto de Orquestração com Prefect e FastAPI

Este projeto demonstra um fluxo de orquestração de dados utilizando Prefect para extrair dados de uma API (Reddit) e uma API FastAPI para armazenar e expor os dados.

## Como Executar

Para executar o projeto, você precisará ter o Docker e o Docker Compose instalados.

1.  **Clone o repositório:**

    ```bash
    git clone <url-do-repositorio>
    cd <nome-do-repositorio>
    ```

2.  **Execute o Docker Compose:**

    ```bash
    docker-compose up -d
    ```

    Isso irá construir e iniciar os dois serviços definidos no `docker-compose.yaml`: `backend` e `orchestration`.

## Verificando os Serviços

### Orquestração (Prefect)

A interface do usuário do Prefect estará disponível em [http://localhost:4200](http://localhost:4200).

Nesta interface, você poderá visualizar os fluxos (`scrape_flow` e `post_flow`), seus status e logs de execução. Os fluxos são configurados para rodar a cada duas horas.

### API (FastAPI)

A API FastAPI estará disponível em [http://localhost:9001](http://localhost:9001).

A API possui os seguintes endpoints:

*   **`GET /get`**: Retorna os dados armazenados em formato JSON.
*   **`POST /post`**: Recebe novos dados do fluxo de orquestração e os armazena.

---

# Orchestration Project with Prefect and FastAPI

This project demonstrates a data orchestration workflow using Prefect to extract data from an API (Reddit) and a FastAPI to store and expose the data.

## How to Run

To run the project, you will need to have Docker and Docker Compose installed.

1.  **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd <repository-name>
    ```

2.  **Run Docker Compose:**

    ```bash
    docker-compose up -d
    ```

    This will build and start the two services defined in `docker-compose.yaml`: `backend` and `orchestration`.

## Checking the Services

### Orchestration (Prefect)

The Prefect UI will be available at [http://localhost:4200](http://localhost:4200).

In this interface, you can view the flows (`scrape_flow` and `post_flow`), their status, and execution logs. The flows are configured to run every two hours.

### API (FastAPI)

The FastAPI will be available at [http://localhost:9001](http.localhost:9001).

The API has the following endpoints:

*   **`GET /get`**: Returns the stored data in JSON format.
*   **`POST /post`**: Receives new data from the orchestration flow and stores it.