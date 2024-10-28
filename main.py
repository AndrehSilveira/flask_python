import mysql.connector
from flask import Flask, request, jsonify
from bd import Carros

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'admin123',
    database = 'Flask',
    auth_plugin='mysql_native_password'
)



app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/carros', methods=['GET'])
def busca_carros():
    my_cursor = mydb.cursor()
    my_cursor.execute('select * from carros')
    meus_carros = my_cursor.fetchall()
    carros = list()
    for carro in meus_carros:
        carros.append(
            {
                'id': carro[0],
                'marca':carro[1],
                'modelo':carro[2],
                'ano':carro[3]
            }
        )

    return jsonify(
            mensagem = "Listagem de carros.",
            data = carros
        )
        
    
    

@app.route('/carros', methods=['POST'])
def create_carro():
    carro = request.json
    my_cursor = mydb.cursor()
    sql = f"insert into carros (marca, modelo, ano) values('{carro['marca']}','{carro['modelo']}',{carro['ano']})"
    my_cursor.execute(sql)
    mydb.commit()

    return jsonify(
        mensagem = 'Carro inserido com sucesso',
        carro = carro
    ), 201

app.run()

