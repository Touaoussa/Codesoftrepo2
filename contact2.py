import tkinter as tk
import json
root = tk.Tk()
root.title("Contact Book")
contacts= []


#create Frame 1 to display contacts info
frame1 = tk.Frame(root)
frame1.pack(side=tk.RIGHT,pady=10)

#create Frame 2 for add inputs
frame2 = tk.Frame(root)
frame2.pack(side=tk.LEFT,pady=10)

# create Frame 3 for update and delete button
frame3 = tk.Frame(frame1)
frame3.pack(pady=10)


#firstname input
firstnamelabel = tk.Label(frame2, text="Firstname:")
firstnamelabel.pack()
firstname=tk.Entry(frame2,width=25)
firstname.pack(pady=4)

#lastnameinput
lastnamelabel = tk.Label(frame2, text="Lastname:")
lastnamelabel.pack()
lastname=tk.Entry(frame2,width=25)
lastname.pack(pady=4)

#numberinput
numberlabel = tk.Label(frame2, text="Number:")
numberlabel.pack()
number=tk.Entry(frame2,width=25)
number.pack(pady=4)

#adressinput
adresselabel = tk.Label(frame2, text="Adresse:")
adresselabel.pack()
adress=tk.Entry(frame2,width=25)
adress.pack(pady=4)


def search(event=None):
	query=searchentry.get()
	listbox.delete(0,tk.END)
	for contact in contacts:
		firstname=contact["Firstname"]
		lastname=contact["Lasttname"]
		if query in firstname :
			listbox.insert(tk.END,contact["Firstname"]+ " "+contact["Lasttname"])
		elif query in lastname :
			listbox.insert(tk.END,contact["Firstname"]+ " "+contact["Lasttname"])
		
					
# Searchbar
searchlabel = tk.Label(frame1, text="Search:")
searchlabel.pack()
searchentry = tk.Entry(frame1)
searchentry.bind("<KeyRelease>", search)
searchentry.pack(pady=4)
 
# Create a listbox to display contacts
listbox = tk.Listbox(frame1, selectmode=tk.SINGLE, width=40, height=10)
listbox.pack(pady=4)






def AddContact():
	if lastname and number:
	    fname = firstname.get()
	    lname= lastname.get()
	    nb=number.get()
	    ads=adress.get()
	    firstname.delete(0, tk.END)
	    lastname.delete(0, tk.END)
	    number.delete(0, tk.END)
	    adress.delete(0, tk.END)
	    contact = {"Firstname": fname, "Lasttname": lname,"Phone": nb, "Adress": ads}
	    contacts.append(contact)
	    fullname = fname+ " "+ lname
	    listbox.insert(tk.END,fullname  )
	    with open("contacts.json", "w") as file:
	    	json.dump(contacts, file, indent=2)

#Button add
buttonadd = tk.Button(frame2,text="Add Contact",width=14,command=AddContact)
buttonadd.pack(pady=4)



def displaycontact():
	selected_index = listbox.curselection()
	if selected_index:
        	index = selected_index[0]
        	contact = contacts[index]
        	# Display selected contact in entry widgets
        	
        	# Create a pop-up window to display detailed contact information
        	popup = tk.Toplevel(root)
        	popup.title("Contact Details")	
        	detail_label = tk.Label(popup, text=f"FirstName: {contact['Firstname']} \n LastName: {contact['Lasttname']} \nPhone: {contact['Phone']}\nAdress : {contact['Adress']}")
        	detail_label.pack(padx=10, pady=10)

#button display
buttondisplay= tk.Button(frame1,text="Display Contact",width=10,command=displaycontact)
buttondisplay.pack(pady=4)

def updatecontact():
	popup = tk.Toplevel(root)
	popup.title("Update Contact")	
	selected_index = listbox.curselection()
	if selected_index:
        	index = selected_index[0]
        	contact = contacts[index]
        	#firstname input
        	firstname2=tk.Entry(popup,width=25)
        	firstname2.pack(pady=4)
        	
        	lastname2=tk.Entry(popup,width=25)
        	lastname2.pack(pady=4)
        	
        	number2=tk.Entry(popup,width=25)
        	number2.pack(pady=4)
        	
        	adress2=tk.Entry(popup,width=25)
        	adress2.pack(pady=4)
        	
        	firstname2.insert(0, contact["Firstname"])
        	lastname2.insert(0, contact["Lasttname"])
        	number2.insert(0, contact["Phone"])
        	adress2.insert(0, contact["Adress"])
        	
        	def savecontact(): 
        		 fname = firstname2.get()
        		 lname= lastname2.get()
        		 nb=number2.get()
        		 ads=adress2.get()
        		 contactupdated = {"Firstname": fname, "Lasttname": lname,"Phone": nb, "Adress": ads}
        		 contacts[index]=contactupdated
        		 listbox.delete(index)
        		 listbox.insert(index,fname + " "+lname)
        	
        	buttonsave = tk.Button(popup,text="Save",width=10,command=savecontact)
        	buttonsave.pack(pady=4)

#Button update
buttonupdate = tk.Button(frame1,text="Update Contact",width=10,command=updatecontact)
buttonupdate.pack(pady=4)			
	

def deletecontact():
	selected_index = listbox.curselection()
	if selected_index:
        	index = selected_index[0]
        	contacts.pop(index)
        	listbox.delete(index)
        	with open("contacts.json", "w") as file:
        		json.dump(contacts, file, indent=2)

#Button delete
buttondelete= tk.Button(frame1,text="Delete Contact",width=10,command=deletecontact)
buttondelete.pack(pady=4)	


def main():
	root.mainloop()

main()
