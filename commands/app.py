def get_data(list_name):
    data = []
    with open(list_name, 'r') as todo_list:
        data = todo_list.read().split('\n')  
    return data

def add(args):
    data = get_data('todo.txt')
    title = args[0]
    data.append({
        'title' : title,
        'created_at': 'current_time'
    })
    # add this todo item
    with open('todo.txt', 'r+') as todo_list:
        data = todo_list.read().split('\n')
        print(data)


def ls(args):
    data = get_data('todo.txt')
    if (len(data) == 0):
        print('todo item does not exist')
        return
    for index, todo_item in enumerate(data):
        print(index+1, todo_item['title'])