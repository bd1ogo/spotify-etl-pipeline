# Spotify ETL Pipeline

## Objetivo

Pipeline ETL que coleta dados da Spotify API, realiza transformações com Pandas e armazena os resultados em PostgreSQL.

## Arquitetura

Spotify API
↓
Extract
↓
Bronze JSON
↓
Transform
↓
Silver CSV
↓
Load
↓
PostgreSQL

## Estrutura do Projeto

![Estrutura](imagens/project-structure.png)

## Execução do Pipeline

![Pipeline](imagens/pipeline-execution.png)

## Dados Carregados

![PostgreSQL](imagens/postgres-data.png)

## Tecnologias

- Python
- Pandas
- Spotify API
- PostgreSQL
- Docker
- SQLAlchemy