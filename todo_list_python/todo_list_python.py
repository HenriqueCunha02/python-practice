from pathlib import Path
from tkinter import *

archive = Path("todo_list.txt")

current_action = None


def clear_placeholder(event):
    if entry.get() == "Write the task and press Execute":
        entry.delete(0, END)


def add_task(task):
    with archive.open("a") as open:
        open.write(task + "\n")


def option_add_task():
    global current_action
    current_action = "add"
    entry.delete(0, END)
    entry.insert(0, "Write the task and press Execute")


def remove_task():
    selected = tasks_box.curselection()

    if not selected:
        not_selected_label = Label(
            list_frame, text="<-- Select a Task ", fg="red", font=("Arial", 14, "bold")
        ).pack(side=RIGHT, padx=10)
        return

    index = selected[0]
    task = tasks_box.get(index)

    lines = archive.read_text().splitlines()
    filtered = [line for line in lines if line.strip() != task]
    archive.write_text("\n".join(filtered))

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
    archive.write_text("")


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
window.title("To Do List")

header_frame = Frame(window)
header_frame.pack(pady=10)

buttons_frame = Frame(window)
buttons_frame.pack(pady=10)

entry_frame = Frame(window)
entry_frame.pack(pady=10)

list_frame = Frame(window)
list_frame.pack(pady=10)

button_quit_frame = Frame(window)
button_quit_frame.pack(pady=10)

introduction = Label(
    header_frame, text="Select the operation that you want:", font=("Arial", 16, "bold")
).pack()

task_list = Label(
    header_frame, text=("\n" "4 - Replace some Task\n" "6 - Quit\n")
).pack()

btn_read = Button(
    buttons_frame,
    text="Read Tasks",
    width=12,
    bg="#4287f5",
    fg="white",
    font=("Arial", 10, "bold"),
    activebackground="#02245c",
    activeforeground="white",
    command=read_task,
).pack(side=LEFT, padx=5)

btn_read = Button(
    buttons_frame,
    text="Add Task",
    width=12,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 10, "bold"),
    activebackground="#004003",
    activeforeground="white",
    command=option_add_task,
).pack(side=LEFT, padx=5)

btn_read = Button(
    buttons_frame,
    text="Remove Task",
    width=12,
    bg="#c72626",
    fg="white",
    font=("Arial", 10, "bold"),
    activebackground="#400000",
    activeforeground="white",
    command=remove_task,
).pack(side=LEFT, padx=5)

btn_read = Button(
    buttons_frame,
    text="Clear Tasks",
    width=12,
    bg="#d18724",
    fg="white",
    font=("Arial", 10, "bold"),
    activebackground="#784705",
    activeforeground="white",
    command=clear_file,
).pack(side=LEFT, padx=5)

entry = Entry(entry_frame, width=56)
entry.pack(side=LEFT, padx=5)
entry.bind("<Button-1>", clear_placeholder)

btn_execute = Button(
    entry_frame,
    text="Execute",
    width=12,
    bg="#c07cd1",
    fg="white",
    font=("Arial", 10, "bold"),
    activebackground="#004912",
    activeforeground="white",
    command=execute_option,
).pack(side=LEFT, padx=5)

tasks_box = Listbox(list_frame, width=80, height=10)
tasks_box.pack(side=LEFT)

btn_execute = Button(
    button_quit_frame,
    text="Quit",
    width=12,
    bg="#c70b0b",
    fg="white",
    font=("Arial", 10, "bold"),
    activebackground="#5C0000",
    activeforeground="white",
    command=window.destroy,
).pack(side=LEFT, padx=5)

window.mainloop()
