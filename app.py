import streamlit as st
from pymongo import MongoClient
import pandas as pd

st.set_page_config(page_title="E-Shop Brasil", layout="wide")

st.title("🛍️ E-Shop Brasil – Visualização de Dados do MongoDB")

# Conexão com MongoDB
cliente = MongoClient("mongodb://localhost:27017/")
db = cliente["e_shop_brasil"]

# Mostrar Produtos
st.header("📦 Produtos")
produtos = list(db.produtos.find())
if produtos:
    df_produtos = pd.DataFrame(produtos).drop(columns=["_id"])
    st.dataframe(df_produtos)
else:
    st.info("Nenhum produto cadastrado.")

# Mostrar Clientes
st.header("👥 Clientes")
clientes = list(db.clientes.find())
if clientes:
    df_clientes = pd.DataFrame(clientes).drop(columns=["_id"])
    st.dataframe(df_clientes)
else:
    st.info("Nenhum cliente cadastrado.")

# Mostrar Pedidos
st.header("🧾 Pedidos")
pedidos = list(db.pedidos.find())
if pedidos:
    df_pedidos = pd.DataFrame(pedidos).drop(columns=["_id"])
    st.dataframe(df_pedidos)
else:
    st.info("Nenhum pedido cadastrado.")
