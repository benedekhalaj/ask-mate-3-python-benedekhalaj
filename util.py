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


def vote(data_list, data_id, operator):
    data, index = get_data_and_index_by_id(data_list, 'id', data_id)
    data_list[index]['vote_number'] = modify_number(data, 'vote_number', operator)
    return data_list

