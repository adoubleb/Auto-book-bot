from tkinter import *
from backend_website import bot

def start():
	name = entry1.get()
	mail = entry2.get()
	num = entry3.get()
	bot(name, mail, num)

window = Tk()
window.title("Experimental Bot V1")
window.iconbitmap('time.ico')
window.geometry("500x250")
search1 = Label(window, text = "Name: ", font = "times 15")
search1.place(x = 10, y = 10)
entry1 = Entry(window, width = 50, borderwidth = 5)
entry1.place(x = 150, y = 10)

search2 = Label(window, text = "Email: ", font = "times 15")
search2.place(x = 10, y = 60)
entry2 = Entry(window, width = 50, borderwidth = 5)
entry2.place(x = 150, y = 60)

search3 = Label(window, text = "Contact Number: ", font = "times 13")
search3.place(x = 10, y = 110)
entry3 = Entry(window, width = 50, borderwidth = 5)
entry3.place(x = 150, y = 110)

b1 = Button(window, text = "Start Botting!", command = start, width = 15, bg = 'gray')
b1.place(x = 200, y = 180)

window.mainloop()
