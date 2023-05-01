from cakeMgmt import CakeMgmt, ShowallCake
from cake import Cake


def Admin():
    choice = 0
    while choice != 10:
        print("\t\t1.Add new Cake")
        print("\t\t2.Display all Cake")
        print("\t\t3.searchbyid Cake")
        print("\t\t4.searchbyName Cake")
        print("\t\t5.Delete by id")
        print("\t\t6.Edit by id")

        print("\t\t10.Exist")
        choice = int(input("Enter a choice :"))
        if choice == 1:
            id = int(input("Enter id :"))
            nm = input("enter name :")
            bs = float(input("enter price :"))
            qty = int(input("Enter quantity:"))
            e = Cake(id, nm, bs,qty)
            CakeMgmt.addCake(e)
        elif choice == 2:
            ShowallCake()
        elif choice == 3:
            id = int(input("Enter id :"))
            CakeMgmt.searchCakebyid(id)
        elif choice == 4:
            name = input("Enter name :")
            CakeMgmt.searchCakebyName(name)
        elif choice == 5:
            id = int(input("Enter id :"))
            CakeMgmt.deleteCakebyid(id)
        elif choice == 6:
            id = int(input("Enter id :"))
            CakeMgmt.editCakebyid(id)
        elif choice == 10:
            print("____________program end ----------------")
        else:
            print("invalid choice")


if __name__ == "__main__":
    Admin()
