from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    headline = "Hello, world!" #variable called headline
    return render_template("hello.html", headline=headline)

