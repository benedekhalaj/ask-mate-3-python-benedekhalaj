from flask import Flask, render_template, request, redirect, url_for
import data_manager
import util


app = Flask(__name__)

COMMENT_HEADER = ['submission_time', 'message', 'edited_count']
ANSWER_HEADER = ['submission_time', 'vote_number', 'message', 'image']
QUESTION_HEADER = ['title', 'message', 'image']


@app.route('/')
@app.route("/list")
def list_questions():
    if "list" not in request.base_url:
        questions = data_manager.sort_questions(request.args) if request.args else data_manager.get_questions(limit=3)
        is_main_page = True
    else:
        questions = data_manager.sort_questions(request.args) if request.args else data_manager.get_questions()
        is_main_page = False
    return render_template('list.html', questions=reversed(questions), titles=data_manager.QUESTION_HEADERS, main_page=is_main_page)


@app.route('/search')
def search_question():
    def split_by_pattern(text, pattern, keyword):
        return text.replace(keyword, f"{pattern}{keyword}{pattern}").split(pattern)

    keyword = request.args.get('q')
    searched_questions = data_manager.search_for_question(keyword)
    searched_answers = data_manager.search_for_answer(keyword)
    split_pattern = '$ß$'
    for question in searched_questions:
        question['title'] = split_by_pattern(question['title'], split_pattern, keyword)
        question['message'] = split_by_pattern(question['message'], split_pattern, keyword)

    for answer in searched_answers:
        answer['message'] = split_by_pattern(answer['message'], split_pattern, keyword)
        print(searched_answers)
    return render_template('search_question.html',
                           questions=searched_questions,
                           answers=searched_answers,
                           titles=data_manager.QUESTION_HEADERS,
                           keyword=keyword,
                           search=True)


@app.route('/question/<question_id>/view')
def increment_view_number(question_id):
    data_manager.increment_view_number(table='question', id=question_id)
    return redirect(f'/question/{question_id}')


@app.route('/question/<question_id>', methods=['GET', 'POST'])
def display_question(question_id):
    questions = data_manager.get_questions()
    question_answers = data_manager.get_question_answers(question_id)
    question = util.get_data_by_id(questions, 'id', question_id)
    comments = data_manager.get_comments()

    tags = data_manager.get_tags()
    question_tags = data_manager.get_question_tags(question_id)
    question_tags = [tag['tag_id'] for tag in question_tags]

    return render_template('display_question.html',
                           question=question,
                           question_tags=question_tags,
                           question_header=QUESTION_HEADER,
                           answers=question_answers,
                           answer_header=ANSWER_HEADER,
                           comments=comments,
                           comment_header=COMMENT_HEADER,
                           tags=tags)


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
    question = data_manager.get_data_by_id(table='question', id=question_id)
    if request.method == 'POST':
        question = util.update_data_by_form(question, request.form)
        data_manager.update_table(table='question', data=question)

        util.delete_file('questions', question_id)
        image_url = util.upload_file(request, question_id)
        data_manager.insert_image('question', question_id, image_url)

        return redirect(f'/question/{question_id}')
    return render_template('edit_question.html', question=question)


@app.route('/question/<question_id>/new-tag', methods=['GET', 'POST'])
def add_new_tag(question_id):
    tags = data_manager.get_tags()
    question_tags = data_manager.get_question_tags(question_id)
    question_tags = [tag['tag_id'] for tag in question_tags]
    print(question_tags)
    if request.method == 'GET':
        return render_template('add_new_tag.html', tags=tags, question_tags=question_tags, question_id=question_id)

    else:
        if request.form['submit_button'] == 'add_new_tag':
            new_tag = request.form.get('new_tag')
            if new_tag:
                data_manager.add_new_tag(new_tag)
            return redirect(url_for('add_new_tag', question_id=question_id))

        else:
            data_manager.delete_tags_from_question(question_id)
            selected_tags = [key for key in request.form.keys() if key != 'submit_button']
            for tag in tags:
                if tag['name'] in selected_tags:
                    data_manager.add_tag_to_question(question_id, tag['id'])
            return redirect(url_for('display_question', question_id=question_id))


@app.route('/question/<question_id>/tag/<tag_id>')
def delete_tag(question_id, tag_id):
    data_manager.delete_tag(tag_id)
    return redirect(url_for('add_new_tag', question_id=question_id))


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


@app.route('/question/<question_id>/new-comment', methods=['GET', 'POST'])
@app.route('/answer/<answer_id>/new-comment', methods=['GET', 'POST'])
def add_new_comment(question_id=None, answer_id=None):
    if 'question' in request.base_url:
        selected_post = data_manager.get_data_by_id(table='question', id=question_id)
        header = QUESTION_HEADER
    else:
        selected_post = data_manager.get_data_by_id(table='answer', id=answer_id)
        header = ANSWER_HEADER
    if request.method == 'POST':
        new_comment = {
            'question_id': question_id,
            'answer_id': answer_id,
            'submission_time': util.add_submission_time()
        }
        util.update_data_by_form(new_comment, request.form)
        data_manager.add_new_comment(new_comment)
        if answer_id:
            question_id = selected_post['question_id']
        return redirect(f'/question/{question_id}')
    return render_template('comments.html', question_id=question_id,
                           answer_id=answer_id,
                           question=selected_post,
                           header=header)


@app.route('/question/<question_id>/new-answer', methods=['GET', 'POST'])
def post_answer(question_id):
    if request.method == 'GET':
        selected_answers = data_manager.get_question_answers(question_id=question_id)
        selected_question = data_manager.get_data_by_id(table='question', id=question_id)
        return render_template('post_answer.html',
                               question=selected_question,
                               answers=selected_answers,
                               header=QUESTION_HEADER)
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


@app.route('/answer/<answer_id>/edit', methods=['GET', 'POST'])
def edit_answer(answer_id):
    message_and_question_id = data_manager.get_answer_by_id(answer_id)
    question_id = message_and_question_id[0]['question_id']
    message = message_and_question_id[0]['message']
    question = data_manager.get_data_by_id(table='question', id=question_id)
    if request.method == 'POST':
        edited_answer = {
            'answer_id': answer_id,
            'submission_time': util.add_submission_time()
        }
        util.update_data_by_form(edited_answer, request.form)
        data_manager.update_answer(edited_answer)
        util.delete_file('answers', answer_id)
        image_url = util.upload_file(request, answer_id)
        data_manager.insert_image('answer', answer_id, image_url)
        return redirect(f'/question/{question_id}')
    return render_template('edit_answer.html',
                           answer_id=answer_id,
                           message_to_edit=message,
                           question=question,
                           header=QUESTION_HEADER)


@app.route('/comment/<comment_id>/edit', methods=['GET', 'POST'])
def edit_comment(comment_id):
    comment = data_manager.get_data_by_id(table='comment' ,id=comment_id)
    if comment['answer_id']:
        id, header, table = comment['answer_id'], ANSWER_HEADER, 'answer'
        question_id = data_manager.get_data_by_id(table=table, id=id)['question_id']
    else:
        id, header, table = comment['question_id'], QUESTION_HEADER, 'question'
        question_id = comment['question_id']
    if request.method == 'GET':
        answer = data_manager.get_data_by_id(table=table, id=id)
        return render_template('edit_comment.html',
                               comment_id=comment_id,
                               message_to_edit=comment['message'],
                               question=answer,
                               h1=table.capitalize(),
                               header=COMMENT_HEADER)
    else:
        comment['message'] = request.form.get('message')
        comment['submission_time'] = util.add_submission_time()
        data_manager.update_comment(message=request.form.get('message'), comment_id=comment_id)

        return redirect(url_for('display_question', question_id=question_id))


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


@app.route('/comment/<comment_id>/delete', methods=['GET', 'POST'])
def delete_comment(comment_id):
    comments = data_manager.get_comments()
    comment = util.get_data_by_id(comments, "id", comment_id)
    if request.method == 'POST':
        if comment['answer_id']:
            id_for_redirect = data_manager.get_data_by_id(table='answer', id=comment['answer_id'])['question_id']
        else:
            id_for_redirect = comment['question_id']
        if request.form['confirm_deleting'] == 'YES':
            data_manager.delete_table_data(table='comment', data_id=comment_id)
            return redirect(f'/question/{id_for_redirect}')
        elif request.form['confirm_deleting'] == 'NO':
            return redirect(f'/question/{id_for_redirect}')
    return render_template('confirm_delete_comment.html',
                           comment=comment,
                           header=COMMENT_HEADER)


if __name__ == "__main__":
    app.run(host='0.0.0.0',
            debug=True,
            port=8000)
