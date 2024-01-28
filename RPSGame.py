import tkinter as tk
from tkinter import messagebox
import random


root = tk.Tk()
root.title("RPSGame")
listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=20, height=10)
listbox.pack( pady=4)
counteruser=0
countercomputer=0


def main():
	listbox.insert(tk.END,"Rock")
	listbox.insert(tk.END,"Paper")
	listbox.insert(tk.END,"Scissors")
	root.mainloop()

def play():
	global	counteruser,countercomputer
	index=listbox.curselection()
	
	if index:
		popup = tk.Toplevel(root)
		popup.title("Result Game")
		
		
		
		choiceuser=listbox.get(index)
		choicecomputer=random.choice(["Rock","Paper","Scissors"])
		print(choicecomputer)
		if choiceuser == choicecomputer:
			resultlabel = tk.Label(popup, text=f"draw up  \n you : {counteruser} \n computer : {countercomputer}")
			resultlabel.pack(padx=20, pady=40)
		elif (choiceuser == 'Rock' and choicecomputer == 'Scissors') or \
		(choiceuser == 'Paper' and choicecomputer == 'Rock') or \
		(choiceuser == 'Scissors' and choicecomputer == 'Paper'):
			counteruser+=1
			resultlabel2 = tk.Label(popup, text=f"congratulations you win \n you : {counteruser} \n computer : {countercomputer}")
			resultlabel2.pack(padx=20, pady=40)
			print (counteruser)
		else:
			countercomputer+=1
			resultlabel3 = tk.Label(popup, text=f"You lose try again \n you : {counteruser} \n computer : {countercomputer}")
			resultlabel3.pack(padx=20, pady=40)
		def playagain():
			popup.destroy()
		buttonplayagain = tk.Button(popup, text="play again ", command=playagain)
		buttonplayagain.pack(pady=5)
		
		
		
			
	else:
	  messagebox.showwarning("you have to pick a choice.")	


buttonplay = tk.Button(root, text="Let's play ", command=play)
buttonplay.pack(pady=5)
	


main()
