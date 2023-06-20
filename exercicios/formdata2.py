from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        return f"Conta criada para o usuário:{username}"
    else:
        return render_template("signup.html")
    
if __name__ == "__main__":
    app.run()