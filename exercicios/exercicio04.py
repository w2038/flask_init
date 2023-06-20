from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    
    
    return f"Formulário enviado com sucesso! <br><br>Nome: {name} <br> Emai: {email}<br>Mensagem: {message}"

if __name__ == "__main__":
    app.run()
