from pathlib import Path
from tkinter import *

archive = Path('todo_list.txt')

current_action = None

def clear_placeholder(event):
    if entry.get() == "Write the task and press Execute":
        entry.delete(0, END)

def add_task(task):
    with archive.open('a') as open: open.write(task + '\n')

def option_add_task():
    global current_action
    current_action = "add"
    entry.delete(0, END)
    entry.insert(0, "Write the task and press Execute")

def remove_task():
    selected = tasks_box.curselection()

    if not selected:
        return

    index = selected[0]
    task = tasks_box.get(index)

    lines = archive.read_text().splitlines()
    filtered = [line for line in lines if line.strip() != task]
    archive.write_text('\n'.join(filtered))

    tasks_box.delete(index)

def replace_in_file(previus, new):

    modified_content = archive.read_text().replace(previus, new)
    archive.write_text(modified_content)

def read_task():
    tasks_box.delete(0, END)

    if not archive.exists():
        return

    tasks = archive.read_text().splitlines()

    for task in tasks:
        tasks_box.insert(END, task)

def clear_file():
    archive.write_text('')

def execute_option():
    global current_action

    value = entry.get()

    if current_action == "add":
        add_task(value)
        current_action = None
        entry.delete(0, END)
        return
    
    if not value.isdigit():
        print("Please enter a valid option number")
        entry.delete(0, END)
        return

    option = int(value)

    match option:
        case 3:
            remove_task(entry.get())
        case 5:
            clear_file()

window = Tk()
window.title('To Do List')

introduction = Label(window, text = 'Select the operation that you want:').grid(column = 1, row = 0)

task_list = Label(window, text = ('\n' \
'3 - Remove Task\n'
'4 - Replace some Task\n'
'6 - Quit\n'))
task_list.grid(column = 1, row = 1)

btn_read = Button(window, text="Read Tasks", command=read_task)
btn_read.grid(column=1, row=2)

btn_read = Button(window, text="Add Tasks", command=option_add_task)
btn_read.grid(column=2, row=2)

btn_read = Button(window, text="Remove Task", command=remove_task)
btn_read.grid(column=4, row=2)

btn_read = Button(window, text="Clear Tasks", command=clear_file)
btn_read.grid(column=0, row=2)

entry = Entry(window, width = 100)
entry.grid(column = 1, row = 3)
entry.bind("<Button-1>", clear_placeholder)

btn_execute = Button(window, text='Execute', command=execute_option)
btn_execute.grid(column=1, row=4)

tasks_box = Listbox(window, width=80, height=10)
tasks_box.grid(column=1, row=6)

window.mainloop()