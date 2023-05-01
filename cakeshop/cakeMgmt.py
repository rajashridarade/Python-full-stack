from cake import Cake
import os


def ShowallCake():
    if os.path.exists("cakedata.txt"):
        with open('cakedata.txt', "r") as fp:
            data = fp.read()
            print(data)
    else:
        print("file is not present")


class CakeMgmt:
    def addCake(c):
        with open("cakedata.txt", 'a') as fp:
            # fp.write("ID  Name  price  Qty\n")
            # fp.write("----------------------\n")
            fp.write(str(c))
            fp.write("\n")

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

    def deleteCakebyid(id):
        if os.path.exists("cakedata.txt"):
            with open('cakedata.txt', "r") as fp:
                allCake = []
                found = False
                for cake in fp:
                    try:
                        cake.index(str(id), 0, 4)
                    except:
                        # no match
                        allCake.append(cake)
                    else:
                        # match
                        found = True

            print(allCake)

            if found:
                with open("cakedata.txt", 'w') as fp:
                    for cake in allCake:
                        fp.write(cake)

            else:
                print("record not found")

        else:
            print("file is not present")

    def editCakebyid(id):
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
                        ans = input("Do you want to change name(y/n)?")
                        if ans.lower() == 'y':
                            cake[1] = input("Enter the new name:")
                        ans = input("Do you want to change Salary(y/n)?")
                        if ans.lower() == 'y':
                            cake[2] = float(input("Enter the new salary:"))
                            cake[2] = str(cake[2]) + "\n"
                            # convert list to string
                            cake = ",".join(cake)

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
