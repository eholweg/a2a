'''
#!/awips2/python/bin/python
'''

from subprocess import call
import re
import lib.AAentry as AA

def loadAA( file ):
    dictionary = {}
    fh = open(file)
    while True:
        line = fh.readline()
        if not line:
            break
        elif not re.match(r'^#', line) and not re.match(r'^\n', line):
            entry = line.rstrip()
            print(entry)
            e = entry.split()
            pil = e[0]
            wmo = e[1]
            icao = e[2]
            dictionary[pil] = AA.AAentry(pil, wmo, icao)
    fh.close()
    return dictionary


# Need vlab username
#vlabName = raw_input("What is your VLAB user name? ")
vlabName = 'test.test'

# Need site we are cleaning up
#siteID = raw_input("What is your site id (ie MRX, FWD, etc)? ").upper()
siteID = 'MRX'

# Need node for site
#node = raw_input("What is your AWIPS send node (First three chars in AWIPS pil MEMZFPMRX... node is MEM)? ").upper()
node = 'MEM'

# Get the user metar sites


raw_metar = raw_input("Please list your METAR sites. Separate each site with a space. (ie TYS TRI CHA OQT)")
metars = raw_metar.split()
print("METAR PILS")
for m in metars:
    pil=node+"MTR"+m
    metarAA = AA.AAentry(pil, "SAUSXX", "KMRX")
    metarD
    print(pil)

# get the user climate locations
raw_climate = raw_input("Please list your climate sites. Separate each site with a space. (TYS TRI CHA)")
climate = raw_climate.split()
print("CLIMATE PILS")
for c in climate:
    print("")



natAAfile = '../inputA2A/afos2awips.txt'
siteAAfile="../inputA2A/" + siteID + "-afos2awips.txt"

# Get copy of national A2A off of NDM
command = "svn export --force https://vlab.ncep.noaa.gov/svn/awips-ndm/trunk/afos2awips.txt --username " + vlabName + " "+natAAfile
print(command)
#call(command, shell=True)

# Get copy of site A2A off of common_static
edexTree = "/awips2/edex/data/utility/common_static"
command = "cp " + edexTree + "/site/" + siteID + "/afos2awips/afos2awips.txt "+siteAAfile
print(command)
#call(command, shell=True)


a1=AA.AAentry("MEMZFPMRX", "WPUS91", "KMRX")
a2=AA.AAentry("MEMZFPOHX", "WPUS91", "KOHX")
a3=AA.AAentry("MEMZFPMRX", "WPUS91", "KMRX")
print (a1)
print (a1 == a3)
print (a1 == a2)

# Read baseline file into array
# If line is not started with # or is a blank line...
# Read and store into array as object.

natAAfile = '../inputA2A/afos2awips.txt'
NATa2a = loadAA(natAAfile)
SITEa2a = loadAA(siteAAfile)


# For every file in baseline with correct NODE... pull it out
# For every file in site with correct NODE... pull it out