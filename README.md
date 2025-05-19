# 🛒 E-Shop Brasil  
*Disciplina — Advanced Databases and Big Data*  

---

## 1 | Introdução  
O e-commerce gera grandes volumes de dados heterogêneos (produtos, clientes, pedidos, logs de navegação).  
Para demonstrar como tecnologias NoSQL e visualização rápida podem resolver esse problema, foi construída a **E-Shop Brasil**, uma aplicação de prova-de-conceito que armazena os dados em **MongoDB** (document-oriented), roda tudo em **Docker** e apresenta uma interface analítica em **Streamlit**.

### 1.1 Problema  
Organizações precisam de um ambiente barato, replicável e flexível para:  
* inserir e editar registros de catálogo, clientes e compras;  
* combinar/concatenar essas informações em consultas analíticas;  
* exibir resultados a usuários não-técnicos em tempo real.  

### 1.2 Objetivos  
* Containerizar todo o stack para evitar “works on my machine”;  
* Popular o MongoDB automaticamente na subida do container;  
* Desenvolver um app Streamlit que faça **CRUD + consultas + concatenação**;  
* Disponibilizar roteiro de execução com testes ilustrados.

---

## 2 | Descrição do Projeto  

| Camada | Descrição |
|--------|-----------|
| **Docker** | `docker-compose.yml` define um serviço `mongodb`. Um volume mapeia a pasta `init/` contendo `init.js`; ele é executado pelo entry-point do Mongo, populando o banco automaticamente. |
| **MongoDB** | Banco `e_shop_brasil` com três coleções: `produtos`, `clientes`, `pedidos`. Esquema flexível: documentos JSON. |
| **Streamlit (app.py)** | 1) abre conexão via **PyMongo**; 2) exibe tabelas interativas (`st.dataframe`) para cada coleção; 3) fornece formulários para **inserir**, **editar** e **excluir** documentos; 4) permite **concatenar** (aggregate) pedidos × produtos para mostrar o valor total de cada pedido. |

### 2.1 Operações implementadas no `app.py`
* **Inserção** – formulários “Adicionar Produto/Cliente/Pedido”.  
* **Manipulação** – botões de *Editar* (update_one) e *Excluir* (delete_one).  
* **Concatenação** – pipeline `aggregate` faz *lookup* `pedidos → produtos` para detalhar itens por preço.  
* **Consulta** – campos de filtro por texto, preço, cliente; resultado mostrado instantaneamente.

---

## 3 | Passos para Implementação  

### 3.1 Clonar o projeto
```bash
git clone https://github.com/<Salete376>/E-Shop-Brasil.git
cd e-shop-brasil
