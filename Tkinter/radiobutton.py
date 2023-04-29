from tkinter import *
from tkinter import messagebox


def selectoption():
    x1 = X.get()
    location = ""

    if x1 == 1:
        location = "Pune"
    elif x1 == 2:
        location = "mumbai"
    elif x1 == 3:
        location = "nagpur"
    else:
        location = "not selected"
    messagebox.showinfo("location","you selected:"+location)


if __name__ == "__main__":
    window = Tk()
    X = IntVar()
    label1 = Label(window, text="select your loaction")
    radio1 = Radiobutton(window, text="pune", variable=X, value=1)
    radio2 = Radiobutton(window, text="mumbai", variable=X, value=2)
    radio3 = Radiobutton(window, text="nagpur", variable=X, value=3)
    btnSelect = Button(window, text="select", command=selectoption)

    label1.grid(row=1, column=1)
    radio1.grid(row=2, column=1)
    radio2.grid(row=1, column=2)
    radio3.grid(row=2, column=2)
    btnSelect.grid(row=3, column=1)
    window.mainloop()
