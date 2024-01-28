import tkinter as tk
from tkinter import *
from tkinter import messagebox
root = tk.Tk()
root.title("To do List")

entry = tk.Entry(root,width=60)
entry.pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=14)

# Create a listbox to display tasks
listbox = tk.Listbox(frame, selectmode=tk.SINGLE, width=40, height=10)
listbox.pack(side=tk.LEFT, pady=4)



def add_task():
    newtask = entry.get()
    if newtask:
    	listbox.insert(tk.END,newtask)
    	clear_input()
    else:
        messagebox.showwarning("Warning.","Please enter a task.")
         
def clear_input():
    entry.delete(0, tk.END)
    
    
def delete_task():
      try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
      except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")    

def update_task():
	try:
	 index= listbox.curselection()[0]
	 new_task = entry.get()
	 if new_task:
	  listbox.delete(index)
	  listbox.insert(index,new_task)
	  clear_input()
	 else:
	  messagebox.showwarning("Warning.","Please enter a task.")
	except IndexError:
         messagebox.showwarning("Warning", "Please select a task to Update.")


def main():
	# Create a label
	label = tk.Label(root, text="Enter new task:")
	label.pack(pady=10)


	# Create a button to get the input
	button = tk.Button(root, text="Add Task", command=add_task)
	button.pack(pady=10)
	
	# Create a button to delete tasks
	button_delete = tk.Button(root, text="Delete Task", command=delete_task)
	button_delete.pack(pady=5)
	
	# Create a button to update tasks
	button_update = tk.Button(root, text="Update Task", command=update_task)
	button_update.pack(pady=5)
	
	root.mainloop()
	
	
	
if __name__ == "__main__":
    main()
