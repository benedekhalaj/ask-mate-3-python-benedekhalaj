from flask import Flask, render_template, request, redirect, url_for
import data_manager

app = Flask(__name__)


@app.route('/')
@app.route("/list")
def list_questions():
    questions = data_manager.get_questions()
    return render_template('list.html', questions=questions)


@app.route('/question/<question_id>')
def display_question(question_id):
    answers_from_file = data_manager.get_answers()
    questions = data_manager.get_questions()
    answers_for_question, question_details = [], []

    for answer in answers_from_file:
        if question_id == answer['id']:
            answers_for_question.append(answer)

    for question in questions:
        if question_id == question['id']:
            question_details.append(question['title'])
            question_details.append(question['message'])
            return render_template('display_question.html', question_id=question_id, answers=answers_from_file, question_details=question_details)


@app.route('/add-question', methods=['GET', 'POST'])
def add_question():
    if request.method == 'POST':
        questions = data_manager.get_questions()
        question = {}
        for key, value in request.form.items():
            question[key] = value
        questions.append(question)
        return redirect('/')
    return render_template('add_question.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0',
            debug=True,
            port=8000)
