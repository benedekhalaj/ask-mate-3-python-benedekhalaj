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
def get_answers(cursor):
    query = """
        SELECT * FROM answer
    """
    cursor.execute(query)
    return cursor.fetchall()


def export_questions(question_list):
    # question_list = add_new_id(question_list, 'question')
    connection.save_csv_file(question_list, QUESTIONS_FILE_PATH, QUESTION_HEADERS)


def export_answers(answer_list):
    # answer_list = add_new_id(answer_list, 'answer')
    connection.save_csv_file(answer_list, ANSWERS_FILE_PATH, ANSWERS_HEADERS)


def add_new_id(data_type):
    if data_type == 'question':
        last_id = int(connection.open_id(QUESTION_ID_FILE_PATH))
        new_id = str(last_id + 1)
        connection.save_id(QUESTION_ID_FILE_PATH, new_id)
    else:
        last_id = int(connection.open_id(ANSWER_ID_FILE_PATH))
        new_id = str(last_id + 1)
        connection.save_id(ANSWER_ID_FILE_PATH, new_id)
    return new_id


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

