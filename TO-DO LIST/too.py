import tkinter as tk
from tkinter import messagebox
import sqlite3

# Database setup
def initialize_db():
    conn = sqlite3.connect('todo_list.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

initialize_db()

# To-Do List 
class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.config(bg='#1E90FF')  
        self.root.geometry('400x400')
        self.root.resizable(False, False)

        # Title -
        self.title_label = tk.Label(root, text="To-Do List", bg='#1E90FF', fg='white', font=('Helvetica', 18, 'bold'))
        self.title_label.pack(pady=10)

        # Entry and Buttons -
        self.task_entry = tk.Entry(root, width=40, bg='white', fg='#1E90FF', font=('Helvetica', 12), relief='solid', bd=1)
        self.task_entry.pack(pady=10, padx=20)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, bg='white', fg='#1E90FF', font=('Helvetica', 12, 'bold'), relief='raised', bd=2)
        self.add_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task, bg='white', fg='#1E90FF', font=('Helvetica', 12, 'bold'), relief='raised', bd=2)
        self.delete_button.pack(pady=5)

        self.tasks_listbox = tk.Listbox(root, width=40, height=10, bg='white', fg='#1E90FF', font=('Helvetica', 12), relief='solid', bd=1, selectbackground='#87CEFA')
        self.tasks_listbox.pack(pady=10, padx=20)

        # Functions - 
        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            conn = sqlite3.connect('todo_list.db')
            cursor = conn.cursor()
            cursor.execute('INSERT INTO tasks (task) VALUES (?)', (task,))
            conn.commit()
            conn.close()
            self.task_entry.delete(0, tk.END)
            self.load_tasks()
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def load_tasks(self):
        self.tasks_listbox.delete(0, tk.END)
        conn = sqlite3.connect('todo_list.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tasks')
        tasks = cursor.fetchall()
        for task in tasks:
            self.tasks_listbox.insert(tk.END, task[1])
        conn.close()

    def delete_task(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            task_text = self.tasks_listbox.get(selected_task_index)
            conn = sqlite3.connect('todo_list.db')
            cursor = conn.cursor()
            cursor.execute('DELETE FROM tasks WHERE task = ?', (task_text,))
            conn.commit()
            conn.close()
            self.load_tasks()
        else:
            messagebox.showwarning("Warning", "You must select a task to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
