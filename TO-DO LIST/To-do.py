import tkinter as tk

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x650+400+100")
root.resizable(False, False)
root.config(bg='#FFC0CB')

task_list = []

# Function to add a task
def addTask():
    task = task_entry.get()
    task_entry.delete(0, tk.END)

    if task:
        with open('tasklist.txt', 'a') as taskfile:
            taskfile.write(f'\n{task}')
        task_list.append(task)
        listbox.insert(tk.END, task)

# Function to delete a task
def deleteTask():
    global task_list
    task = str(listbox.get(tk.ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open('tasklist.txt', 'w') as taskfile:
            for task in task_list:
                taskfile.write(task + '\n')
        listbox.delete(tk.ANCHOR)

# Function to open and read tasks from file
def opentaskfile():
    try:
        global task_list
        with open('tasklist.txt', 'r') as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            if task != '\n':
                task_list.append(task.strip())
                listbox.insert(tk.END, task.strip())

    except FileNotFoundError:
        open('tasklist.txt', 'w')

# Top bar
top_image = tk.PhotoImage(file='bar1.png').subsample(2, 2)
tk.Label(root, image=top_image).pack()

# Title
tk.Label(root, text='To-Do List', font='Georgia 30 bold', fg='black', bg='#FFC0CB').place(x=130, y=20)

# Frame for task input
frame = tk.Frame(root, width=400, height=50, bg='#FF1493')
frame.place(x=0, y=180)

task_entry = tk.Entry(frame, width=18, font='arial 18', bd=0)
task_entry.place(x=10, y=7)
task_entry.focus()

add_button = tk.Button(frame, text="ADD", font='arial 20 bold', width=6, bg='#FF1493', fg='white', bd=0, command=addTask)
add_button.place(x=300, y=0)

# Frame for task list
frame1 = tk.Frame(root, bd=3, width=700, height=280, bg='#FF1493')
frame1.pack(pady=(100, 0))  

listbox = tk.Listbox(frame1, font=('arial ', 12), width=40, height=17, bg='white', fg='black', cursor='hand2', selectbackground='#FFC0CB')
listbox.pack(side=tk.LEFT, fill=tk.BOTH, padx=2)
scrollbar = tk.Scrollbar(frame1)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

opentaskfile()

# Delete button
delete_button = tk.Button(root, text="Delete Task", command=deleteTask, bg='#FF1493', fg='white', font='arial 20 bold', bd=2,width=15, height=1)
delete_button.pack(side=tk.BOTTOM, pady=10)

root.mainloop()
