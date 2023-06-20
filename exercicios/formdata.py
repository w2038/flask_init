from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        query = request.form.get('query')

        # Lógica para realizar a pesquisa
        return f"Você pesquisou por: {query}"
    else:
        return render_template("search.html")

if __name__ == '__main__':
    app.run()
