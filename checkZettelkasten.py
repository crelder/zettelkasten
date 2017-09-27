# -*- coding: utf-8 -*-

import os, re


##########################
######### INPUT ##########
##########################

zettelkastenDirectory = os.listdir('../Zettelkasten') #Link to Zettelkasten-directory

def zettelFilter(allFilenames):
    filteredFilenames = []
    for fileName in sorted(allFilenames):
        if fileName.endswith(".png") or fileName.endswith(".txt") or fileName.endswith(".pdf"):
            filteredFilenames.append(fileName)
    return filteredFilenames


#########################
###### FUNCTIONS ########
#########################

######### Check, if Literaturesources exist in Bibtex file ###########
def getBibkeysZettel(allZettelNames):
    a = []
    for zettelName in allZettelNames:
        if zettelName.find("-", 9) != -1:
            a.append(zettelName[zettelName.find("-", 9)+2:])

    b = re.findall('[a-zA-Z,]+\d{4}', ' '.join(a))
    c = map(lambda x:x.lower(), b)
    bibkeys = map(lambda x:x.replace(" ", ""), c)

    return bibkeys

def getBibkeysBibfile(string):
    bibkeys = re.findall('[@]{1}\S+[{]{1}[A-Za-z]+\d{4}[,]{1}', string)
    bibkeys = map(lambda x: x[x.find("{") +1 : len(x)-1], bibkeys)
    return bibkeys

def checkBibkeyExistence(bibkeysZettel, bibkeysBibfile):
    missingBibkeys = []
    for bibkey in bibkeysZettel:
        if not bibkey in bibkeysBibfile:
            missingBibkeys.append(bibkey)
    return list(set(missingBibkeys))

def getMissingBibkeys(zettelkastenDirectory):
    bibkeysZettel = getBibkeysZettel(zettelFilter(zettelkastenDirectory))
    bibfile = open('Dissertation.bib')
    bibkeysBibfile = sorted(getBibkeysBibfile(bibfile.read()))
    return checkBibkeyExistence(bibkeysZettel, bibkeysBibfile)


################## Check Format of links ########################
#def getWrongFormats(allFilenames):
#    sortedFilenames = map(lambda x: x[8:len(x)-4], zettelFilter(allFilenames))
    # Tolerant criteria for identifying potential (wrong) links and IDs
#    findings = re.findall("\S{0,3}\d{5,20}\D{3}", ', '.join(sortedFilenames))
#    wrongFormats = []
#    for x in findings:
#        if not re.match("\d{6}[a-z]{1}", x):  # Hier muss noch die Suche geschärft werden.
#            wrongFormats.append(x)
#    return wrongFormats


################## Check if any IDs are doubled ##########################
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
            print("link in ids:", link in ids)
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

### Check Links ###
a = getEmptyLinks(zettelkastenDirectory)
if a:
    print( "Broken links!")
    for i in a:
        print( i )
else:
    print( "All links point to an existing ID.")
print( " ")


### Check IDs ###
b = getDoubleIDs(zettelkastenDirectory)
if b:
    print( "These IDs exist several times!")
    for i in b:
        print( i)
else:
    print( "All IDs are unique.")
print( " ")


### Check Format of Links ####
#c = getWrongFormats(zettelkastenDirectory)
#if c: #Error!
#    print( "The following link formats are not correct!"
#    for i in c:
#        print( i
#else:
#    "All links have the correct format."
#print( " "


################### Check, if IDs have the correct format ########
e = getIDsWithUncorrectFormat(zettelkastenDirectory)
if e:
    print( "The following IDs have a wrong format!")
    for i in e:
        print( i)
else:
    print( "All IDs have the correct format.")
print( " ")


### Check, if Literaturesources exist in Bibtex file ###
d = sorted(getMissingBibkeys(zettelkastenDirectory))
if d:
    print( "The following literature sources are not in the bibtex file!")
    for i in d:
        print( i)
else:
    print( "All literature sources are in the bibtex file.")
print( " ")


print( "##################################")
print( " ")

input()
