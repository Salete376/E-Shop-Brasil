from pymongo import MongoClient

# Conectar ao MongoDB
cliente = MongoClient("mongodb://localhost:27017/")
db = cliente["e_shop_brasil"]

# Inserir produtos
produtos = [
    {"nome": "Notebook Dell", "preco": 3500.00, "estoque": 10},
    {"nome": "Mouse Logitech", "preco": 120.00, "estoque": 50},
    {"nome": "Teclado Mecânico", "preco": 450.00, "estoque": 30}
]
db.produtos.insert_many(produtos)

# Inserir clientes
clientes = [
    {"nome": "Ana Souza", "email": "ana@example.com"},
    {"nome": "Carlos Lima", "email": "carlos@example.com"}
]
db.clientes.insert_many(clientes)

# Inserir pedidos
pedidos = [
    {"cliente": "Ana Souza", "itens": ["Notebook Dell", "Mouse Logitech"], "total": 3620.00},
    {"cliente": "Carlos Lima", "itens": ["Teclado Mecânico"], "total": 450.00}
]
db.pedidos.insert_many(pedidos)

print("✅ Dados inseridos com sucesso!")
