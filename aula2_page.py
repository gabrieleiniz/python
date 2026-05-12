from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Currículo</title>
        </head>
        <body>
            <h1>Currículo</h1>

            <h2>Informações Pessoais</h2>
            <ul>
                <li><strong>Nome:</strong> Gabriel Diniz</li>  
                <li><strong>Email:</strong> dinizgabriel777@Gmail.com</li>
                <li><strong>Telefone:</strong> (31) 98315-0897 </li>
            </ul>

            <h2>Habilidades</h2>
            <ul>
                <li><strong>Falar ingles quase fluentemente:</strong> 
                <li><strong>Saber python, html e java:</strong> 
                <li><strong>Trabalhar em equipe:</strong> 
            </ul>
        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
