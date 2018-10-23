'''
#!/awips2/python/bin/python
'''

from subprocess import call

# Need vlab username
vlabName = raw_input("What is your VLAB user name? ")

# Need site we are cleaning up
siteID = raw_input("What is your site id (ie MRX, FWD, etc)? ").upper()

# Need node for site
node = raw_input("What is your AWIPS send node (First three chars in AWIPS pil MEMZFPMRX... node is MEM)? ").upper()

# Get copy of national A2A off of NDM
command = "svn export --force https://vlab.ncep.noaa.gov/svn/awips-ndm/trunk/afos2awips.txt --username " + vlabName + " ../a2aInput/"
print(command)
#call(command, shell=True)


# Get copy of site A2A off of common_static
edexTree = "/awips2/edex/data/utility/common_static"
command = "cp " + edexTree + "/site/" + siteID + "/afos2awips/afos2awips.txt ../a2aInput/" + siteID + "-afos2awips.txt"
print command
#call(command, shell=True)


# Read baseline file into array
# Read Site file into array

# For every file in baseline with correct NODE... pull it out
# For every file in site with correct NODE... pull it out