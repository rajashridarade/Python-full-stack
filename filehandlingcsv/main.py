from empMgmt import EmpMgmt, ShowallEmp
from emp import Emp

if __name__ == "__main__":
    choice = 0
    while choice != 10:
        print("\t\t1.Add new Emp")
        print("\t\t2.Display all emp")
        print("\t\t3.searchbyid emp")
        print("\t\t4.searchbyName emp")
        print("\t\t5.Delete by id")
        print("\t\t6.Edit by id")

        print("\t\t10.Exist")
        choice = int(input("Enter a choice :"))
        if choice == 1:
            id = int(input("Enter id :"))
            nm = input("enter name :")
            bs = float(input("enter salary :"))
            e = Emp(id,nm,bs)
            EmpMgmt.addEmp(e)
        elif choice == 2:
            ShowallEmp()
        elif choice == 3:
            id = int(input("Enter id :"))
            EmpMgmt.searchEmpbyid(id)
        elif choice == 4:
            name = input("Enter name :")
            EmpMgmt.searchEmpbyName(name)
        elif choice == 5:
            id = int(input("Enter id :"))
            EmpMgmt.deleteEmpbyid(id)
        elif choice == 6:
            id = int(input("Enter id :"))
            EmpMgmt.editEmpbyid(id)
        elif choice == 10:
            print("____________program end ----------------")
        else:
            print("invalid choice")
