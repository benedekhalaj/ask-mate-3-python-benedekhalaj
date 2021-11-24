def get_data_by_id(data_list, value, id):
    for data in data_list:
        if data[value] == id:
            return data


def get_data_and_index_by_id(data_list, value, id):
    for index, data in enumerate(data_list):
        if data[value] == id:
            return data, index


def modify_number(data, value, operator):
    if operator == '+':
        return data[value] + 1
    else:
        return data[value] - 1


def update_data_by_form(data, form):
    for key, value in form.items():
        data[key] = value
    return data


def add_new_data(data, data_list):
    data_list.append(data)
    return data_list
