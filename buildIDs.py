#!/usr/bin/env
# -*- coding: utf-8 -*-

import os, re, string

def zettelFilter(allFilenames):
    filteredFilenames = []
    for fileName in sorted(allFilenames):
        if fileName.endswith(".png") or fileName.endswith(".txt") or fileName.endswith(".pdf"):
            filteredFilenames.append(fileName)
    return filteredFilenames

def makeID(zettel):
	for letter in string.ascii_lowercase:
		print( letter)
		print( idExists(zettel[:6]+letter))
		if not idExists(zettel[:6]+letter):
			os.rename('../Zettel/' + zettel, '../Zettel/' + zettel[:6] + letter + zettel[6:])
			break

def idExists(id):
	allZettelNames = zettelFilter(os.listdir('../../Zettelkasten')) + zettelFilter(os.listdir('../Zettel'))
	for zettel in allZettelNames:
		if zettel.startswith(id):
			return True   #Hier muss glaube ich noch ein False hin...
			break


for zettel in zettelFilter(os.listdir('../Zettel')):
	if re.match('^\d{6}[ ]{1}', zettel):
		makeID(zettel)

print("Done")
