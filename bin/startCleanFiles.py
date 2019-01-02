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
            #print(entry)
            e = entry.split()
            pil = e[0]
            wmo = e[1]
            icao = e[2]
            dictionary[pil] = AA.AAentry(pil, wmo, icao)
    fh.close()
    return dictionary


# GET VLAB USER NAME
#vlabName = raw_input("What is your VLAB user name? ")
vlabName = 'test.test'

# GET LOCAL SITE ID
#siteID = raw_input("What is your site id (ie MRX, FWD, etc)? ").upper()
siteID = 'MRX'

# GET NODE FOR SITE
#node = raw_input("What is your AWIPS send node (First three chars in AWIPS pil MEMZFPMRX... node is MEM)? ").upper()
node = 'MEM'


# LOAD NATIONAL A2A FILE
natAAfile = '../inputA2A/afos2awips.txt'
vlabLink = 'https://vlab.ncep.noaa.gov/svn/awips-ndm/trunk/afos2awips.txt'
command = "svn export --force " + vlabLink + " --username " + vlabName + " "+natAAfile
print(command)
#call(command, shell=True)
NATa2a = loadAA(natAAfile)

#Filter National File To Pull Only
#CORRECT WMOID (INCLUDES CLIMATE AND METAR SITES)
# KMRX
for keyPil, value in NATa2a.items():
    if ( value.getIcaoID()!="K"+siteID ):
        # REMOVE FROM THE NATIONAL FILE
        NATa2a.pop(keyPil)

# NOW SHOULD ONLY HAVE ENTRIES WITH CORRECT ICAOID
# WRITE THE ENTRIES TO A FILE FOR LATER EVALUATION
natAAfileForSite='../data/NatA2Afor'+siteID+".txt"
f = open(natAAfileForSite,"w")

f.write("HERE ARE THE PILS FOR SITE "+siteID+"\n")
f.write("THAT ARE CURRENTLY IN THE NATIONAL A2A FILE\n")
for keys,values in NATa2a.items():
    f.write(str(values)+"\n")
f.close()

# WORK ON SITE LEVEL FILES
#Run external script to create a composite site file from AWIPS
#TODO - CREATE LINUX SCRIPT TO CREATE SITE FILE IN inputA2A directory

#LOAD THE FILE YOU CREATED INTO A DICTIONARY
edexTree = "/awips2/edex/data/utility/common_static"
siteAAfile="../inputA2A/" + siteID + "-afos2awips.txt"
command = "cp " + edexTree + "/site/" + siteID + "/afos2awips/afos2awips.txt.NEW.ORIG "+siteAAfile
print(command)
#call(command, shell=True)
SITEa2a = loadAA(siteAAfile)

#PULL OUT ALL ENTRIES THAT DO NOT HAVE YOUR SITE WMOID
for keyPil, value in SITEa2a.items():
    if ( value.getIcaoID()!="K"+siteID ):
        # REMOVE FROM THE SITE FILE
        SITEa2a.pop(keyPil)

# NOW SHOULD ONLY HAVE ENTRIES WITH CORRECT ICAOID
# WRITE THE ENTRIES TO A FILE FOR LATER EVALUATION
siteAAfileForSite='../data/siteA2Afor'+siteID+".txt"
f = open(siteAAfileForSite,"w")

f.write("HERE ARE THE PILS FOR SITE "+siteID+"\n")
f.write("THAT ARE CURRENTLY IN YOUR SITE LEVEL A2A FILE\n")
for keys,values in SITEa2a.items():
    f.write(str(values)+"\n")
f.close()

#NOW GO THROUGH YOUR SITE FILE LINE BY LINE
# FOR EACH LINE CHECK IF IT IS IN THE NEW NATIONAL FILE YOU HAVE
# IF SO... COPY TO ALREADY INCLUDED FILE
# IF NOT... COPY TO NEED TO INCLUDE FILE
inNatA2A={}
for keyPil, value in SITEa2a.items():
    for natKeyPil, natVal in NATa2a.items():
        if (value == natVal):
            inNatA2A[keyPil]= value
            SITEa2a.pop(keyPil)
            break

# SITE FILE WILL NOW ONLY HAVE ENTRIES THAT WERE NOT
# IN THE NATIONAL a2a FILE
siteAAfileForSite='../data/SiteOnlyA2Afor'+siteID+".txt"
f = open(siteAAfileForSite,"w")

f.write("HERE ARE THE PILS THAT WERE ONLY\n")
f.write("FOUND IN THE SITE LEVEL A2A\n")
f.write("(THESE NEED TO BE ADDED TO THE BASELINE)\n")
for keys,values in SITEa2a.items():
    f.write(str(values)+"\n")
f.close()

# inNatA2A WILL NOW CONTAIN ONLY THOSE ENTRIES THAT WERE
# IN BOTH THE SITE AND NATIONAL NDM A2A
siteEntriesAlreadyInNatAA='../data/SiteEntriesAlreadyInNatA2A_'+siteID+".txt"
f = open(siteEntriesAlreadyInNatAA,"w")

f.write("HERE ARE THE PILS THAT WERE FOUND IN\n")
f.write("BOTH THE SITE AND THE NATIONAL A2A\n")
f.write("(THESE DO NOT NEED TO BE ADDED TO THE BASELINE)\n")
for keys,values in inNatA2A.items():
    f.write(str(values)+"\n")
f.close()

exit(0)

# Review the site file... determine where pils are
# Pils can already be in the baseline file
baselineDict={}
siteOnlyDict={}
# Pils can not yet be in the baseline file
for siteEntry in SITEa2a:
    siteLine=SITEa2a[siteEntry]
    for natEntry in NATa2a:
        natLine=NATa2a[natEntry]
        if siteLine == natLine:
            #print("IS IN NATIONAL FILE: "+ siteLine.getPil())
            baselineDict[siteLine.getPil()] = siteLine
        else:
            #Pil is not in the national file... so check to see
            #if it is a pil that belongs to us?
            #Looking for 1. Correct Node
            #            2. Correct Site including climate and metar sites.
            # metar / climate
            # for sid in metar:
            #     name=node+''
            #     for  in climateMetar
            #     if siteLine.getPil()

            #If it is then add to the siteOnlyDictionary
            #print("NOT IN NATIONAL FILE: "+ siteLine.getPil())
            siteOnlyDict[siteLine.getPil()] = siteLine

print "HERE ARE THE SITE ONLY PILS (THESE WILL NEED TO BE ADDED TO THE BASELINE)"
for p in siteOnlyDict:
    print(siteOnlyDict[p])

print "HERE ARE THE SITE PILS ALREADY IN NAT FILE"

