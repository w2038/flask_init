from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact")
def contat():
    return render_template('contact.html')

@app.route("/user/<username>")
def user_profile(username):
    return render_template('profile.html', username = username)

if __name__ == '__main__':
    app.run()