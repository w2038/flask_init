from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/form2")
def show_form():
    return render_template("form2.html")
    
@app.route("/submit", methods=['POST'])
def submit_form():
    nome = request.form.get("name")
    idade = request.form.get("age")
    
    return render_template("result2.html", name=nome, age=idade)

if __name__ == "__main__":
    app.run(debug=True)