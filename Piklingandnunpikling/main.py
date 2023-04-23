import pickle
from emp import Emp


def serialization():
    e1 = Emp(11, "RADHA", 3400)
    with open("empData.dat", "wb") as fp:
        pickle.dump(e1, fp)


def Deserialization():
    with open("empData.dat", "rb") as fp:
        e1 = pickle.load(fp)
        print(e1)


if __name__ == "__main__":
    Deserialization()
    # serialization()
