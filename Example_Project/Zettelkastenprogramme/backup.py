#!/usr/bin/env
# -*- coding: utf-8 -*-

# This program creates a text-file in the folder "/backups" which contains all the names of the zettel in the folder zettelkasten. You can use this text-file as a backup for the meta-data of all the zettel. You can also print the text-file in order to increase security.

import os, re, time

# Location of Zettelkasten-director saved in a variable "zettelkastenDirectory"
zettelkastenDirectory = os.listdir('../Zettelkasten')  

# A function that filters filenames which end in ".png" and return them in an array "filteredFilenames".
# E.g. hidden files will not show up in the backup-file.
def zettelFilter(allFilenames):
    filteredFilenames = []
    for fileName in sorted(allFilenames):
        if fileName.endswith(".png"):
            # :len(fileName)-4 - Save the filename without the filetype at the end.
            filteredFilenames.append(fileName[:len(fileName)-4]) 
    return filteredFilenames 

# Define Filename of the Backup-File
filename = time.strftime("%y%m%d_%H-%M-%S", time.localtime()) + "_Backup_Zettelkasten_Metadaten.txt"

# Create a file with the defined filename
backup = open('Backups/' + filename, 'w')

# Write a header with the actual time and then list all filenames (one in each line)
backup.write(time.strftime("%d.%m.%Y -- %H:%M:%S", time.localtime()) + '\n' + '===============' + '\n' + '\n'.join(zettelFilter(zettelkastenDirectory)))
backup.close()