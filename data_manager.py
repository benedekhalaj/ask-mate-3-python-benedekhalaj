from psycopg2.sql import SQL, Literal, Identifier
from psycopg2.extras import RealDictCursor

from database_common import connection_handler as connection


QUESTION_HEADERS = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']


@connection
def get_questions(cursor):
    query = """
        SELECT * FROM question
    """
    cursor.execute(query)
    return cursor.fetchall()


@connection
def get_question_by_id(cursor, question_id):
    query = """
        SELECT * FROM question
        WHERE id = {question_id}
    """
    cursor.execute(SQL(query).format(
        question_id=Literal(question_id)
    ))
    return cursor.fetchone()


@connection
def get_answers(cursor):
    query = """
        SELECT * FROM answer
    """
    cursor.execute(query)
    return cursor.fetchall()


@connection
def get_question_answers(cursor, question_id):
    query = """
        SELECT * FROM answer
        WHERE question_id = {question_id}
    """
    cursor.execute(SQL(query).format(
        question_id=Literal(question_id)
    ))

    return cursor.fetchall()


@connection
def insert_question(cursor, question_details):
    query = """
        INSERT INTO question(submission_time, view_number, vote_number, title, message, image)
        VALUES (
            {submission_time},
            0,
            0,
            {title},
            {message},
            {image}"""
    cursor.execute(SQL(query).format(
        submission_time=Literal(question_details['submission_time']),
        title=Literal(question_details['title']),
        message=Literal(question_details['message']),
        image=Literal(question_details['image'])
    ))


@connection
def insert_answer(cursor, new_answer):
    query = """
        INSERT INTO answer(submission_time, vote_number, question_id, message, image)
        VALUES (
            {submission_time},
            0,
            {question_id},
            {message},
            {image})
    """
    cursor.execute(SQL(query).format(
        submission_time=Literal(new_answer['submission_time']),
        question_id=Literal(new_answer['question_id']),
        message=Literal(new_answer['message']),
        image=Literal(new_answer['image'])
    ))


@connection
def get_new_id(cursor, submission_time):
    query = """
        SELECT id FROM question
        WHERE submission_time = {submission_time}
    """
    cursor.execute(SQL(query).format(
        submission_time=Literal(submission_time)
    ))
    return cursor.fetchone()


@connection
def increment_view_number(cursor, table, id):
    query = """
        UPDATE {table} 
        SET view_number = view_number + 1
        WHERE id = {id}
        """
    cursor.execute(SQL(query).format(
        table=Identifier(table),
        id=Literal(id)
    ))


@connection
def modify_vote_number(cursor, table, voting, id):
    if 'vote_up' in voting:
        voting = 1
    else:
        voting = -1
    query = """
        UPDATE {table} 
        SET vote_number = vote_number + {voting}
        WHERE id = {id} 
        """
    cursor.execute(SQL(query).format(
        table=Identifier(table),
        id=Literal(id),
        voting=Literal(voting)
    ))


@connection
def delete_table_data(cursor, table, data_id):
    query = """
        DELETE FROM {table}
        WHERE id = {data_id}
    """
    cursor.execute(SQL(query).format(
        data_id=Literal(data_id),
        table=Identifier(table)
    ))


@connection
def update_table(cursor, table, data):
    query = """
        UPDATE {table}
        SET title = {title}, message = {message}
        WHERE id = {id}
    """
    cursor.execute(SQL(query).format(
        table=Identifier(table),
        title=Literal(data['title']),
        message=Literal(data['message']),
        id=Literal(data['id'])
    ))


def sort_questions(orders):
    question_list = get_questions()
    order_title = orders['order_by']
    order_direction = orders['order_direction']
    if order_direction == 'asc':
        is_reverse = False
    elif order_direction == 'desc':
        is_reverse = True
    ordered_list = sorted(question_list, key=lambda item: item[order_title], reverse=is_reverse)
    return ordered_list


@connection
def update_table(cursor, table, data):
    query = """
        UPDATE {table}
        SET title = {title}, message = {message}
        WHERE id = {id}
    """
    cursor.execute(SQL(query).format(
        table=Identifier(table),
        title=Literal(data['title']),
        message=Literal(data['message']),
        id=Literal(data['id'])
    ))


@connection
def search_for_question(cursor, keyword):
    answers_rdr = search_for_answer(keyword)
    answers = tuple([answer['question_id'] for answer in answers_rdr])
    if answers:
        query = """
        SELECT * FROM question
        WHERE message LIKE {keyword} OR title LIKE {keyword} OR id in {answers}
        """
    else:
        query = """
                SELECT * FROM question
                WHERE message LIKE {keyword} OR title LIKE {keyword}
                """
    cursor.execute(SQL(query).format(
        keyword=Literal(f'%{keyword}%'),
        answers=Literal(answers)
    ))
    return cursor.fetchall()


@connection
def search_for_answer(cursor, keyword):
    query = """
    SELECT question_id FROM answer
    WHERE message LIKE {keyword}
    """
    cursor.execute(SQL(query).format(
        keyword=Literal(f'%{keyword}%')
    ))
    return cursor.fetchall()


@connection
def add_new_comment(cursor, comment_details):
    query = """
    INSERT INTO comment (question_id, message, submission_time)
    VALUES ({question_id}, {message}, {submission_time})
    """
    cursor.execute(SQL(query).format(
        question_id=Literal(comment_details['question_id']),
        message=Literal(comment_details['message']),
        submission_time=Literal(comment_details['submission_time'])
    ))

@connection
def get_comments(cursor, id):
    query = """
    SELECT submission_time, message FROM comment
    WHERE question_id = {id}
    """
    cursor.execute(SQL(query).format(
        id=Literal(id)
    ))
    return cursor.fetchall()