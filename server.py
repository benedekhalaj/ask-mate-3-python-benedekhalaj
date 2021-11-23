from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
@app.route("/list")
def list_questions():
    questions = []
    for _ in range(5):
        questions.append({'id': '0', 'title': 'test', 'name': 'zsu'})
    return render_template('list.html', questions=questions)


if __name__ == "__main__":
    app.run(host='0.0.0.0',
            debug=True,
            port=8000)
