import sqlite3
import tkinter as tk
from tkinter import ttk


#This will create a new connection object named conn that you can use to execute SQL commands.
conn = sqlite3.connect('blood_management.db')


#A cursor is a database object that enables you to execute SQL commands and fetch the results.
c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS blood_management
    (id INTEGER PRIMARY KEY, name TEXT, blood_group TEXT, age INTEGER, contact_number integer)
''')

root = tk.Tk()
root.geometry("1920x1080")

def insert_row():
    name_value = name_entry.get() # .get() is used to retrieve data from user
    blood_group_value = blood_group_entry.get()
    age_value = age_entry.get()
    contact_number_value = contact_number_entry.get()

    c.execute("INSERT INTO blood_management (name, blood_group, age, contact_number) VALUES (?, ?, ?, ?)", (name_value, blood_group_value, age_value, contact_number_value))
    
    #its used to save the transactions/ entries
    conn.commit()

    name_entry.delete(0, tk.END)
    blood_group_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    contact_number_entry.delete(0, tk.END)

    display_table()

def display_table():
    table.delete(*table.get_children())
    c.execute("SELECT * FROM blood_management")
    data = c.fetchall()
    for item in data:
        table.insert("", "end",values=item)

def delete_row():
    item = table.item()["values"][0]
    print(item)

# root is used to create the main window 
name_label = tk.Label(root, text='Name:')
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

blood_group_label = tk.Label(root, text='Blood Group:')
blood_group_label.pack()
blood_group_entry = tk.Entry(root)
blood_group_entry.pack()

age_label = tk.Label(root, text='Age:')
age_label.pack()
age_entry = tk.Entry(root)
age_entry.pack()

contact_number_label = tk.Label(root, text='Contact Number:')
contact_number_label.pack()
contact_number_entry = tk.Entry(root)
contact_number_entry.pack()

insert_button = tk.Button(root, text='Insert Row', command=insert_row)
insert_button.pack()
delete_button = tk.Button(root,text="delete Row" ,command=delete_row)
delete_button.pack()
tree_frame = tk.Frame(root) 
 # treeview used to make hirearical order
table = ttk.Treeview(tree_frame,columns= ("id","name","blood_group","age","contact_no"),show="headings")
table.heading("id", text="ID")
table.heading("name", text="Name")
table.heading("blood_group", text="Blood Group")
table.heading("age", text="Age")
table.heading("contact_no", text="Contact number")
table.column("id",width=80)
table.column("name",width=100)
table.column("blood_group",width=80)
table.column("age",width=80)
table.column("contact_no",width=80)

table.pack()

tree_frame.pack()

display_table()
conn.commit()

root.mainloop()
conn.close()