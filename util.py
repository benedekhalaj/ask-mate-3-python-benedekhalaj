import datetime

from werkzeug.utils import secure_filename
import os
import datetime

UPLOAD_FOLDER = './static/images'


def get_data_by_id(data_list, value, id):
    for data in data_list:
        if data[value] == int(id):
            return data


def get_data_and_index_by_id(data_list, value, id):
    for index, data in enumerate(data_list):
        if data[value] == int(id):
            return data, index


def get_data_list(data_list, value, id):
    return [data for data in data_list if data[value] == int(id)]


def modify_number(data, value, operator):
    if operator == '+':
        new_value = int(data[value]) + 1
        return str(new_value)
    else:
        new_value = int(data[value]) - 1
        return str(new_value)


def update_data_by_form(data, form):
    for key, value in form.items():
        data[key] = value
    return data


def add_new_data(data, data_list):
    data_list.append(data)
    return data_list


def delete_data(data_list, data_id, value='id'):
    for data in data_list:
        if data_id == data[value]:
            data_list.remove(data)
            if data['image']:
                delete_file('answers', data['id'])

    return data_list


def change_vote_number(data_list, data_id, operator):
    data, index = get_data_and_index_by_id(data_list, 'id', data_id)
    data_list[index]['vote_number'] = modify_number(data, 'vote_number', operator)
    return data_list


def upload_file(request_attributes, r_type='questions'):
    file = request_attributes.files['file']
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(f"{UPLOAD_FOLDER}/{r_type}", filename))
        source = f"{UPLOAD_FOLDER}/{r_type}/{filename}"
        return source if r_type == 'questions' else f"../{source}"
    return ''


def delete_file(r_type, id):
    directory_in_str = f'{UPLOAD_FOLDER}/{r_type}'
    directory = os.fsencode(directory_in_str)

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(f"_{id}.png") or filename.endswith(f"_{id}.jpg"):
            os.remove(os.path.join(f"{directory_in_str}/{filename}"))


def add_submission_time():
    return str(datetime.datetime.now().isoformat())
