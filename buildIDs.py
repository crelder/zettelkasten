#!/usr/bin/env
# -*- coding: utf-8 -*-

import os, re, string

# A function that filters filenames which end in ".png" and return them in an array "filteredFilenames".
# E.g. hidden files will not show up in the backup-file.
def zettelFilter(allFilenames):
    filteredFilenames = []
    for fileName in sorted(allFilenames):
        if fileName.endswith(".png"):
            filteredFilenames.append(fileName)
    return filteredFilenames


# This function checks, if a certain id exists in either the Zettelkasten-Directory ('../../Zettelkasten') 
# or the directory, where new zettel get parked ('../Zettel'), until a filename is assigned to them.
def idExists(id):
	allZettelNames = zettelFilter(os.listdir('../../Zettelkasten')) + zettelFilter(os.listdir('../Zettel'))
	for zettel in allZettelNames:
		if zettel.startswith(id):
			return True
			break

# This function creates a unique ID by adding a small letter to the 6 digits at the beginning of the filename.
def makeID(zettel):
	# Go through all small letters
	for letter in string.ascii_lowercase:
		# If the combination 6 digits (e.g. '171103') plus a certain letter (e.g. 'a') does not already exist, 
		# then assign this unique ID to the filename e.g. 171103a
		if not idExists(zettel[:6]+letter):
			os.rename('../Zettel/' + zettel, '../Zettel/' + zettel[:6] + letter + zettel[6:])
			break

# Go through all the zettel in the directory 'Zettel' and create a unique ID for each zettel.
for zettel in zettelFilter(os.listdir('../Zettel')):
	if re.match('^\d{6}[ ]{1}', zettel):
		makeID(zettel)
