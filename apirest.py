from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST']= 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'dani112722'
app.config['MYSQL_DB'] = 'flaskapp'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        detalhes = request.form
        name = detalhes['name']
        email = detalhes['email']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO usuarios(usuario, email) VALUES(%s, %s)", (name, email))
        mysql.connection.commit()
        cursor.close()
        return 'Adicionado com sucesso'        
    return '<form method="POST" action="">Name <input type="text" name="name"/><br>Email <input type="email" name="email"/><br><input type="submit"></form>'


@app.route('/usuarios')
def users():
    cursor = mysql.connection.cursor()
    consulta = cursor.execute("SELECT * FROM usuarios")
    if consulta > 0:
        usuarios = cursor.fetchall()
        return '<table border = 1>{% for user in usuarios %} <tr><td>{{usuario[0]}}</td><td>{{usuario[1]}}</td></tr>{% endfor %}</table>'


@app.route('/deletar', methods=['GET', 'POST'])
def deleteuser():
    if request.method == 'POST':
        detalhes = request.form
        name = detalhes['name']
        cursor = mysql.connection.cursor()
        cursor.execute(f"DELETE FROM usuarios WHERE usuario = '{name}'")
        mysql.connection.commit()
        cursor.close()
    return '<h1>Usuário que deseja deletar</h1><form method="POST" action="">Name <input type="text" name="name"/><br><input type="submit"></form>'




if __name__ == '__main__':
    app.run(debug=True)
