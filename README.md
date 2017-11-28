# zettelkasten

The following project proposes a personal knowledge management system that is robust, cheap and built to last a lifetime.

## Motivation

We live in a knowledge-based society (German: "Wissensgesellschaft"). There are projects like Wikipedia, where collective knowledge about the world is processed and stored. However what about personal knowledge? Is there a way to equally enrich the way we process and store **personal knowledge** like the project Wikipedia does for collective knowledge?

This project might be the answer. Go to the [Wiki tab](https://github.com/crelder/zettelkasten/wiki) in order to learn more about it.

## Supporting python programs: Philosophy

All the following programs are short and simple programs. Actually you do not need them in order to use this proposed personal knowledge management system. The philosophy behind that is, that in order to use a personal knowledge management system that lasts a lifetime, you should be able to build it yourself. You should not depend on other's programs in order to use your personal knowledge system.

If you do not have programming skills, I recommend you to learn some in order to understand what these little programs do. Order for example the book [Python Ge-Packt](https://www.amazon.de/Python-Ge-Packt-mitp-Michael-Weigend/dp/3826687264/ref=sr_1_fkmr0_1?s=books&ie=UTF8&qid=1511876890&sr=1-1-fkmr0&keywords=python+gepackt+6.+Auflage) and read the first chapters or take a free [python course at codecademy](https://www.codecademy.com/learn/learn-python) (it takes a few hours for this course).

All programs run with [python3](https://de.wikipedia.org/wiki/Python_(Programmiersprache)). You can download and install the programming language [here](https://www.python.org/downloads/). After the installation you can run the programs by either double clicking on them, or navigating in the programms "terminal" (Mac or Linux) or "cmd" (Windows) to the folder of the programs and type ```python NAMEOFTHEPROGRAM.py``` or ```py NAMEOFTHEPROGRAM.py``` (`.py` stands for python-files).

## Supporting python programs: Use

The following programs make it easier to work with the personal knowledge management system called "zettelkasten":


### checkZettelkasten.py

Check the zettelkasten's integrity (`checkZettelkasten.py`). This program operates read only on the files in the zettelkasten. It checks, if your zettelkasten is consistent. The criteria are:

  * all IDs are in the correct format and unique
  * links have the correct format
  * all links point to an existing ID

![If your zettelkasten is damaged, it will look like this.](https://github.com/crelder/zettelkasten/blob/master/pictures/checkZettelkasten-2.PNG "Results of checkZettelkasten.py")

![If your zettelkasten is alright, it will look like this.](https://github.com/crelder/zettelkasten/blob/master/pictures/checkZettelkasten.PNG "Results of checkZettelkasten.py")


### buildIDs.py

Assign correct IDs to all files in the folder "/zettel" (`buildIDs.py`). This program automatically assigns a correct small letter to a zettel ID.

![After you renamed the png file names it looks like this.](https://github.com/crelder/zettelkasten/blob/master/pictures/zettel-7.PNG "Results of the program buildIDs.py")

![The program buildIDs.py then automatically creates unique IDs.](https://github.com/crelder/zettelkasten/blob/master/pictures/zettel-8.PNG "Results of the program buildIDs.py")


### link_overview.py

Shows how a certain zettel interlinks with other zettel in the zettelkasten (`link_overview.py`). 

![The program link_overview.py shows how the zettel are interlinked.](https://github.com/crelder/zettelkasten/blob/master/pictures/search-linkeOverview.PNG "Shows how the zettel are interlinked.")

Program features are:

* If you position the cursor on a zettel and press down the left mouse button, the zettel will enlarge in order to read it better.

* If you right click on a certain zettel, the whole network will rebuild around this specific zettel.

* You can write a certain zettel ID in the field and hit enter. The network will be then rebuild around this specific zettel.

This program is only useful, if you have more than about 1000 zettel in your zettelkasten. It is for advanced use and a more complicated program to understand. Note: if you use a Mac you have to change in line 4 "tkinter" to "Tkinter" (for now this is the workaround).


### backup.py

Generate a list with the filename (metadata) of every zettel and save it in the folder "/Backups" (`backup.py`). You can print this list every now and then and store it in the physical zettelkasten as a backup in case your computer crashes. From this list and the physical zettel you can always completly recover your digital zettelkasten. 