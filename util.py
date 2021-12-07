import datetime

from werkzeug.utils import secure_filename
import os
import datetime

UPLOAD_FOLDER = './static/images'


def get_data_by_id(data_list, value, id):
    for data in data_list:
        if data[value] == int(id):
            return data


def update_data_by_form(data, form):
    for key, value in form.items():
        data[key] = value
    return data


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
    return datetime.datetime.now().isoformat()
