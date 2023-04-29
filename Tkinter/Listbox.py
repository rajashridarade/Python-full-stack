from  tkinter import *

def addToList():
    list.insert(END,txtEntry.get())
    txtEntry.delete(0,END)
    txtEntry.focus()

if __name__ == "__main__":
    window = Tk()

    list = Listbox(window)
    list.pack()
    txtEntry = Entry(window)
    txtEntry.pack()
    btnAdd = Button(window,text="Add to list",command=addToList)
    btnAdd.pack()
    window.geometry("200x300")
    window.mainloop()
