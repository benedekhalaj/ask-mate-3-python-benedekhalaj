import connection

QUESTIONS_FILE_PATH = 'data/questions.csv'
QUESTION_HEADER = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']

ANSWERS_FILE_PATH = 'data/answers.csv'
ANSWERS_HEADER = ['id', 'submission_time', 'vote_number', 'question_id', 'message', 'image']


def get_questions():
    return connection.open_file(QUESTIONS_FILE_PATH)


def get_answers():
    return connection.open_file(ANSWERS_FILE_PATH)


def export_question(question_list):
    question_list = add_new_id(question_list)
    connection.write_file(question_list, QUESTIONS_FILE_PATH, QUESTION_HEADER)


def add_new_id(question_list):
    last_id = int(question_list[-2]['id'])
    new_id = last_id + 1
    question_list[-1]['id'] = new_id
    return question_list
