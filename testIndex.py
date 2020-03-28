
from flask import Flask
from interfaces import interface
from flask import render_template


app = Flask(__name__)

app.register_blueprint(interface)


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        debug=True,
    )