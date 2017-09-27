#!/usr/bin/env
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
            filteredFilenames.append(fileName[:len(fileName)-4])
    return filteredFilenames 

zettelNames = zettelFilter(zettelkastenDirectory)

##########
#METHODS##
##########

def getID(zettel):
	return zettel[:7]

def getKeywords(zettel):  #Hier wird oft noch das Ende des Strings abgeschnitten!
	
	#return zettel[:7]  #labels sind IDs
	
	if zettel.find(" - ", 10) != -1: #labels sind Keywords
		return zettel[10: zettel.find("- ", 10)]
	else:
		return zettel[10:]

def getLinks(zettel):
	return re.findall("\d{6}[a-z]{1}", zettel[10:])


def buildNode(zettel):
	return '<node id="' + zettel[0] + '" label="' + zettel[1] + '"/>'

def buildEdge(zettel, link , i):
	return '<edge id="' + str(i) + '" source="' + zettel[0] + '" target="' + link + '"/>'
	

##########
##OUTPUT##
##########

##### Build Zettelkasten
zettelkasten = []
for zettel in zettelNames:
	zettelkasten.append([getID(zettel), getKeywords(zettel), getLinks(zettel)])

header = '<?xml version="1.0" encoding="UTF-8"?> \n<gexf xmlns:viz="http:///www.gexf.net/1.1draft/viz" version="1.1" xmlns="http://www.gexf.net/1.1draft"> \n<meta lastmodifieddate="2010-03-03+23:44"> \n<creator>Gephi 0.7</creator> \n</meta> \n<graph defaultedgetype="directed" idtype="string" type="static"> \n'

nodes = []
for zettel in zettelkasten:
	nodes.append(buildNode(zettel))
nodeCount = '<nodes count="' + str(len(nodes)) + '">\n'

edges = []
i = 1
for zettel in zettelkasten:
	if zettel[2]: #Möglicherweise auch einfach löschen!
		for link in zettel[2]:
			edges.append(buildEdge(zettel, link, i))
			i += 1
edgecount = '<edges count="' + str(len(edges)) + '">\n'


end = '</graph>\n</gexf>'

Gephi_zettelkasetn = open('Gephi_zettelkasetn.gexf', 'w')
Gephi_zettelkasetn.write(header + nodeCount + '\n'.join(nodes) + '\n</nodes>\n'+ edgecount + '\n'.join(edges) + '\n</edges>\n' + end)