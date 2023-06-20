from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/login", methods=['GET'])
def show_login_form():
        return render_template('login.html')
    
@app.route("/login", methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username == 'admin' and password == 'admin':
        return "login bem sucedido!"
    else:
        return "Falha no ligin"


if __name__ == "__main__":
    app.run()