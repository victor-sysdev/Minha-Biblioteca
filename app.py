from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

def get_conexao():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="biblioteca"
    )

@app.route("/")
def index():
    pesquisa = request.args.get("pesquisa", "")

    conexao = get_conexao()
    cursor = conexao.cursor()

    if pesquisa:
        sql = """
        SELECT * FROM livros
        WHERE nome LIKE %s OR autor LIKE %s OR categoria LIKE %s
        """
        valor = f"%{pesquisa}%"
        cursor.execute(sql, (valor, valor, valor))
    else:
        cursor.execute("SELECT * FROM livros")

    livros = cursor.fetchall()

    cursor.close()
    conexao.close()

    return render_template("index.html", livros=livros, pesquisa=pesquisa)

if __name__ == "__main__":
    app.run(debug=True)