# Projeto de Orquestração com Prefect e FastAPI

Mini projeto para demonstrar ferramenta de orquestração prefect com objetivo de demonstrar
algumas capacidades do prefect de agendar automatização de tarefas

## O que ele faz

A cada 2 horas o código irá executar scraping de novos posts do reddit por default será
o r/redditdev. Esse scraping irá pegar titulo, link, author e votos e irá postar na api
criada localmente apenas para efeitos de exemplos

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

    Isso irá construir e iniciar os cinco serviços definidos no `docker-compose.yaml`: `backend`, `flow_server`,
    `work-pool-creator`, `flow-scheduler`, `flow-starter`

### Orquestração (Prefect)

A interface do usuário do Prefect estará disponível em [http://localhost:4200](http://localhost:4200).

Nesta interface, você poderá visualizar os fluxos (`scrape_flow` e `post_flow`), seus status e logs de execução. Os fluxos são configurados para rodar a cada duas horas.
