from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World</P>"


@app.route("/about")
def sobre_nos():
    return "Sobre nós"


@app.route("/contact")
def contato():
    return "Contato"

if __name__ == '__main__':
    app.run()