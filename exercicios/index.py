from flask import Flask, request

app = Flask(__name__)

@app.route("/search")
def search():
    keyword = request.args.get('q')
    category = request.args.get('category')
    
    if keyword:
        return f"Reazando uma busca por '{keyword}' na categoria '{category}'."
    else:
        return "Por favor, forneça uma palavra-chave para fazer a busca."

if __name__ == "__main__":
    app.run()