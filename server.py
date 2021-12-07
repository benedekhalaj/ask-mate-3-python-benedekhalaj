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
    questions = data_manager.get_questions()
    question_answers = data_manager.get_question_answers(question_id)
    question = util.get_data_by_id(questions, 'id', question_id)
    return render_template('display_question.html', question_id=question_id, answers=question_answers, question=question)


@app.route('/search')
def search_question():
    keyword = request.args.get('q')
    searched_questions = data_manager.search_for_question(keyword)
    return render_template('search_question.html', questions=searched_questions, titles=data_manager.QUESTION_HEADERS)


@app.route('/question/<question_id>/view')
def increment_view_number(question_id):
    data_manager.increment_view_number(table='question', id=question_id)
    return redirect(f'/question/{question_id}')


@app.route('/add-question', methods=['GET', 'POST'])
def add_question():
    if request.method == 'POST':
        new_question = {"submission_time": util.add_submission_time()}
        new_question = util.update_data_by_form(new_question, request.form)
        data_manager.insert_question(new_question)

        new_question_id = data_manager.get_new_id(new_question['submission_time'])
        image_url = util.upload_file(request, new_question_id)
        data_manager.insert_image('question', new_question_id, image_url)

        return redirect(f'/question/{new_question_id}')
    return render_template('add_question.html')


@app.route('/question/<question_id>/edit', methods=['GET', 'POST'])
def edit_question(question_id):
    question = data_manager.get_question_by_id(question_id)
    if request.method == 'POST':
        question = util.update_data_by_form(question, request.form)
        data_manager.update_table(table='question', data=question)

        util.delete_file('questions', question_id)
        image_url = util.upload_file(request, question_id)
        data_manager.insert_image('question', question_id, image_url)

        return redirect(f'/question/{question_id}')
    return render_template('edit_question.html', question=question)


@app.route('/question/<question_id>/delete', methods=['POST'])
@app.route('/question/<question_id>/vote_up')
@app.route('/question/<question_id>/vote_down')
def change_question(question_id):
    if 'delete' not in request.base_url:
        data_manager.modify_vote_number(table='question', voting=request.base_url, id=question_id)
    else:
        data_manager.delete_table_data(table='question', data_id=question_id)
        util.delete_file('questions', question_id)
    return redirect('/list')


@app.route('/question/<question_id>/new-answer', methods=['GET', 'POST'])
def post_answer(question_id):
    if request.method == 'GET':
        selected_answers = data_manager.get_question_answers(question_id=question_id)
        selected_question = data_manager.get_question_by_id(question_id)
        return render_template('post_answer.html', question=selected_question, answers=selected_answers)
    else:
        new_answer = {
            'question_id': question_id,
            'submission_time': util.add_submission_time()
        }
        util.update_data_by_form(new_answer, request.form)
        data_manager.insert_answer(new_answer)
        new_answer_id = data_manager.get_new_id(new_answer['submission_time'], 'answer')

        image_url = util.upload_file(request, new_answer_id, 'answers')
        data_manager.insert_image('answer', new_answer_id, image_url)

        return redirect(f'/question/{question_id}')


@app.route('/answer/<answer_id>/delete', methods=['POST'])
@app.route('/answer/<answer_id>/vote_up')
@app.route('/answer/<answer_id>/vote_down')
def change_answer(answer_id):
    answers = data_manager.get_answers()
    question_id = util.get_data_by_id(answers, "id", answer_id)["question_id"]
    if 'delete' not in request.base_url:
        data_manager.modify_vote_number(table='answer', voting=request.base_url, id=answer_id)
    else:
        data_manager.delete_table_data(table='answer', data_id=answer_id)
        util.delete_file('answers', answer_id)
    return redirect(f'/question/{question_id}')


@app.route('/question/<question_id>/new-comment', methods=['GET', 'POST'])
def add_new_comment(question_id):
    selected_question = data_manager.get_question_by_id(question_id)
    if request.method == 'POST':
        new_comment = request.args.get('new-comment')

        return redirect(f'/question/{question_id}')
    return render_template('comments.html', question_id=question_id, question=selected_question)


if __name__ == "__main__":
    app.run(host='0.0.0.0',
            debug=True,
            port=8000)
