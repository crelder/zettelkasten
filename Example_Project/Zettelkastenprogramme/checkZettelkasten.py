# -*- coding: utf-8 -*-

import os, re


##########################
######### INPUT ##########
##########################

zettelkastenDirectory = os.listdir('../Zettelkasten') #Link to Zettelkasten-directory

def zettelFilter(allFilenames):
    filteredFilenames = []
    for fileName in sorted(allFilenames):
        if fileName.endswith(".png"):
            filteredFilenames.append(fileName)
    return filteredFilenames


#########################
###### FUNCTIONS ########
#########################


################## Check if all IDs are unique ##########################
def getDoubleIDs(allFilenames):
    results = []
    for filename in zettelFilter(allFilenames):
        liste = sorted(allFilenames)
        liste.remove(filename)
        for n in liste:
            if filename.startswith(n[:7]):
                results.append(n[:7])
	### Remove doubled IDs in variable results
    cleanResults = []
    if list(set(results)):
        for i in list(set(results)):
            cleanResults.append(i)
    return cleanResults


################### Check if all links work (all Link points to an existing ID) ###
def getEmptyLinks(allFilenames): 
    sortedFilenames = zettelFilter(allFilenames)

    ids = [filename[:7] for filename in sortedFilenames]

    links = ', '.join(map(lambda x: x[7:], sortedFilenames))
    foundLinks = re.findall("\d{6}[a-z]{1}", links)

    emptyLinks = []
    for link in foundLinks:
        if not link in ids:
             emptyLinks.append(link)
    return emptyLinks

################### Check, if IDs have the correct format #################
def getIDsWithUncorrectFormat(allFilenames):  # 1703128c  wird noch nicht erkannt!
    ids = map(lambda x: " " + x[:8], zettelFilter(allFilenames))
    wrongIDFormats = []
    for x in ids:
        if not re.match("\s{1}\d{6}[a-z]{1}\s{1}", x):
            wrongIDFormats.append(x[1:])
    return wrongIDFormats


#######################################
############### OUTPUT ################
#######################################

print( " ")
print( "#################################")
print( "### ZETTELKASTEN HEALTH CHECK ###")
print( "#################################")
print( " ")

### Check, if all links point to an existing ID ###
a = getEmptyLinks(zettelkastenDirectory)
if a:
    print( "Broken links!")
    for i in a:
        print( i )
else:
    print( "All links point to an existing ID.")
print( " ")


### Check if all IDs are unique ###
b = getDoubleIDs(zettelkastenDirectory)
if b:
    print( "These IDs exist several times!")
    for i in b:
        print( i)
else:
    print( "All IDs are unique.")
print( " ")


### Check, if IDs have the correct format ###
e = getIDsWithUncorrectFormat(zettelkastenDirectory)
if e:
    print( "The following IDs have a wrong format!")
    for i in e:
        print( i)
else:
    print( "All IDs have the correct format.")
print( " ")


print( "##################################")
print( " ")

input()
