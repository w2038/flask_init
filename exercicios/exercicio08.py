from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/login2", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        
        if username == 'admin' and password == "123":
             return redirect(url_for('dashboard'))
        else:
            error = 'Credenciais inválidas. Tente novamente.'
            return render_template('login2.html', error=error)
    else:
        return render_template('login2.html')

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)