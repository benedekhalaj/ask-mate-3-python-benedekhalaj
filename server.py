from flask import Flask, render_template, request, redirect, url_for
import data_manager

app = Flask(__name__)


@app.route('/')
@app.route("/list")
def list_questions():
    questions = data_manager.get_questions()
    if 'order_by' in request.form:
        return render_template(f'/list?ored_by{request.form["order_by"]}&order_direction{request.form["order_direction"]}')
    return render_template('list.html', questions=questions)


@app.route('/question/<question_id>')
def display_question(question_id):
    return render_template('display_question.html', question_id=question_id)


@app.route('/question/<question_id>/new-answer')
def post_answer(question_id):
    return render_template('post_answer.html')


@app.route('/add-question', methods=['GET', 'POST'])
def add_question():
    if request.method == 'POST':
        questions = data_manager.get_questions()
        question = {}
        for key, value in request.form.items():
            question[key] = value
        questions.append(question)
        data_manager.export_questions(questions)
        return redirect('/')
    return render_template('add_question.html')


@app.route('/sort-question')
def sort_question():
    return render_template('sort_question.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0',
            debug=True,
            port=8000)
