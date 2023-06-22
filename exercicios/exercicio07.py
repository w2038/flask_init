from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/contact")
def show_contact_form():
    return render_template("contact.html")

@app.route("/submit_contact", methods=['POST'])
def submit_contact_form():
    nome = request.form.get("name")
    email = request.form.get("email")
    mensagem = request.form.get("message")
    
    return render_template("submit_contact_form.html", name=nome, email=email, message=mensagem )

if __name__ == "__main__":
    app.run(debug=True)