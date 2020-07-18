import tkinter as tk
import tkinter.ttk as ttk
from backend import Database

database=Database("db1.db")
window=tk.Tk()
window.title("Asset Manager")
window.geometry("850x520")
menu=tk.Menu(window)

menu.add_command(label="Addition",command=lambda:addition_frame())
menu.add_command(label="Search",command=lambda:switch_frame(search_frame))
menu.add_command(label="Records",command=lambda:switch_frame(records_frame))
menu.add_command(label="Order",command=lambda:switch_frame(order_frame))
window.configure(menu=menu)



def switch_frame(frame):
	new_frame=frame()
	if frame is not None:
		frame=tk.Frame.destroy()
	new_frame=frame()
	new_frame.pack()


def addition_frame():
	options=("COMPUTERS","FURNITURES","SERVERS","OFFICE_EQUIPMENTS")
	description=tk.StringVar()
	tag_number=tk.StringVar()
	serial_number=tk.StringVar()
	category=tk.StringVar()
	location=tk.StringVar()
	cost=tk.DoubleVar()

	ld=tk.Label(text="DESCRIPTION:")
	ld.grid(row=0,column=0)
	ltag=tk.Label(text="TAG NUMBER:")
	ltag.grid(row=1,column=0)
	lserial=tk.Label(text="SERIAL NUMBER:")
	lserial.grid(row=2,column=0)
	lcat=tk.Label(text="CATEGORY:")
	lcat.grid(row=3,column=0)
	llocation=tk.Label(text="LOCATION:")
	llocation.grid(row=4,column=0)
	lcost=tk.Label(text="COST:")
	lcost.grid(row=5,column=0)

	description=tk.Entry(textvar=description,width=80)
	description.grid(row=0,column=1)
	tag_number=tk.Entry(textvar=tag_number,width=80)
	tag_number.grid(row=1,column=1)
	serial_number=tk.Entry(textvar=serial_number,width=80)
	serial_number.grid(row=2,column=1)
	category=tk.Entry(textvar=category,width=80)
	category.grid(row=3,column=1)
	location=tk.Entry(textvar=location,width=80)
	location.grid(row=4,column=1)
	cost=tk.Entry(textvar=cost,width=80)
	cost.grid(row=5,column=1)


	def insert_data():
		database.insert(description.get(),tag_number.get(),serial_number.get(),category.get(),location.get(),cost.get())

	submit_b=tk.Button(text="SUBMIT",width=10,command=insert_data)
	submit_b.grid(row=12,column=1)



def search_frame():
	query=tk.StringVar()

	query=tk.Label(text="SEARCH HERE:")
	query.grid(row=0,column=1)

	query=tk.Entry(textvar=query,width=80)
	query.grid(row=0,column=2)

	search_button=tk.Button(text="SEARCH",width=10,command=database.search())
	search_button.grid(row=0,column=4)


def order_frame():
	print("No record Yet")

def records_frame():
	records=database.view()
	for data in records:
		print(data)
		l1=tk.Label(text=data)
		l1.grid()

window.mainloop()
