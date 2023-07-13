from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='clientess'
)

@app.route('/', methods=['GET', 'POST'])
def template_render():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        # Conecte-se ao banco de dados
        conn = mydb
        cursor = conn.cursor()

        # Insira os dados do usuário na tabela
        query = "INSERT INTO usuarios (email, senha) VALUES (%s, %s)"
        values = (email, senha)
        cursor.execute(query, values)

        # Commit e feche a conexão com o banco de dados
        conn.commit()
        cursor.close()
        conn.close()

        return 'Usuário cadastrado com sucesso!'

    return '<form method="POST" action="/"> \
                <input type="text" name="email" placeholder="E-mail"><br> \
                <input type="password" name="senha" placeholder="Senha"><br> \
                <input type="submit" value="Cadastrar"> \
            </form>'

if __name__ == '__main__':
    app.run()
