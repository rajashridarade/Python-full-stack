from tkinter import *

def cleardata():
    txtId.delete(0,END)
    txtName.delete(0,END)
    txtbasic.delete(0,END)
    txtId.focus()

def addEmp():
    eid = txtId.get()
    ename = txtName.get()
    basic = txtbasic.get()
    emp = eid+","+ename+","+basic
    listMain.insert(END,emp)
    cleardata()

def selectEmp():
    cleardata()
    index.set(listMain.curselection()[0])
    emp = listMain.get(ACTIVE)  #emp is string
    emp = emp.split(",")        #string to list
    txtId.insert(0,emp[0])
    txtName.insert(0,emp[1])
    txtbasic.insert(0,emp[2])


def updateEmp():
    i = index.get()
    eid = txtId.get()
    ename = txtName.get()
    basic = txtbasic.get()
    emp = eid + "," + ename + "," + basic
    listMain.delete(i)
    listMain.insert(i, emp)
    cleardata()



def deleteEmp():
    listMain.delete(ACTIVE)
    cleardata()


if __name__ == "__main__":
    window = Tk()
    index = IntVar()

    frame1 = Frame(window, highlightbackground="blue", highlightthickness=2)
    frame2 = Frame(window, highlightbackground="blue", highlightthickness=2)
    frame3 = Frame(window, highlightbackground="blue", highlightthickness=2)

    labID = Label(frame1, text="Eid")
    labEname = Label(frame1, text="Ename")
    labBasic = Label(frame1, text="basic")

    txtId = Entry(frame1)
    txtName = Entry(frame1)
    txtbasic = Entry(frame1)

    labID.grid(row=1, column=1)
    labEname.grid(row=2, column=1)
    labBasic.grid(row=3, column=1)
    txtId.grid(row=1, column=2)
    txtName.grid(row=2, column=2)
    txtbasic.grid(row=3, column=2)

    btnAdd = Button(frame2, text="ADD", command=addEmp)
    btnSelect = Button(frame2, text="SELECT", command=selectEmp)
    btnUpdate = Button(frame2, text="UPDATE", command=updateEmp)
    btnDelete = Button(frame2, text="DELETE", command=deleteEmp)

    btnAdd.pack(side=LEFT)
    btnSelect.pack(side=LEFT)
    btnUpdate.pack(side=LEFT)
    btnDelete.pack(side=LEFT)

    scrollbar = Scrollbar(frame3)
    scrollbar.pack(side=RIGHT, fill=Y)
    listMain = Listbox(frame3, yscrollcommand=scrollbar.set)
    scrollbar.configure(command=listMain.yview())

    listMain.pack()

    frame1.pack()
    frame2.pack()
    frame3.pack()
    window.geometry("300x200")
    window.mainloop()
