from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/login", methods=['GET', 'POST'])
def show_login_form():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')
        return f"Usuário e senha criado com sucesso!"
    else:
        return render_template('login.html')

if __name__ == "__main__":
    app.run()