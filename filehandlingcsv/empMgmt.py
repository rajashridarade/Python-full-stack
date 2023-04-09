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
