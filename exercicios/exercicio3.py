from flask import Flask, render_template

app = Flask(__name__)

users = [
    {'name': 'John Doe', 'age': 25},
    {'name': 'Jane Smith', 'age': 30},
    {'name': 'Alice Johnson', 'age': 28}
]

@app.route("/index")
def index():
    return render_template("index.html", users=users)

if __name__ == "__main__":
    app.run()