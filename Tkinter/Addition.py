from tkinter import *
from tkinter import messagebox


def displaySum():
    try:
        num1 = int(txtNum1.get())
        num2 = int(txtNum2.get())
        s = num1 + num2
        messagebox.showinfo("Title:sum", "sum=" + str(s))
    except ValueError:
        messagebox.showerror("Error", "invalid inputs")
    finally:
        txtNum1.delete(0, END)
        txtNum2.delete(0, END)
        txtNum1.focus()


if __name__ == "__main__":
    window = Tk()
    label1 = Label(window, text="Enter 1st number")
    label2 = Label(window, text="Enter 2nd number")
    # fo textbox we use Entry widget
    txtNum1 = Entry(window)
    txtNum2 = Entry(window)
    btnAdd = Button(window, text="sum", command=displaySum)

    label1.grid(row=1, column=1)
    label2.grid(row=2, column=1)
    txtNum1.grid(row=1, column=2)
    txtNum2.grid(row=2, column=2)
    btnAdd.grid(row=3, column=1)
    window.mainloop()
