# AlphabotDB
Program to make a pc and an alphabot communicate.
The clien sends commands to the server that will execute them.
There are some predetermined movement sequences which are saved in an sqlite database on the robot.

This is the project scheme:
![Immagine nel web](scheme.png "schema progetto")

The db structure is:

|name|command|
|:-|:-:|
|slalom|command1_duration;command2_duration;...|
|...|...|


Nicolo' Cora - Andrea Tomatis
