from tkinter import *
from backend_website import bot

def start():
	name = entry1.get()
	mail = entry2.get()
	num = entry3.get()
	bot(name, mail, num)

window = Tk()
window.geometry("450x200")
search1 = Label(window, text = "Name: ", font = "bold 12")
search1.place(x = 10, y = 10)
entry1 = Entry(window)
entry1.place(x = 250, y = 10)

search2 = Label(window, text = "Email: ", font = "bold 12")
search2.place(x = 10, y = 60)
entry2 = Entry(window)
entry2.place(x = 250, y = 60)

search3 = Label(window, text = "Contact Number: ", font = "arial 12")
search3.place(x = 10, y = 110)
entry3 = Entry(window)
entry3.place(x = 250, y = 110)

b1 = Button(window, text = "Start Botting!", command = start, width = 15, bg = 'gray')
b1.place(x = 170, y = 160)

window.mainloop()
