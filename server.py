from flask import Flask, render_template, request, redirect, url_for
import data_manager

app = Flask(__name__)


@app.route('/')
@app.route("/list")
def list_questions():
    titles = data_manager.QUESTION_HEADER
    if request.args:
        questions = data_manager.sort_questions(request.args)
    else:
        questions = data_manager.get_questions()
    return render_template('list.html', questions=questions, titles=titles)


@app.route('/question/<question_id>')
def display_question(question_id):
    answers_from_file = data_manager.get_answers()
    questions = data_manager.get_questions()
    answers_for_question = []

    for answer in answers_from_file:
        if question_id == answer['question_id']:
            answers_for_question.append(answer)

    for index, question in enumerate(questions):
        if question_id == question['id']:
            increment_question_number(questions, index, 'view_number')
            return render_template('display_question.html', question_id=question_id, answers=answers_for_question, question=question)


def increment_question_number(questions, index, key):
    new_number = int(questions[index][key]) + 1
    questions[index][key] = new_number
    data_manager.export_questions(questions)


def decrement_question_number(questions, index, key):
    new_number = int(questions[index][key]) - 1
    questions[index][key] = new_number
    data_manager.export_questions(questions)


@app.route('/add-question', methods=['GET', 'POST'])
def add_question():
    if request.method == 'POST':
        questions = data_manager.get_questions()
        question = {"view_number": 0, "vote_number": 0}
        for key, value in request.form.items():
            question[key] = value
        questions.append(question)
        data_manager.export_questions(questions)
        return redirect('/')
    return render_template('add_question.html')


@app.route('/question/<question_id>/edit', methods=['GET', 'POST'])
def edit_question(question_id):
    questions = data_manager.get_questions()
    for index, question in enumerate(questions):
        if question['id'] == question_id:
            current_question = question
            current_id = index
            break
    if request.method == 'GET':
        return render_template('edit_question.html', question=current_question)
    else:
        for key, value in request.form.items():
            questions[current_id][key] = value
        data_manager.export_questions(questions)
        return redirect(f'/question/{question_id}')


@app.route('/question/<question_id>/delete', methods=['POST'])
def delete_question(question_id):
    questions = data_manager.get_questions()
    for index, question in enumerate(questions):
        if question['id'] == question_id:
            questions.pop(index)
            break
    data_manager.export_questions(questions)
    return redirect('/list')


@app.route('/sort-question')
def sort_question():
    return render_template('sort_question.html')


@app.route('/question/<question_id>/vote_up')
def vote_question_up(question_id):
    questions = data_manager.get_questions()
    for index, question in enumerate(questions):
        if question_id == question['id']:
            increment_question_number(questions, index, 'vote_number')
    return redirect('/list')


@app.route('/question/<question_id>/vote_down')
def vote_question_down(question_id):
    questions = data_manager.get_questions()
    for index, question in enumerate(questions):
        if question_id == question['id']:
            decrement_question_number(questions, index, 'vote_number')
    return redirect('/list')


@app.route('/question/<question_id>/new-answer', methods=['GET', 'POST'])
def post_answer(question_id):
    questions = data_manager.get_questions()
    answers = data_manager.get_answers()
    if request.method == 'GET':
        selected_answers = [answer for answer in answers if answer['question_id'] == question_id]
        for question in questions:
            if question['id'] == question_id:
                selected_question = question
                break
        return render_template('post_answer.html', question=selected_question, answers=selected_answers)
    else:
        new_answer = {'question_id': question_id}
        for key, value in request.form.items():
            new_answer[key] = value
        answers.append(new_answer)
        data_manager.export_answers(answers)
        return redirect(f'/question/{question_id}')


@app.route('/answer/<answer_id>/delete', methods=['POST'])
def delete_answer(answer_id):
    answers = data_manager.get_answers()
    for index, answer in enumerate(answers):
        if answer_id == answer['id']:
            question_id = answer['question_id']
            answers.pop(index)
            break
    data_manager.export_answers(answers)
    return redirect(f'/question/{question_id}')


if __name__ == "__main__":
    app.run(host='0.0.0.0',
            debug=True,
            port=8000)
