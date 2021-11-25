from flask import Flask, render_template, request, redirect
import data_manager
import util


app = Flask(__name__)


@app.route('/')
@app.route("/list")
def list_questions():
    questions = data_manager.sort_questions(request.args) if request.args else data_manager.get_questions()
    return render_template('list.html', questions=reversed(questions), titles=data_manager.QUESTION_HEADERS)


@app.route('/question/<question_id>')
def display_question(question_id):
    answers = data_manager.get_answers()
    questions = data_manager.get_questions()
    question_answers = util.get_data_list(answers, 'question_id', question_id)
    question = util.get_data_by_id(questions, 'id', question_id)
    return render_template('display_question.html', question_id=question_id, answers=question_answers, question=question)


@app.route('/question/<question_id>/view')
def increment_view_number(question_id):
    questions = data_manager.get_questions()
    question, index = util.get_data_and_index_by_id(questions, 'id', question_id)
    questions[index]['view_number'] = util.modify_number(question, 'view_number', '+')
    data_manager.export_questions(questions)
    return redirect(f'/question/{question_id}')


@app.route('/add-question', methods=['GET', 'POST'])
def add_question():
    if request.method == 'POST':
        new_id = data_manager.add_new_id('question')
        new_question = {
            "view_number": 0,
            "vote_number": 0,
            "id": new_id,
            "image": util.upload_file(request, new_id),
            "submission_time": util.add_submission_time()
        }
        new_question = util.update_data_by_form(new_question, request.form)
        questions = util.add_new_data(new_question, data_manager.get_questions())
        data_manager.export_questions(questions)
        return redirect(f'/question/{new_id}')
    return render_template('add_question.html')


@app.route('/question/<question_id>/edit', methods=['GET', 'POST'])
def edit_question(question_id):
    questions = data_manager.get_questions()
    current_question, current_id = util.get_data_and_index_by_id(questions, 'id', question_id)
    if request.method == 'POST':
        questions[current_id] = util.update_data_by_form(questions[current_id], request.form)
        util.delete_file('questions', question_id)
        questions[current_id]['image'] = util.upload_file(request, question_id)
        data_manager.export_questions(questions)
        return redirect(f'/question/{question_id}')
    return render_template('edit_question.html', question=current_question)


@app.route('/question/<question_id>/delete', methods=['POST'])
@app.route('/question/<question_id>/vote_up')
@app.route('/question/<question_id>/vote_down')
def change_question(question_id):
    questions = data_manager.get_questions()
    operator = '+' if 'vote_up' in request.base_url else '-'
    if 'delete' not in request.base_url:
        questions = util.change_vote_number(questions, question_id, operator)
    else:
        questions = util.delete_data(questions, question_id)
        data_manager.export_answers(util.delete_data(data_manager.get_answers(), question_id, 'question_id'))
        util.delete_file('questions', question_id)
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
        new_id = data_manager.add_new_id('answer')
        new_answer = {
            'question_id': question_id,
            'vote_number': 0,
            'id': new_id,
            'image': util.upload_file(request, new_id, 'answers'),
            'submission_time': util.add_submission_time()
        }
        util.update_data_by_form(new_answer, request.form)
        util.add_new_data(new_answer, answers)
        data_manager.export_answers(answers)
        return redirect(f'/question/{question_id}')


@app.route('/answer/<answer_id>/delete', methods=['POST'])
@app.route('/answer/<answer_id>/vote_up')
@app.route('/answer/<answer_id>/vote_down')
def change_answer(answer_id):
    answers = data_manager.get_answers()
    question_id = util.get_data_by_id(answers, "id", answer_id)["question_id"]
    if 'delete' not in request.base_url:
        answers = util.change_vote_number(answers, answer_id, '+' if 'vote_up' in request.base_url else '-')
    else:
        answers = util.delete_data(answers, answer_id)
        util.delete_file('answers', answer_id)
    data_manager.export_answers(answers)
    return redirect(f'/question/{question_id}')


if __name__ == "__main__":
    app.run(host='0.0.0.0',
            debug=True,
            port=8000)
