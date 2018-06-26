#!/usr/bin/env
# -*- coding: utf-8 -*-

from tkinter import Label, Frame, Tk, Entry, StringVar, END, IntVar, Scrollbar
from PIL import Image, ImageTk #Hier muss statt PIL noch Pillow rein, weil das neuer ist.
from re import findall, match
from os import listdir, open
from sys import platform
from random import choice


window = Tk(className = "-Zettelkasten-", )
window.attributes("-fullscreen", True)

#### INICIAL VARIABLES ###########################################

if platform.startswith('win32'):
	pathToZettel = "../Zettelkasten/"
	#### Workaround für tkinter (Win) und Tkinter (Mac)
elif platform.startswith('darwin'):
	pathToZettel = "../Zettelkasten/"

miniatureWidth = 150
depth_right_global = 3
depth_left_global = 3

#### BUILDING THE CANVAS ##########################################
def getFollowerIDs(id):
	return findall("\d{6}[a-z]{1}", getFileName(id)[10:])

def idExists(id):
	for filename in listdir(pathToZettel):
		if filename.startswith(id):
			return True
			break
	return False

def getPredecessorIDs(id):
	predecessors = []
	for filename in listdir(pathToZettel):
		if filename[10:].find(id) != -1:
			predecessors.append(filename[:7])
	return predecessors

def getFileName(id): # hier noch bei nichtexistent false zurückgeben. Was mache ich, wenn kein Filename vorhanden? -> Nur auf gesundem Zettelkasten laufen lassen.
	for filename in listdir(pathToZettel):
		if filename.startswith(id):
			return filename
			break

def buildPicThumbforID(id, thumbWidth):
	try:
		path = pathToZettel + getFileName(id)
		with Image.open(path) as img:
			wpercent = (thumbWidth / float(img.size[0]))
			hsize = int((float(img.size[1]) * float(wpercent)))
			return img.resize((thumbWidth, hsize), Image.ANTIALIAS)
	except OSError:
		path = "C:/Users/je6108/Documents/Dissertation_sync/Zettelkastenprogramme/errorImage.png"
		with Image.open(path) as img:
			wpercent = (thumbWidth / float(img.size[0]))
			hsize = int((float(img.size[1]) * float(wpercent)))
			return img.resize((thumbWidth, hsize), Image.ANTIALIAS)
		

def drawZettel_right(id, master):
	image = ImageTk.PhotoImage(buildPicThumbforID(id, miniatureWidth))
	label = Label(master, image=image, textvariable=id, borderwidth=1, relief="solid")
	label.image = image #Workaround, damit Bild nicht vom python-Müllabfuhr gelöscht wird, da die Methode selbst nicht sich um den Erhalt kümmert.
	label.textvariable = id
	label.pack(side="left")

def drawZettel_left(id, master):
	image = ImageTk.PhotoImage(buildPicThumbforID(id, miniatureWidth))
	label = Label(master, image=image, textvariable=id, borderwidth=1, relief="solid")
	label.image = image #Workaround, damit Bild nicht vom python-Müllabfuhr gelöscht wird, da die Methode selbst nicht sich um den Erhalt kümmert.
	label.textvariable = id
	label.pack(side="right")

def drawMiniaturesRight(id, depth_right, master):
	drawZettel_right(id, master)  #Ausgangszettel
	if depth_right >= 1:
		f_vertical = Frame(master, padx=5, pady=8)
		f_vertical.pack()
		for followerID in getFollowerIDs(id):
			f_horizontal = Frame(f_vertical)
			f_horizontal.pack(anchor="w")
			drawMiniaturesRight(followerID, depth_right - 1, f_horizontal)

def drawMiniaturesLeft(id, depth_left, master):
	drawZettel_left(id, master)  #Erster linker Zettel
	if depth_left >= 1:
		f_vertical = Frame(master, padx=5, pady=8)
		f_vertical.pack()
		for predecessorID in getPredecessorIDs(id):
			f_horizontal = Frame(f_vertical, borderwidth=1)
			f_horizontal.pack(anchor="e")
			drawMiniaturesLeft(predecessorID, depth_left-1, f_horizontal)

def buildCanvas(id):
	destroyChildren(zettelFrame_left)
	destroyChildren(zettelFrame_center)
	destroyChildren(zettelFrame_right)
	destroyLargeMiniature(window)

	global idFrame
	idFrame = Frame(zettelFrame_center, borderwidth=1)
	idFrame.pack(side="left")

	global idEntryField
	idEntryField = Entry(idFrame, width = 10, bg="#03A89E", font=("Arial", 11))
	idEntryField.pack(anchor="w")
	idEntryField.insert(0, id_global)
	idEntryField.bind('<KeyPress-Return>', canvasReloadWithID)

	image = ImageTk.PhotoImage(buildPicThumbforID(id, miniatureWidth))
	label = Label(idFrame, image=image, textvariable=id, borderwidth=1, relief="solid")
	label.image = image #Workaround, damit Bild nicht vom python-Müllabfuhr gelöscht wird, da die Methode selbst nicht sich um den Erhalt kümmert.
	label.textvariable = id
	label.pack(anchor="w")

	global depth_left_global
	global depth_right_global

	if depth_left_global >= 1:
		for predecessorID in getPredecessorIDs(id):
			f_horizontal = Frame(zettelFrame_left)
			f_horizontal.pack(anchor="e")
			drawMiniaturesLeft(predecessorID, depth_left_global-1, f_horizontal)

	if depth_right_global >= 1:
		for followerID in getFollowerIDs(id):
			f_horizontal = Frame(zettelFrame_right)
			f_horizontal.pack(anchor="w")
			drawMiniaturesRight(followerID, depth_right_global-1, f_horizontal)

	idEntryField.focus()

##### INTERACTION FUNCTIONS ##################################################
def enlargeMiniatur(widgetObject):
	id = widgetObject.widget["textvariable"]
	image = ImageTk.PhotoImage(buildPicThumbforID(id,800))
	global enlargedMiniatureWidget
	enlargedMiniatureWidget = Label(window, image=image, textvariable=id, borderwidth=1, relief="solid")
	enlargedMiniatureWidget.image = image #Workaround, damit Bild nicht vom python-Müllabfuhr gelöscht wird, da die Methode selbst nicht sich um den Erhalt kümmert.
	enlargedMiniatureWidget.textvariable = id
	enlargedMiniatureWidget.place(x=40, y=40)
	enlargedMiniatureWidget.lift()

def destroyLargeMiniature(widgetObject):
	try:
		enlargedMiniatureWidget.destroy()
	except NameError:
		pass

def canvasReloadWithID(widgetObject):
	id = idEntryField.get()
	if match("^\d{6}[a-z]{1}", id) and match("\d{6}[a-z]{1}$", id) and idExists(id):
		global id_global
		id_global = idEntryField.get()
		buildCanvas(id_global)

def canvasClickReload(widgetObject):  #Fehlerhaft! Hier werden nicht die richtigen Kinder aufgezeigt. Es fehlt eins!
	buildCanvas(widgetObject.widget.textvariable)
	global id_global
	id_global = widgetObject.widget.textvariable
	idEntryField.delete(0, END)
	idEntryField.insert(0, id_global)

def destroyChildren(widgetObject):
	for child in widgetObject.winfo_children():
		child.destroy()

def changeMiniatureWidthSize(widgetObject):
	global id_global
	global miniatureWidth
	miniatureWidth = int(entryMiniatureWidth.get())
	buildCanvas(id_global)

def changeDepth(widgetObject):
	global depth_right_global, depth_left_global, id_global
	depth_left_global = int(entryLeftDepth.get())   #Hier nur einfügen, wenn auch wirklich int
	depth_right_global = int(entryRightDepth.get()) 	#Hier nur einfügen, wenn auch wirklich int
	buildCanvas(id_global)

#################################################
#### User Interface #############################
#################################################

###Main Frames
canvasFrame = Frame(window)
canvasFrame.pack(side="top", anchor="center", pady=20)

zettelFrame_left = Frame(canvasFrame)
zettelFrame_left.pack(side="left")
zettelFrame_center = Frame(canvasFrame)
zettelFrame_center.pack(side="left", padx=50)
zettelFrame_right = Frame(canvasFrame)
zettelFrame_right.pack(side="left")

mainFrame_Menu = Frame(window)
mainFrame_Menu.pack(side="bottom", pady=20)
#showMenu(mainFrame_Menu)

### Menu
leftMenuFrame = Frame(mainFrame_Menu)
leftMenuFrame.pack(side="left")

centerMenuFrame = Frame(mainFrame_Menu)
centerMenuFrame.pack(side="left")

rightMenuFrame = Frame(mainFrame_Menu)
rightMenuFrame.pack(side="left")

entryLeftDepth = Entry(leftMenuFrame, width=3)
entryLeftDepth.pack(side="right")
entryLeftDepth.insert(0, depth_left_global)

entryRightDepth = Entry(rightMenuFrame, width = 3)
entryRightDepth.pack(side="left")
entryRightDepth.insert(0, depth_right_global)

entryMiniatureWidth = Entry(centerMenuFrame, width=5)
entryMiniatureWidth.pack(padx=miniatureWidth/2-5)
entryMiniatureWidth.insert(0, miniatureWidth )

##################################################

canvasFrame.bind_class("Label", "<Button-3>", canvasClickReload) # Rechtsklick bei Windows
canvasFrame.bind_class("Label", "<Button-2>", canvasClickReload) # Rechtsklick beim Mac
canvasFrame.bind_class("Label", "<Button-1>", enlargeMiniatur)
canvasFrame.bind_class("Label", "<ButtonRelease-1>", destroyLargeMiniature)

entryMiniatureWidth.bind('<KeyPress-Return>', changeMiniatureWidthSize)
entryLeftDepth.bind('<KeyPress-Return>', changeDepth)
entryRightDepth.bind('<KeyPress-Return>', changeDepth)

#id_global = "170118b"  #ID für Zettelkastenprogramme/Zetteltest
id_global = choice(listdir(pathToZettel))[:7]  #Starte mit zufälligem Zettel im Zettelkasten

buildCanvas(id_global)

window.mainloop()
print('Done')
