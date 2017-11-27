# zettelkasten

The following project proposes a personal knowledge management system that is robust, cheap and build to last a lifetime.

## Motivation

We live in a knowledge-based society (German: "Wissensgesellschaft"). There are projects like Wikipedia, where collective knowledge about the world is processed and stored. However what about personal knowledge? Is there a way to equally enrich the way we process and store **personal knowledge** like the project Wikipedia does for collective knowledge?

This project might be the answer. Go to the Wiki tab (LINK) in order to learn more about it.

## Supporting python programs: Philosophy

All the following programs are short and simple programs. Actually you do not need them in order to use this proposed personal knowledge management system. The philosophy behind that is, that in order to use a personal knowledge management system that lasts a lifetime, you should be able to build it yourself. You should not depend on other's programs in order to use your personal knowledge system.

If you do not have programming skills, I recommend you to learn some in order to understand what these little programs do. Order for example the book Python Kompakt (LINK) (read chapter 1 and 2) or go to https://www.codecademy.com/learn/learn-python (10 hours).

All programs run with python3. You can install it here: https://www.python.org/downloads/. After the installation you can run the programs by either double clicking on them. Or navigate in the programms "terminal" (Mac or Linux) or "cmd" (Windows) to the folder of the programs and type ```python NAMEOFTHEPROGRAM.py``` or ```py NAMEOFTHEPROGRAM.py``` (`.py` stands for python-files).

## Supporting python programs: Use

The following programs make it easier to work with the personal knowledge management system called "zettelkasten":

* Check the zettelkasten's integrity (`checkZettelkasten.py`). This program operates read only on the files in the zettelkasten. It checks, if your zettelkasten is consistent. The criteria are if:

  * all IDs are in the correct format and unique
  * all links point to an existing ID and
  * and links have the correct format (Bild)

Screenshots of health check zettelkasten.

* Assign correct IDs to all prenamed files in the folder "/zettel" (`buildIDs.py`). This program automatically assigns a correct small letter to a zettel ID.

Screenshots of program with zettelnames without letter and afterwards with letter.

* Shows how a certain zettel is interlinked within the zettelkasten (`overview.py`). This program shows how a certain zettel interlinks with other zettel in the zettelkasten. Program features are:

  * If you position the cursor on a zettel and press down the left mouse button, the zettel will enlarge in order to read it better.

  * If you right click on a certain zettel, the whole network will rebuild around this specific zettel.

  * You can write a certain zettel ID in the field and hit enter. The network will be then rebuild around this specific zettel.

This program is only useful, if you have more than about 1000 zettel in your zettelkasten. It is for advanced use and a more complicated program to understand.