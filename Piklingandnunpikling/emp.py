class Emp:
    def __init__(self, id, nm, bs):
        self.cid = id
        self.name = nm
        self.basic = bs

    def __str__(self):
        data = "EID = " + str(self.cid)
        data += "\nEname=" + self.name
        data += "\nbasic=" + str(self.basic)
        return data
