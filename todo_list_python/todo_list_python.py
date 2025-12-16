from pathlib import Path
from tkinter import *

archive = Path("todo_list.txt")

current_action = None


def clear_placeholder(event):
    if entry.get() == "Write the task and press Execute":
        entry.delete(0, END)


def show_entry(placeholder=""):
    entry.pack(side=LEFT, padx=5)
    btn_execute.pack(side=LEFT, padx=5)

    entry.delete(0, END)
    entry.insert(0, placeholder)
    entry.bind("<Key>", clear_placeholder)
    entry.focus()


def hide_entry():
    entry.pack_forget()
    btn_execute.pack_forget()
    entry.delete(0, END)


def add_task(task):
    with archive.open("a") as open:
        open.write(task + "\n")


def option_add_task():
    global current_action
    current_action = "add"
    show_entry("Write the task and press Execute")


def remove_task():
    selected = tasks_box.curselection()

    if not selected:
        warning_label.pack(side="top", padx=10)
        return

    warning_label.pack_forget()

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

    value = entry.get().strip()

    if current_action == "add":
        if value:
            add_task(value)
        hide_entry()
        return

    elif current_action == "replace":
        pass

    hide_entry()
    current_action = None


window = Tk()
window.title("To Do List")
window.configure(bg="#ffffff")
window.geometry("700x500")
window.resizable(False, False)


header_frame = Frame(window, bg="#c0c0c0")
header_frame.pack(pady=10, fill=X)

buttons_frame = Frame(window, bg="#ffffff")
buttons_frame.pack(pady=10)

entry_frame = Frame(window, bg="#ffffff")
entry_frame.pack(pady=10)

warning_label_frame = Frame(window, bg="#ffffff")
warning_label_frame.pack()

list_frame = Frame(window, bg="#ffffff")
list_frame.pack(pady=10)

button_quit_frame = Frame(window, bg="#ffffff")
button_quit_frame.pack(pady=10)

introduction = Label(
    header_frame,
    text="Select the operation that you want:",
    font=("Segoe UI", 16, "bold"),
    bg="#c0c0c0",
).pack()

btn_read = Button(
    buttons_frame,
    text="Read Tasks",
    width=12,
    bg="#4287f5",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    activebackground="#02245c",
    activeforeground="white",
    command=read_task,
).pack(side=LEFT, padx=5)

btn_add = Button(
    buttons_frame,
    text="Add Task",
    width=12,
    bg="#4CAF50",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    activebackground="#004003",
    activeforeground="white",
    command=option_add_task,
).pack(side=LEFT, padx=5)

btn_remove = Button(
    buttons_frame,
    text="Remove Task",
    width=12,
    bg="#c72626",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    activebackground="#400000",
    activeforeground="white",
    command=remove_task,
).pack(side=LEFT, padx=5)

btn_clear = Button(
    buttons_frame,
    text="Clear Tasks",
    width=12,
    bg="#d18724",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    activebackground="#784705",
    activeforeground="white",
    command=clear_file,
).pack(side=LEFT, padx=5)

entry = Entry(
    entry_frame,
    width=37,
    bg="#c0c0c0",
    relief="flat",
    font=("bold"),
)


btn_execute = Button(
    entry_frame,
    text="Execute",
    width=12,
    bg="#c07cd1",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    activebackground="#004912",
    activeforeground="white",
    command=execute_option,
)

warning_label = Label(
    warning_label_frame,
    text="SELECT A TASK BEFORE REMOVE IT",
    fg="red",
    bg="#ffffff",
    font=("Segoe UI", 14, "bold"),
)

tasks_box = Listbox(
    list_frame,
    width=80,
    height=10,
    selectbackground="#444444",
    font=("Consolas", 12, "bold"),
    bg="#c0c0c0",
)
tasks_box.pack(side=LEFT)


btn_quit = Button(
    button_quit_frame,
    text="Quit",
    width=12,
    bg="#c70b0b",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    activebackground="#5C0000",
    activeforeground="white",
    command=window.destroy,
).pack(side=LEFT, padx=5)

window.mainloop()
