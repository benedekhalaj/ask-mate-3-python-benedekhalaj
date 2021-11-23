from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/list")
def list_questions():
    return "Hello World!"


if __name__ == "__main__":
    app.run()
