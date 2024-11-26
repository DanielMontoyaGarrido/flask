from flask import Flask, render_template

print(__name__)
app = Flask(__name__)

@app.route("/first")
def hello_world():
    return render_template("jinja_intro.html")

