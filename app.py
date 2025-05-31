from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Configuração do banco
db_config = {
    'host': 'aula4-db-1',  # nome do container Docker (ou 'localhost' se for local)
    'user': 'root',
    'password': 'root',
    'database': 'sistema'
}

# Rota para cadastrar novo pedido
@app.route('/pedidos', methods=['POST'])
def cadastrar_pedido():
    data = request.get_json()
    cliente_id = data['cliente_id']
    produto_id = data['produto_id']
    quantidade = data['quantidade']

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO pedido (cliente_id, produto_id, quantidade)
        VALUES (%s, %s, %s)
    """, (cliente_id, produto_id, quantidade))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({'status': 'Pedido cadastrado com sucesso'}), 201

# Rota para listar pedidos
@app.route('/pedidos', methods=['GET'])
def listar_pedidos():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT p.id, c.nome AS cliente, pr.nome AS produto, p.quantidade
        FROM pedido p
        JOIN cliente c ON p.cliente_id = c.id
        JOIN produto pr ON p.produto_id = pr.id
    """)
    pedidos = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(pedidos), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)