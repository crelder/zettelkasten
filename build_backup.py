#!/usr/bin/env
# -*- coding: utf-8 -*-

import os, re, time


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

filename = time.strftime("%y%m%d_%H-%M-%S", time.localtime()) + "_Backup_Zettelkasten_Metadaten.txt"
print(filename)

#backup = open('backup_metadaten.txt', 'w')
backup = open('Backups/' + filename, 'w')
backup.write(time.strftime("%d.%m.%Y -- %H:%M:%S", time.localtime()) + '\n' + '===============' + '\n' + '\n'.join(zettelFilter(zettelkastenDirectory)))
backup.close()

input("")