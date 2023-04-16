class Cake:
    def __init__(self,id,nm,bs):
        self.cid = id
        self.name = nm
        self.basic = bs

    def __str__(self):
        return str(self.cid)+","+self.name+","+str(self.basic)
