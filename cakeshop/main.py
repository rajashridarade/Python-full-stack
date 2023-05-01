from admin import Admin
from user import user

if __name__ == "__main__":
    print("\t\t1.Admin")
    print("\t\t2.User")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        uname = input("Enter user name")
        pwd = input("enter password")
        if uname == "Admin" and pwd == "admin123":
            Admin()
        else:
            print("invalid credentials")

    elif choice == 2:
        uname = input("Enter user name")
        pwd = input("enter password")
        if uname == "user" and pwd == "user123":
            user()
        else:
            print("invalid credentials")

