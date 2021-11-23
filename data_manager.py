import connection

QUESTIONS_FILE_PATH = 'data/questions.csv'
ANSWERS_FILE_PATH = 'data/answers.csv'
DATA_HEADER = ['id','submission_time','view_number','vote_number','title','message','image']

def read_csv_file():
    questions_list: list[dict[str]: str] = connection.open_file()