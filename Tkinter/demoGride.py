from tkinter import *

if __name__ == "__main__":
    window = Tk()
    window.title("mywindow")
    window.geometry("300x400")
    window.configure(bg="yellow")

    label1 = Label(window,text="first label")
    label2 = Label(window, text="second label")
    label3 = Label(window, text="third label")
    label4 = Label(window, text="fourth label")

    label1.grid(row=1,column=4)
    label2.grid(row=5,column=7)
    # label3.pack(side=LEFT)
    window.mainloop()
