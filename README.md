# zettelkasten
The following project proposes a personal knowledge management system which is robust, cheap and build to last a lifetime.

## Solve the problem "What to do with a good thought?"
Grundsätzlicher Nutzen eines Systems für eigene oder fremde Gedanken
- Wiederfinden von Gedanken (Annahme: Kenntnis der Existenz des Gedankens)
- Aufzeigen relevanter Gedanken in gewissem Kontext (Annahme: Unkenntnis der Existenz des Gedankens)

## Requirements for a system for own (or others) thoughts
- Robust 				        (Voraussetzung für Nutzung)
- Langlebig (z.B. auf Lebenszeit ausgelegt) (Voraussetzung für Nutzung)
- Input ≠ „schlechter Input“		        (Voraussetzung für Nutzung)
- System generiert einen Output und dadurch einen Nutzen für mich, d.h. ich nutze es. (wichtig, da Inputerzeugung ressourcenaufwendig)

## How this propsed system functions
Format der Zettelnamen ist immer
[ID] - [Schlagwörter] - [Quelle] - [Links]

- ID: Pflicht: Datum + Kleinbuchstabe
- Schlagwörter: Pflicht: Schlagwörter mit Komma getrennt
- Quelle: Optional: Nachname + vierstelliges Jahresdatum (Welter2011) sind Buchquellen, welche auch in meiner Bibtex file sein müssen. Ansonsten steht so etwas wie “Gespräch Sascha” oder “Museumsbesuch Hamburg 2017” dort. Die Quelle dienst zum einen, um Gedanken wiederzufinden (“Als ich da und da war, habe ich doch was gedacht…”) und später zum korrekten zitieren mit Hilfe der Bibtex file.
- Links: Optional: IDs mit Komma getrennt

Beispiele:
- 170105a - Entrepreneurshipforschung, Kleinunternehmen, neuartige Unternehmen - Bögenhold2016.png
- 170115r - Wirtschaftswachstum, Wohlstand, Gesellschaftskonflikte - 170128h, 170303d.png

----------

- Für eine Sprache entscheiden
- Für ein Format entscheiden
- Nur Zettel (Filter für vorschnelle „Gedanken“, bewusster Filter für die hohe Quantität gegenüber Qualität)

See folder with example data.

You do not need these programms 

Screenshots of files in the folder with preview.
Screenshots of program with zettelnames without letter and afterwards with letter.
Screenshots of health check zettelkasten.


## Why it functions this way and discussion of fullfilment of the requirements
Virtuelle Zettelkasten nicht so gut funktioniert.
Durch schreiben wird es klarer - man ist gezwungen, es selbst zu schreiben
Man kann leicht Skizzen, Pfeile, etc. hinzufügen - kann Gedanken eher so niederschreiben, wie sie im eigenen Gehirn repräsentiert sind.

Software has the problem that it lives not very long. You do not need a single program to run the zettelkasten. You can just use the folder and search feature of a MAC, Windows or Linux operating system. If this fails you can just use your printed file list with the slips of paper (Zettel).

## What do the programs related to the zettelkasten do?
All programms run with pyhton3. You can install it here: https://www.python.org/downloads/

1. Health check (checkZettelkasten.py): nur read auf die Dateien im Zettelkasten. Prüft die Gesamtkonistenz des Zettelkastens auf mehrere Kriterien.

2. Gephi Format File creater (buildGraphFile.py) (gestern noch eine Nachtsession eingelegt bis 3 Uhr - Du siehst, das wird mit dem Programmiernerd noch was…)

3. buildIDs.py: Automatische Vergabe für IDs im Ordner “Zettel” (das ist der Ordner, wo abfotografierte Zettel hinkommen, um dann noch den korrekten Dateinamen zu bekommen: Schlagwörter, Quelle, Links
Alle Zettel im Ordner “Zettel” welche mit sechs Zahlen begingen, gefolgt von einem Leerzeichen, bekommen noch zusätzlich einen Buchstaben angehängt, welcher weder im Ordner “Zettel” noch im Ordern “Zettelkasten” vorhanden ist.
Ich kann noch nicht wirklich einen Nutzen aus der Graphdarstellung ziehen. Zu wenige Links und die Darstellung ist noch scheiße. 

4. Overview: Programm-Features:
Solange ich mit der linken Maustaste auf einem Zettel gedrückt bleibe, wird der Zettel vergrößert angezeigt.
Bei rechtem Mausklick auf einen Zettel baut er die Ansicht erneut um diesen Zettel auf.
In das Feld kann ich eine ID eingeben. Enter. Ist die ID vorhanden, so baut sich um den Zettel mit dieser ID der Zettelkontext auf.

Unteres Menü - Einstellmöglichkeiten
Linke Zettelpfad-Tiefe
Breite der Zettelminiaturen
Rechte Zettelpfad-Tiefe

Thematischen Zettelzugang und Zugang über die Gedanken-Quellen finde ich über die normale Ordnersuche im Explorer.

See testset, wo Testdaten so prepariert sind, sodass man die Wirkung der Programme erkennen kann.

## Limits of the zettelkasten
If you have to deliver a concrete project with a deadline (e.g. thesis, dissertation, book) then maybe it is better to fill a file directly with your thoughts.

## Source of inspiration
The Zettelkasten is inspired by the function of Video wissenschaftliche Auswertung. Zeitungsartikel. Youtube Video Luhmann.

