from pathlib import Path

archive = Path('todo_list.txt')

def add_task(task):

    with archive.open('a') as open: open.write(task + '\n')

def remove_task(task):

    lines = archive.read_text().splitlines()
    filtered = [line for line in lines if line.strip() != task]
    archive.write_text('\n'.join(filtered))

def replace_in_file(previus, new):

    modified_content = archive.read_text().replace(previus, new)
    archive.write_text(modified_content)

def read_task():
    print(archive.read_text())

def clear_file():
    archive.write_text('')

option = int(input('Select the operation that you want:\n' \
'1 - Read Tasks\n'
'2 - Add Task\n'
'3 - Remove Task\n'
'4 - Replace some Task\n'
'5 - Clear All the Tasks\n'))

match option:
    case 1:
        read_task()
    case 2:
        task_to_add = input('Write the task that you want to add: ')
        add_task(task_to_add)
    case 3:
        print('\nTasks that you have: ')
        read_task()
        task_to_remove = input('Write the task that you wants to remove: ')
        remove_task(task_to_remove)
    case 4:
        print('\nTasks that you have: ')
        read_task()
        previus = input('Write the task that you want to replace: ')
        new = input('Write the task that you want to add: ')

        replace_in_file(previus, new)

    case 5:
        clear_file()