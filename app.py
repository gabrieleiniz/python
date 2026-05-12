from flask import Flask

app = Flask(__name__)

@app.route("/decorator")
def decorator():
    return """
        <h1>Decorator em Python</h1>

        <p>
        Um decorator em Python é uma forma de modificar o comportamento de uma função
        sem alterar diretamente seu código.
        </p>

        <p>
        Ele serve para adicionar funcionalidades extras, como autenticação,
        validações, logs e organização do código.
        </p>

        <p>
        No Flask, os decorators são usados para definir rotas. Por exemplo:
        @app.route('/decorator')
        indica que a função abaixo será executada quando o usuário acessar
        esse caminho no navegador.
        </p>
        """

if __name__ == "__main__":
    app.run(debug=True)