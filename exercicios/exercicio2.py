from flask import Flask

app = Flask(__name__)


users = {
    1:{'name': 'Wagner Silva', 'age': 33},
    2:{'name': 'Lorena Lopes', 'age': 27},
    3:{'name': 'Max Millian',  'age': 1}
}

@app.route("/user/<int:user_id>")
def show_user(user_id):
    if user_id in users:
        user = users[user_id]
        return f"Nome: {user['name']}, Idade: {user['age']}"
    else:
        return "Usuário não encontrado"
    
if __name__ == "__main__":
    app.run()