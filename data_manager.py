import connection

QUESTIONS_FILE_PATH = 'data/questions.csv'
QUESTION_HEADER = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']

ANSWERS_FILE_PATH = 'data/answers.csv'
ANSWERS_HEADER = ['id', 'submission_time', 'vote_number', 'question_id', 'message', 'image']


def get_questions():
    return connection.open_file(QUESTIONS_FILE_PATH)


def get_answers():
    return connection.open_file(ANSWERS_FILE_PATH)


def export_questions(question_list):
    question_list = add_new_id(question_list)
    connection.write_file(question_list, QUESTIONS_FILE_PATH, QUESTION_HEADER)


def export_answers(answer_list):
    answer_list = add_new_id(answer_list)
    connection.write_file(answer_list, ANSWERS_FILE_PATH, ANSWERS_HEADER)


def add_new_id(data_list):
    last_id = int(data_list[-2]['id'])
    new_id = last_id + 1
    data_list[-1]['id'] = new_id
    return data_list


def sort_questions(order):
    question_list = get_questions()
    order_title = order['order_by']
    order_direction = order['order_direction']
    if order_direction == 'asc':
        question_list.sort()
    elif order_direction == 'desc':
        pass

