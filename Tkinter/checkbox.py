from tkinter import *
from tkinter import messagebox


def selectoption():
    x1 = x.get()
    x2 = y.get()
    x3 = z.get()
    location = ""
    if x1 == 1:
        location = "Pune"
    if x2 == 1:
        location += "mumbai"
    if x3 == 1:
        location += "nagpur"

    messagebox.showinfo("location","you selected:"+location)


if __name__ == "__main__":
    window = Tk()
    x = IntVar()
    y = IntVar()
    z = IntVar()
    label1 = Label(window, text="select your loaction")
    check1 = Checkbutton(window, text="pune", variable=x)
    check2 = Checkbutton(window, text="mumbai", variable=y)
    check3 = Checkbutton(window, text="nagpur", variable=z)
    btnSelect = Button(window, text="select", command=selectoption)

    label1.grid(row=1, column=1)
    check1.grid(row=2, column=1)
    check2.grid(row=1, column=2)
    check3.grid(row=2, column=2)
    btnSelect.grid(row=3, column=1)
    window.mainloop()
