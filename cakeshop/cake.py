class Cake:
    def __init__(self,id,nm,bs,qty):
        self.cid = id
        self.name = nm
        self.basic = bs
        self.qty = qty

    def __str__(self):
        return str(self.cid)+","+self.name+","+str(self.basic)+","+str(self.qty)
