class Emp:
    def __init__(self,id,nm,bs):
        self.eid = id
        self.name = nm
        self.basic = bs

    def __str__(self):
        return str(self.eid)+","+self.name+","+str(self.basic)
