class AAentry:
    pil = ""
    wmoid = ""
    icaoid = ""

    def __init__(self, pil="", wmoid = "", icaoid = ""):
        """ Create a new point at x, y """
        self.pil = pil
        self.wmoid = wmoid
        self.icaoid = icaoid

    def __str__(self):
        return "%s %s %s" % (self.pil, self.wmoid, self.icaoid)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def getPil(self):
        return self.pil

    def getIcaoID(self):
        return self.icaoid

    def getNode(self):
        return self.pil[:3]

    def getProduct(self):
        return self.pil[3:6]

    def getSite(self):
        return self.pil[6:]

    def isSamePil(self, p):
        if self.pil == p:
            return True
        else:
            return False

    def isSameWMO(self, w):
        if self.wmoid == w:
            return True
        else:
            return False

    def isSameICAO(self, i):
        if self.icaoid == i:
            return True
        else:
            return False
