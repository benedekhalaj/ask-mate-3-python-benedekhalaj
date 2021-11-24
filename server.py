from flask import Flask, render_template, request, redirect, url_for
import data_manager
import util

app = Flask(__name__)


@app.route('/')
@app.route("/list")
def list_questions():
    titles = data_manager.QUESTION_HEADERS
    if request.args:
        questions = data_manager.sort_questions(request.args)
    else:
        questions = data_manager.get_questions()
    return render_template('list.html', questions=questions, titles=titles)


@app.route('/question/<question_id>')
def display_question(question_id):
    answers = data_manager.get_answers()
    questions = data_manager.get_questions()
    answers_for_question = util.get_data_list(answers, 'question_id', question_id)
    question = util.get_data_by_id(questions, 'id', question_id)
    return render_template('display_question.html', question_id=question_id, answers=answers_for_question, question=question)


@app.route('/add-question', methods=['GET', 'POST'])
def add_question():
    if request.method == 'POST':
        new_question = {"view_number": 0, "vote_number": 0, "id": data_manager.add_new_id('question')}
        new_question = util.update_data_by_form(new_question, request.form)
        questions = util.add_new_data(new_question, data_manager.get_questions())
        data_manager.export_questions(questions)
        return redirect('/')
    else:
        return render_template('add_question.html')


@app.route('/question/<question_id>/edit', methods=['GET', 'POST'])
def edit_question(question_id):
    questions = data_manager.get_questions()
    current_question, current_id = util.get_data_and_index_by_id(questions, 'id', question_id)
    if request.method == 'GET':
        return render_template('edit_question.html', question=current_question)
    else:
        questions[current_id] = util.update_data_by_form(questions[current_id], request.form)
        data_manager.export_questions(questions)
        return redirect(f'/question/{question_id}')


@app.route('/question/<question_id>/delete', methods=['POST'])
def delete_question(question_id):
    questions = data_manager.get_questions()
    question, index = util.get_data_and_index_by_id(questions, 'id', question_id)
    questions.pop(index)
    data_manager.export_questions(questions)

    answers = data_manager.get_answers()
    selected_answers = util.get_data_list(answers, 'question_id', question_id)
    for selected_answer in selected_answers:
        answers.remove(selected_answer)
    data_manager.export_answers(answers)
    return redirect('/list')


@app.route('/sort-question')
def sort_question():
    return render_template('sort_question.html')


@app.route('/question/<question_id>/vote_up')
@app.route('/question/<question_id>/vote_down')
def vote_question(question_id):
    questions = data_manager.get_questions()
    if 'vote_up' in request.base_url:
        questions = util.vote(questions, question_id, '+')
    else:
        questions = util.vote(questions, question_id, '-')
    data_manager.export_questions(questions)
    return redirect('/list')


@app.route('/question/<question_id>/new-answer', methods=['GET', 'POST'])
def post_answer(question_id):
    questions = data_manager.get_questions()
    answers = data_manager.get_answers()
    if request.method == 'GET':
        selected_answers = util.get_data_list(answers, 'question_id', question_id)
        selected_question = util.get_data_by_id(questions, 'id', question_id)
        return render_template('post_answer.html', question=selected_question, answers=selected_answers)
    else:
        new_answer = {'question_id': question_id, 'vote_number': 0, 'id': data_manager.add_new_id('answer')}
        util.update_data_by_form(new_answer, request.form)
        util.add_new_data(new_answer, answers)
        data_manager.export_answers(answers)
        return redirect(f'/question/{question_id}')


@app.route('/answer/<answer_id>/delete', methods=['POST'])
def delete_answer(answer_id):
    answers = data_manager.get_answers()
    question_id = util.get_data_by_id(answers, 'id', answer_id)['question_id']
    answers = util.delete_data(answers, answer_id)
    data_manager.export_answers(answers)
    return redirect(f'/question/{question_id}')


@app.route('/answer/<answer_id>/vote_up')
@app.route('/answer/<answer_id>/vote_down')
def vote_answer(answer_id):
    answers = data_manager.get_answers()
    answer_question_id = util.get_data_by_id(answers, 'question_id', answer_id)['question_id']
    if 'vote_up' in request.base_url:
        answers = util.vote(answers, answer_id, '+')
    else:
        answers = util.vote(answers, answer_id, '-')
    data_manager.export_answers(answers)
    return redirect(f'/question/{answer_question_id}')


if __name__ == "__main__":
    app.run(host='0.0.0.0',
            debug=True,
            port=8000)
