import lib.AAentry as AA

# TESTS TO RUN FOR AAentry Class

a1=AA.AAentry("MEMZFPMRX", "WPUS91", "KMRX")
a2=AA.AAentry("MEMZFPOHX", "WPUS91", "KOHX")
a3=AA.AAentry("MEMZFPMRX", "WPUS91", "KMRX")
print (a1)
print (a1 == a3)
print (a1 == a2)
print (a1.isSamePil("MEMPFMMRX"))
print (a1.isSamePil("MEMZFPMRX"))
print (a2.isSameICAO("KMRX"))
print (a2.isSameICAO("KJAN"))
print (a2.isSameICAO("KOHX"))
print (a3.isSameWMO("WPUS91"))
print (a3.isSameWMO("SPUS99"))

print("")

print(a1.getPil())
print(a1.getNode())
print(a1.getProduct())
print(a1.getSite())
print(a1.getIcaoID())