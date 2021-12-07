import csv
from psycopg2 import sql
from psycopg2.extras import RealDictCursor

import database_common as database
import connection

QUESTIONS_FILE_PATH = 'data/questions.csv'
QUESTION_ID_FILE_PATH = 'data/question_id.txt'
QUESTION_HEADERS = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']

ANSWERS_FILE_PATH = 'data/answers.csv'
ANSWER_ID_FILE_PATH = 'data/answer_id.txt'
ANSWERS_HEADERS = ['id', 'submission_time', 'vote_number', 'question_id', 'message', 'image']


@database.connection_handler
def get_questions(cursor):
    query = """
        SELECT * FROM question
    """
    cursor.execute(query)
    return cursor.fetchall()


@database.connection_handler
def get_question_by_id(cursor, question_id):
    cursor.execute(sql.SQL("""
        SELECT * FROM question
        WHERE id = {question_id}
    """).format(question_id=sql.Literal(question_id)))
    return cursor.fetchone()


@database.connection_handler
def get_answers(cursor):
    query = """
        SELECT * FROM answer
    """
    cursor.execute(query)
    return cursor.fetchall()


@database.connection_handler
def get_question_answers(cursor, question_id):
    cursor.execute(sql.SQL("""
        SELECT * FROM answer
        WHERE question_id = {question_id}
    """).format(question_id=sql.Literal(question_id)))

    return cursor.fetchall()


@database.connection_handler
def insert_question(cursor, question_details):
    cursor.execute(sql.SQL("""
        INSERT INTO question(submission_time, view_number, vote_number, title, message, image)
        VALUES (
            {submission_time},
            0,
            0,
            {title},
            {message},
            {image}
            )
    """).format(submission_time=sql.Literal(question_details['submission_time']),
                title=sql.Literal(question_details['title']),
                message=sql.Literal(question_details['message']),
                image=sql.Literal(question_details['image'])))


@database.connection_handler
def insert_answer(cursor, new_answer):
    cursor.execute(sql.SQL("""
        INSERT INTO answer(submission_time, vote_number, question_id, message, image)
        VALUES (
            {submission_time},
            0,
            {question_id},
            {message},
            {image})
    """).format(submission_time=sql.Literal(new_answer['submission_time']),
                question_id=sql.Literal(new_answer['question_id']),
                message=sql.Literal(new_answer['message']),
                image=sql.Literal(new_answer['image'])))


@database.connection_handler
def get_new_id(cursor, submission_time):
    cursor.execute(sql.SQL("""
        SELECT id FROM question
        WHERE submission_time = {}
    """).format(sql.Literal(submission_time)))
    return cursor.fetchone()


@database.connection_handler
def increment_view_number(cursor, table, id):
    cursor.execute(sql.SQL("""
        UPDATE {table} 
        SET view_number = view_number + 1
        WHERE id = {id}
        """
                           ).format(table=sql.Identifier(table),
                                    id=sql.Literal(id)))


@database.connection_handler
def modify_vote_number(cursor, table, voting, id):
    if 'vote_up' in voting:
        voting = 1
    else:
        voting = -1
    cursor.execute(sql.SQL("""
        UPDATE {table} 
        SET vote_number = vote_number + {voting}
        WHERE id = {id} 
        """
                           ).format(table=sql.Identifier(table),
                                    id=sql.Literal(id),
                                    voting=sql.Literal(voting)))


@database.connection_handler
def delete_table_data(cursor, table, data_id):
    cursor.execute(sql.SQL("""
        DELETE FROM {table}
        WHERE id = {data_id}
    """).format(data_id=sql.Literal(data_id),
                table=sql.Identifier(table)))


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


@database.connection_handler
def update_table(cursor, table, data):
    query = """
        UPDATE {table}
        SET title = {title}, message = {message}
        WHERE id = {id}
    """
    cursor.execute(sql.SQL(query).format(
        table=sql.Identifier(table),
        title=sql.Literal(data['title']),
        message=sql.Literal(data['message']),
        id=sql.Literal(data['id'])
    ))


@database.connection_handler
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
    cursor.execute(sql.SQL(query).format(
        keyword=sql.Literal(f'%{keyword}%'),
        answers=sql.Literal(answers)
    ))
    return cursor.fetchall()


@database.connection_handler
def search_for_answer(cursor, keyword):
    query = """
    SELECT question_id FROM answer
    WHERE message LIKE {keyword}
    """
    cursor.execute(sql.SQL(query).format(
        keyword=sql.Literal(f'%{keyword}%')
    ))
    return cursor.fetchall()
