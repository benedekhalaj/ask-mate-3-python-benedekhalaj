import connection

QUESTIONS_FILE_PATH = 'data/questions.csv'
ANSWERS_FILE_PATH = 'data/answers.csv'
DATA_HEADER = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']


def get_questions():
    return connection.open_file(QUESTIONS_FILE_PATH)
