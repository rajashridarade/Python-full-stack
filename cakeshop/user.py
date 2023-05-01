from useMgmt import UserMgmt, ShowallCake,billDetails,viewCart
from cake import Cake


def user():
    choice = 0
    while choice != 10:
        print("\t\t1.Display all Cake")
        print("\t\t2.searchbyid Cake")
        print("\t\t3.searchbyName Cake")
        print("\t\t4.Add to cart")
        print("\t\t5.Buy(billDetails) items")
        print("\t\t6.View Cart ")
        print("\t\t10.Exist")
        choice = int(input("Enter a choice :"))
        if choice == 1:
            ShowallCake()
        elif choice == 2:
            id = int(input("Enter id :"))
            UserMgmt.searchCakebyid(id)
        elif choice == 3:
            name = input("Enter name :")
            UserMgmt.searchCakebyName(name)
        elif choice == 4:
            id = int(input("Enter id :"))
            qty = int(input("enter quntity"))
            UserMgmt.addTOcart(id,qty)
        elif choice == 5:
            billDetails()
        elif choice == 6:
            viewCart()
        elif choice == 10:
            print("____________program end ----------------")
        else:
            print("invalid choice")


if __name__ == "__main__":
    user()
