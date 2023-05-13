from cake import Cake
import os


def ShowallCake():
    if os.path.exists("cakedata.txt"):
        with open('cakedata.txt', "r") as fp:
            data = fp.read()
            print(data)
    else:
        print("file is not present")


def viewCart():
    if os.path.exists("cartdata.txt"):
        with open('cartdata.txt', "r") as fp:
            data = fp.read()

            print(data)
    else:
        print("file is not present")


def billDetails():
    if os.path.exists("cartdata.txt"):
        with open('cartdata.txt', "r") as fp:
            Total = 0
            for cake in fp:
                cake = cake.strip()
                cake = cake.split(",")
                cake.append(str(float(cake[2]) * int(cake[3])))
                cake = " ".join(cake) + "\n"
                with open("cart_details.txt", "w") as fp:
                    fp.write(cake)
            with open("cart_details.txt", "a") as fp:
                fp.write("--------------------------------------------------------")

    else:
        print("file is not present")


class UserMgmt:

    def searchCakebyid(id):
        if os.path.exists("cakedata.txt"):
            with open('cakedata.txt', "r") as fp:
                for cake in fp:
                    try:
                        cake.index(str(id), 0, 4)
                    except:
                        pass
                    else:
                        print("cake present")
                        break
                else:
                    print("cake not found")

        else:
            print("file is not present")

    def searchCakebyName(name):
        if os.path.exists("cakedata.txt"):
            with open('cakedata.txt', "r") as fp:
                for cake in fp:
                    if name in cake:
                        print("record found")
                        break
                else:
                    print("record not found")

        else:
            print("file is not present")

    def addTOcart(id, qty):
        if os.path.exists("cakedata.txt"):
            with open('cakedata.txt', "r") as fp:
                allCake = []
                found = False
                for cake in fp:
                    try:
                        cake.index(str(id), 0, 4)
                    except:
                        # no match
                        pass
                    else:
                        # match
                        found = True
                        # str tp list
                        cake = cake.split(",")
                        cake[3] = int(cake[3]) - qty
                        cake[3] = str(cake[3]) + "\n"
                        # convert list to string
                        cake = ",".join(cake)
                        with open("cartdata.txt", "a") as fp1:
                            # details = str(id) + "," + str(qty) + cake[1] + str(cake[2]) + "\n"
                            # cake[3] = str(qty)

                            fp1.write(cake)
                            # fp.write(cake)
                        # i want selected cake should be in cart_details.txt
                    finally:
                        allCake.append(cake)

            print(allCake)

            if found:
                with open("cakedata.txt", 'w') as fp:
                    for cake in allCake:
                        fp.write(cake)
            else:
                print("record not found")
        else:
            print("file is not present")

    def editCakebyid(id, qty):
        if os.path.exists("cartdata.txt"):
            with open('cartdata.txt', "r") as fp:
                allCake = []
                found = False
                for cake in fp:
                    try:
                        cake.index(str(id), 0, 4)
                    except:
                        # no match
                        pass
                    else:
                        # match
                        found = True
                        # str tp list
                        cake = cake.split(",")
                        ans = input("Do you want to change quantity(y/n)?")
                        if ans.lower() == 'y':
                            cake[3] = input("Enter the new quantity:")
                            # ans = input("Do you want to change Salary(y/n)?")
                            # if ans.lower() == 'y':
                            #     cake[2] = float(input("Enter the new salary:"))
                            cake[3] = str(cake[3]) + "\n"
                            # convert list to string
                            cake = ",".join(cake)

                    finally:
                        allCake.append(cake)

            print(allCake)

            if found:
                with open("cartdata.txt", 'w') as fp:
                    for cake in allCake:
                        fp.write(cake)

            else:
                print("record not found")

        else:
            print("file is not present")
