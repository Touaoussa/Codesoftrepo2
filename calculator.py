import tkinter as tk

def build_calculator():
	root = tk.Tk()
	root.title("Calculator")
	
	#create an input
	entry = tk.Entry(root, width=16, font=('Arial', 16), justify="right")
	entry.grid(row=0, column=0, columnspan=4)
]
	#create numbers from 1 to 9
	rownum = 1
	colnum = 0
	for i in range(1,10):
		tk.Button(root,text=i,padx=30, pady=30, font=('Arial', 14),command= lambda var=i : calculate(var,entry)).grid(row=rownum, column=colnum)
		colnum += 1
		if colnum > 2:
		 colnum = 0
		 rownum += 1
	
	#create artmitic operators
	operators={"+","-","*","/"}
	colnum=4
	rownum=1
	for j in operators:
		tk.Button(root,text=j,padx=30, pady=30, font=('Arial', 14),command= lambda var=j : calculate(var,entry)).grid(row=rownum, column=colnum)
		rownum+=1
	
	#add the last line
	last_line={"0","C",".","="}
	colnum=0
	rownum=4
	for k in last_line:
		if k == "=" :
			tk.Button(root,text=k,width=20, font=('Arial', 14),command= lambda var=k  : calculate(var,entry)).grid(row=5, column=0, columnspan=4)
		else :	
			tk.Button(root,text=k,padx=30, pady=30, font=('Arial', 14),command= lambda var=k  : calculate(var,entry)).grid(row=rownum, column=colnum)
			colnum+=1
	root.mainloop()


def calculate(val,entr) :
	try:
		expr = entr.get()
		if val == '=':
			result = eval(expr)
			entr.delete(0, tk.END)
			entr.insert(tk.END, str(result))
		elif val == 'C':
			entr.delete(0, tk.END)
		else:
			entr.delete(0, tk.END)
			entr.insert(tk.END, expr + str(val))
	except Exception as e:
        	entr.delete(0, tk.END)
        	entr.insert(tk.END, "Error")
			
	
def main():
	build_calculator()

if __name__ == "__main__":
    main()
