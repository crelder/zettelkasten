# zettelkasten
The following project proposes a personal knowledge management system which is robust, cheap and build to last a lifetime.

Go to the Wiki tab (LINK) in order to learn more about it.

## Supporting python programs
All programs have low complexity. The philosophy is that in order to use a personal knowledge management system that lasts a life time, you should be able to build it your self. You do not need these programs in order to use the zettelkasten. If you do not have programming skills, I recommend you order for example the book Python Kompakt (LINK) and learn the little programs and what they do.

All programs run with python3. You can install it here: https://www.python.org/downloads/. After the installation you can run the programs by either double clicking on them. Or navigate in the terminal (Mac or Linux) or cmd (Windows) to the folder of the programs and type 
    ```python NAMEOFTHEPROGRAM.py```
or 
    ```py NAMEOFTHEPROGRAM.py```

".py“ stands for python-files.

The function of the programs are
* check zettelkasten integrity (zettelkastenhealth.py)
* assign correct ID to every correctly named file in the folder zettel (buildIDs.py)
* show how a certain zettel is interlinked within the zettelkasten (overview.py)

* Healthcheck (checkZettelkasten.py): it operates read only on the files in the zettelkasten. It checks, if your zettelkasten is consistent. The criteria are: 1. are all IDs in the correct format and unique? 2. do all links point to an existing ID? 3. Do all links have the correct format? (Bild)  
Screenshots of health check zettelkasten.
* buildIDs.py: it automatically assigns a correct small letter to an zettel ID.  
Screenshots of program with zettelnames without letter and afterwards with letter.
* link overview.py: this program servesProgramm-Features: Solange ich mit der linken Maustaste auf einem Zettel gedrückt bleibe, wird der Zettel vergrößert angezeigt. Bei rechtem Mausklick auf einen Zettel baut er die Ansicht erneut um diesen Zettel auf. In das Feld kann ich eine ID eingeben. Enter. Ist die ID vorhanden, so baut sich um den Zettel mit dieser ID der Zettelkontext auf.
Unteres Menü - Einstellmöglichkeiten Linke Zettelpfad-Tiefe Breite der Zettelminiaturen Rechte Zettelpfad-Tiefe
Thematischen Zettelzugang und Zugang über die Gedanken-Quellen finde ich über die normale Ordnersuche im Explorer.
See testset, wo Testdaten so prepariert sind, sodass man die Wirkung der Programme erkennen kann.