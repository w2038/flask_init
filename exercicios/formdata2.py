from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/signup", methods=['POST'])
def signup_up():
    username = request.form.get('username')
    password = request.form.get('password')

    return f"Conta criada para o usuário:{username}"

    
if __name__ == "__main__":
    app.run()