import tkinter
import backdb


def view_fn():
	list1.delete(0,END)
	for rows in backdb.view():
		list1.insert(END,rows)

def search_fn():
	list1.delete(0,END)
	for rows in backdb.search(author_text.get(),year_text.get(),title_text.get(),isbn_text.get()):
		list1.insert(END,rows)
	

def insert_fn():
	backdb.insert(author_text.get(),year_text.get(),title_text.get(),isbn_text.get())
	list1.delete(0,END)
	list1.insert(END,(author_text.get(),year_text.get(),title_text.get(),isbn_text.get()))



#def update_fn():

#def delete_fn():


#def close_fn():

window = tkinter.Tk()
window.wm_title("book db")

#top entry
l1=tkinter.Label(window,text='Title')
l1.grid(row=0,column=0)
title_text=tkinter.StringVar()
t1=tkinter.Entry(window,textvariable=title_text)
t1.grid(row=0,column=1)


l2=tkinter.Label(window,text='Author')
l2.grid(row=0,column=2)
author_text=tkinter.StringVar()
a1=tkinter.Entry(window,textvariable=author_text)
a1.grid(row=0,column=3)

l3=tkinter.Label(window,text='Year')
l3.grid(row=1,column=0)
year_text=tkinter.StringVar()
y1=tkinter.Entry(window,textvariable=year_text)
y1.grid(row=1,column=1)


l4=tkinter.Label(window,text='ISBN')
l4.grid(row=1,column=2)
isbn_text=tkinter.StringVar()
i1=tkinter.Entry(window,textvariable=isbn_text)
i1.grid(row=1,column=3)

#buttons
b6=tkinter.Button(window,text='View all',width=12,command=view_fn)
b6.grid(row=2,column=3)

b1=tkinter.Button(window,text='Search Entry',width=12,command=search_fn)
b1.grid(row=3,column=3)

b2=tkinter.Button(window,text='Add Entry',width=12,command=insert_fn)
b2.grid(row=4,column=3)

b3=tkinter.Button(window,text='Update',width=12)
b3.grid(row=5,column=3)

b4=tkinter.Button(window,text='Delete',width=12)
b4.grid(row=6,column=3)

b5=tkinter.Button(window,text='Close',width=12,command=window.destroy)
b5.grid(row=7,column=3)


#listbox
list1=tkinter.Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1 = tkinter.Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

window.mainloop()



