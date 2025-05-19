from pymongo import MongoClient

# Conectar ao MongoDB no container Docker
cliente = MongoClient("mongodb://localhost:27017/")

# Selecionar o banco de dados
db = cliente["e_shop_brasil"]

# Acessar as coleções
produtos = db.produtos.find()
clientes = db.clientes.find()
pedidos = db.pedidos.find()

print("\n=== Produtos ===")
for produto in produtos:
    print(produto)

print("\n=== Clientes ===")
for cliente in clientes:
    print(cliente)

print("\n=== Pedidos ===")
for pedido in pedidos:
    print(pedido)
