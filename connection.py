import csv


def open_csv_file(file_path):
    with open(file_path, "r") as file:
        data_list = []
        reader = csv.DictReader(file)
        for dictionary in reader:
            data_list.append(dictionary)
    return data_list


def save_csv_file(data_list, file_path, header):
    with open(file_path, "w") as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        writer.writerows(data_list)


def open_id(file_path):
    with open(file_path, "r") as file:
        id = file.read()
        return id


def save_id(file_path, new_id):
    with open(file_path, "w") as file:
        file.write(new_id)