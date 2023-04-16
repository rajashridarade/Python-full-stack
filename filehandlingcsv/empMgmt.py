from emp import Emp
import os


def ShowallEmp():
    if os.path.exists("empdata.txt"):
        with open('empdata.txt', "r") as fp:
            data = fp.read()
            print(data)
    else:
        print("file is not present")


class EmpMgmt:
    def addEmp(e):
        with open("empdata.txt", 'a') as fp:
            fp.write(str(e))
            fp.write("\n")

    def searchEmpbyid(id):
        if os.path.exists("empdata.txt"):
            with open('empdata.txt', "r") as fp:
                for emp in fp:
                    try:
                        emp.index(str(id), 0, 4)
                    except:
                        pass
                    else:
                        print("Record present")
                        break
                else:
                    print("record not found")

        else:
            print("file is not present")

    def searchEmpbyName(name):
        if os.path.exists("empdata.txt"):
            with open('empdata.txt', "r") as fp:
                for emp in fp:
                    if name in emp:
                        print("record found")
                        break
                else:
                    print("record not found")

        else:
            print("file is not present")

    def deleteEmpbyid(id):
        if os.path.exists("empdata.txt"):
            with open('empdata.txt', "r") as fp:
                allEmp = []
                found = False
                for emp in fp:
                    try:
                        emp.index(str(id), 0, 4)
                    except:
                        # no match
                        allEmp.append(emp)
                    else:
                        # match
                        found = True

            print(allEmp)

            if found:
                with open("empdata.txt", 'w') as fp:
                    for emp in allEmp:
                        fp.write(emp)

            else:
                print("record not found")

        else:
            print("file is not present")

    def editEmpbyid(id):
        if os.path.exists("empdata.txt"):
            with open('empdata.txt', "r") as fp:
                allEmp = []
                found = False
                for emp in fp:
                    try:
                        emp.index(str(id), 0, 4)
                    except:
                        # no match
                        pass
                    else:
                        # match
                        found = True
                        # str tp list
                        emp = emp.split(",")
                        ans = input("Do you want to change name(y/n)?")
                        if ans.lower() == 'y':
                            emp[1] = input("Enter the new name:")
                        ans = input("Do you want to change Salary(y/n)?")
                        if ans.lower() == 'y':
                            emp[2] = float(input("Enter the new salary:"))
                            emp[2] = str(emp[2]) + "\n"
                            # convert list to string
                            emp = ",".join(emp)

                    finally:
                        allEmp.append(emp)

            print(allEmp)

            if found:
                with open("empdata.txt", 'w') as fp:
                    for emp in allEmp:
                        fp.write(emp)

            else:
                print("record not found")

        else:
            print("file is not present")
