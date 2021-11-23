import csv

def open_file(file_path):
    with open(file_path, "r") as file:
        data_list = []
        csv_dict = csv.DictReader(file)
        for dictionary in csv_dict:
            data_list.append(dictionary)
    return data_list


def write_file(data_list, file_path, header):
    with open(file_path, "r") as file:
        csv_file = csv.DictWriter(file, fieldnames=header)
        csv.DictReader()
        for data in data_list:
            csv_file.writerow(data)


if __name__ == "__main__":
    answers = 'data/answers.csv'
    questions = 'data/questions.csv'
    questions = open_file(questions)
    answers = open_file(answers)


