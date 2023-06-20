from flask import Flask, request

app = Flask(__name__)

@app.route("/author")
def rota():
    autor = request.args.get('nome')
    
    return f"nome do autor: {autor}"


if __name__ == "__main__":
    app.run()