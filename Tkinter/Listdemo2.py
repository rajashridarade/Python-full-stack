from tkinter import *


def addToList1():
    list1.insert(END, list2.get(ACTIVE))
    list2.delete(ACTIVE)


def addToList2():
    list2.insert(END, list1.get(ACTIVE))
    list1.delete(ACTIVE)


if __name__ == "__main__":
    window = Tk()
    list1 = Listbox(window)
    list1.insert(END, "Apple")
    list1.insert(END, "grapes")
    list1.insert(END, "orange")
    list1.insert(END, "watermelon")
    list1.pack(side=LEFT)
    window.geometry("300x200")

    frame = Frame(window)
    btnAdd1 = Button(frame, text="---->>----", command=addToList2)
    btnAdd2 = Button(frame, text="----<<----", command=addToList1)
    frame.pack(side=LEFT)
    btnAdd1.pack()
    btnAdd2.pack()

    list2 = Listbox(window)
    list2.insert(END, "onion")
    list2.insert(END, "potato")
    list2.insert(END, "Tamato")
    list2.insert(END, "garlic")
    list2.pack(side=LEFT)
    window.geometry("300x200")
    window.mainloop()
