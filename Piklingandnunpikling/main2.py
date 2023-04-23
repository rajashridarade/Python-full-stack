import pickle
from emp import Emp


def serialization(obj):
    with open("myData.dat", "wb") as fp:
        pickle.dump(obj, fp)


def Deserialization():
    with open("myData.dat", "rb") as fp:
        obj = pickle.load(fp)
        return obj


def store():
    e1 = Emp(11, "RADHA", 3400)
    e2 = Emp(12, "ADHA", 3400)
    e3 = Emp(13, "DHA", 3400)
    e4 = Emp(14, "sayalo", 3400)
    e5 = Emp(16, "mahesh", 3400)
    # allEMP = {11: e1, 12: e2, 13: e3, 14: e4, 16: e5}
    allEMP = { e1:11, e2:12, e3: 13,e4:14, e5:16}

    serialization(allEMP)


def fetch():
    obj = Deserialization()
    # print(OBJ)
    for x, y in obj.items():
        print(x)


if __name__ == "__main__":
    # store()
    fetch()
    # Deserialization()
    # serialization()
