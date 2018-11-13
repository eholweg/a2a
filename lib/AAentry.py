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

