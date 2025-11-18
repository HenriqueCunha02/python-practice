from pathlib import Path

archive = Path('todo_list.txt')#?

print(archive)

def add_task(task):

    with archive.open('a') as open: open.write(task + '\n')

def remove_task():
    ...

def replace_in_file(previus, new):

    modified_content = archive.read_text().replace(previus, new)
    archive.write_text(modified_content)

def read_task():
    print(archive.read_text())

def clear_file():
    archive.write_text('')

read_task()