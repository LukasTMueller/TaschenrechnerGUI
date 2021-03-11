"""
Author: Lukas Müller
Date: 11.12.2020
"""

from tkinter import *


# ------- Globale Variablen zur Datenverwaltung -------

eingabe = ''  # aktuelle eingabe als string
ergebnis = 0  # aktuelle eingabe als int/ float
dotCounter = 0  # counter ob ein punkt eingegeben wurde -> im moment nicht genutzt
zeichenCounter = 0  # counter ob ein zeichen (rechenzeichen) eingegeben wurde -> 0 = Nein, 1 = Ja
ergebnisHilfsVar = 0  # hilfsvariable die den wert des zwischenergebnis annimmt -> beim ersten rechenzeichen den wert
# von "ergebnis", im verlauf das zwischenergebnis
eingabeHilfsVar = ''  # übernimmt den aktuellen string von "eingabe", sobald ein rechenzeichen eingegeben wurde -> um
# das letzte rechenzeichen später aufzurufen
zeichenListe = ['+', '-', '*', '/']  # liste mit rechenzeichen zum überprüfen ob eins eingegeben wurde


# ---------------- Funktionen ----------------------


def entry():  # Funktion um die eingabe zu bearbeiten
    global eingabe, ergebnis, eingabeHilfsVar, ergebnisHilfsVar, zeichenCounter, dotCounter

    zahl = number.get()
    eingabe = eingabe + zahl
    if eingabe[len(eingabe) - 1] in zeichenListe:  # wurde ein operator eingegeben oder nicht? -> folge für ja
        if zeichenCounter == 0:  # der erste operator, welcher eingegeben wurde
            ergebnisHilfsVar = ergebnis
            eingabeHilfsVar = eingabeHilfsVar + eingabe
            labelRechnung.config(text=eingabeHilfsVar)
            eingabe = ''
            ergebnis = 0
            zeichenCounter = 1
            dotCounter = 0
            buttonDot.config(state=NORMAL)
        else:
            if zeichenCounter != 0:  # es wurde schon min. einer vorher verwendet
                rechnung()

    else:  # es wurde eine zahl eingegeben
        if eingabe[len(eingabe) - 1] not in zeichenListe:
            if zahl == '.':  # war die eingabe ein "."
                dotCounter = 1
            if dotCounter == 1:  # Ja -> eingabe wird in float umgewandelt
                ergebnis = float(eingabe)
                buttonDot.config(state=DISABLED)
            if dotCounter == 0:  # Nein -> eingabe bleibt int
                ergebnis = int(eingabe)
            labelErgebnis.config(text=ergebnis)

    buttonClean()


def rechnung():  # funktion welche das zwischenergebnis berechnet -> wird verwendet ab eingabe des zweiten operators
    global eingabe, ergebnis, eingabeHilfsVar, ergebnisHilfsVar, dotCounter

    try:
        if eingabeHilfsVar[len(eingabeHilfsVar) - 1] == '+':  # verwendeter operator war ein "+"
            ergebnisHilfsVar = ergebnisHilfsVar + ergebnis
            labelErgebnis.config(text=ergebnisHilfsVar)
            eingabeHilfsVar = eingabeHilfsVar + eingabe
            labelRechnung.config(text=eingabeHilfsVar)

        else:
            if eingabeHilfsVar[len(eingabeHilfsVar) - 1] == '-':  # verwendeter operator war ein "-"
                ergebnisHilfsVar = ergebnisHilfsVar - ergebnis
                labelErgebnis.config(text=ergebnisHilfsVar)
                eingabeHilfsVar = eingabeHilfsVar + eingabe
                labelRechnung.config(text=eingabeHilfsVar)

            else:
                if eingabeHilfsVar[len(eingabeHilfsVar) - 1] == '*':  # verwendeter operator war ein "*"
                    ergebnisHilfsVar = ergebnisHilfsVar * ergebnis
                    labelErgebnis.config(text=ergebnisHilfsVar)
                    eingabeHilfsVar = eingabeHilfsVar + eingabe
                    labelRechnung.config(text=eingabeHilfsVar)

                else:
                    if eingabeHilfsVar[len(eingabeHilfsVar) - 1] == '/':  # verwendeter operator war ein "/"
                        ergebnisHilfsVar = ergebnisHilfsVar / ergebnis
                        labelErgebnis.config(text=ergebnisHilfsVar)
                        eingabeHilfsVar = eingabeHilfsVar + eingabe
                        labelRechnung.config(text=eingabeHilfsVar)

    except:
        pass

    eingabe = ''
    ergebnis = 0
    dotCounter = 0
    buttonDot.config(state=NORMAL)

    buttonClean()


def output():  # Funktion sobald "=" gedrückt wurde
    global eingabe, ergebnis, eingabeHilfsVar, ergebnisHilfsVar, zeichenCounter

    try:
        if eingabeHilfsVar[len(eingabeHilfsVar) - 1] == '+':  # verwendeter operator war ein "+"
            ergebnisHilfsVar = ergebnisHilfsVar + ergebnis
            labelErgebnis.config(text=ergebnisHilfsVar)
            eingabeHilfsVar = eingabeHilfsVar + eingabe + '='
            labelRechnung.config(text=eingabeHilfsVar)

        if eingabeHilfsVar[len(eingabeHilfsVar) - 1] == '-':  # verwendeter operator war ein "-"
            ergebnisHilfsVar = ergebnisHilfsVar - ergebnis
            labelErgebnis.config(text=ergebnisHilfsVar)
            eingabeHilfsVar = eingabeHilfsVar + eingabe + '='
            labelRechnung.config(text=eingabeHilfsVar)

        if eingabeHilfsVar[len(eingabeHilfsVar) - 1] == '*':  # verwendeter operator war ein "*"
            ergebnisHilfsVar = ergebnisHilfsVar * ergebnis
            labelErgebnis.config(text=ergebnisHilfsVar)
            eingabeHilfsVar = eingabeHilfsVar + eingabe + '='
            labelRechnung.config(text=eingabeHilfsVar)

        if eingabeHilfsVar[len(eingabeHilfsVar) - 1] == '/':  # verwendeter operator war ein "/"
            ergebnisHilfsVar = ergebnisHilfsVar / ergebnis
            labelErgebnis.config(text=ergebnisHilfsVar)
            eingabeHilfsVar = eingabeHilfsVar + eingabe + '='
            labelRechnung.config(text=eingabeHilfsVar)

    except:
        pass

    buttonClean()


def clearEntry():  # Funktion um die gesamte eingabe zu löschen -> variablen für die eingabe zurücksetzen
    global ergebnis, eingabe, dotCounter

    ergebnis = 0
    eingabe = ''
    dotCounter = 0
    buttonDot.config(state=NORMAL)
    labelErgebnis.config(text=ergebnis)


def clearAll():  # funktion um die gesamte rechnung zu löschen -> alle variablen zurück auf ihre startwerte
    global ergebnis, eingabe, ergebnisHilfsVar, eingabeHilfsVar, dotCounter, zeichenCounter

    ergebnis = 0
    ergebnisHilfsVar = 0
    eingabe = ''
    eingabeHilfsVar = ''
    dotCounter = 0
    zeichenCounter = 0
    buttonDot.config(state=NORMAL)
    labelErgebnis.config(text=ergebnis)
    labelRechnung.config(text=eingabeHilfsVar)


def backSpace():  # funktion um das letzte eingegebene zeichen rückgängig zu machen -> operatoren sind NICHT betroffen
    global ergebnis, eingabe, dotCounter

    if len(eingabe) > 1:
        if dotCounter == 1:
            dotPosi = eingabe.endswith(".")
            if dotPosi:
                eingabe = eingabe[:-1]
                ergebnis = int(eingabe)
                dotCounter = 0
                buttonDot.config(state=NORMAL)

            else:
                if not dotPosi:
                    eingabe = eingabe[:-1]
                    ergebnis = float(eingabe)
        if dotCounter == 0:
            eingabe = eingabe[:-1]
            ergebnis = int(eingabe)

    else:
        if len(eingabe) == 1:
            eingabe = ''
            ergebnis = 0
            dotCounter = 0
            buttonDot.config(state=NORMAL)

    labelErgebnis.config(text=ergebnis)


def signChange():  # wechsel des vorzeichens -> "+" zu "-" und "-" zu "+"
    global ergebnis, eingabe

    ergebnis = ergebnis * -1
    minusPosi = eingabe.endswith("-", 0, 1)
    if ergebnis != 0:
        if minusPosi:
            eingabe = eingabe[1:]

        if not minusPosi:
            eingabe = "-" + eingabe
        labelErgebnis.config(text=ergebnis)

    else:
        if ergebnis == 0:
            pass


def buttonClean():  # funktion welche alle radiobuttons wieder deaktiviert: nach jeder eingabe verwendet
    radioButtons = [buttonNumber0, buttonNumber1, buttonNumber2, buttonNumber3, buttonNumber4, buttonNumber5,
                    buttonNumber6, buttonNumber7, buttonNumber8, buttonNumber9, buttonDot, buttonDivision, buttonPlus,
                    buttonMinus, buttonMultiplication]
    for i in range(15):
        radioButtons[i].deselect()


# ------------------ Erstellen des Fensters -----------------

ProgramWindow = Tk()
ProgramWindow.title('Rechner')
ProgramWindow.geometry('275x345')

# Frame des Displays: labelRechnung zeigt den Rechenweg, labelErgebnis zeigt das zwischen/endergebnis
frameDisplay = Frame(master=ProgramWindow)
frameDisplay.place(x=5, y=5, width=265, height=95)
labelRechnung = Label(master=frameDisplay, bg='#E6E6E6', text=eingabeHilfsVar, anchor='e', font='Arial 14')
labelRechnung.place(x=5, y=5, width=255, height=40)
labelErgebnis = Label(master=frameDisplay, bg='#E6E6E6', text=ergebnis, anchor='e', font='Arial 14')
labelErgebnis.place(x=5, y=50, width=255, height=40)

# Frame für den Tastenblock (Buttons sind von oben links nach unten rechts erstellt)
frameTasten = Frame(master=ProgramWindow)
frameTasten.place(x=5, y=110, width=265, height=230)
number = StringVar()

# reihe 1
buttonClearEntry = Button(master=frameTasten, bg='lightgrey', bd=1, text='CE', font='Arial 14', command=clearEntry)
buttonClearEntry.place(x=5, y=5, width=60, height=40)
buttonClearAll = Button(master=frameTasten, bg='lightgrey', bd=1, text='C', font='Arial 14', command=clearAll)
buttonClearAll.place(x=70, y=5, width=60, height=40)
buttonBackspace = Button(master=frameTasten, bg='lightgrey', bd=1, text='<-', font='Arial 14', command=backSpace)
buttonBackspace.place(x=135, y=5, width=60, height=40)
buttonDivision = Radiobutton(master=frameTasten, bg='lightgrey', bd=1, indicator=0, text='/', value='/',
                             variable=number, font='Arial 14', command=entry)
buttonDivision.place(x=200, y=5, width=60, height=40)

# reihe 2
buttonNumber7 = Radiobutton(master=frameTasten, bg='#F2F2F2', bd=1, indicator=0, text='7', value=7, variable=number,
                            font='Arial 14', command=entry)
buttonNumber7.place(x=5, y=50, width=60, height=40)
buttonNumber8 = Radiobutton(master=frameTasten, bg='#F2F2F2', bd=1, indicator=0, text='8', value=8, variable=number,
                            font='Arial 14', command=entry)
buttonNumber8.place(x=70, y=50, width=60, height=40)
buttonNumber9 = Radiobutton(master=frameTasten, bg='#F2F2F2', bd=1, indicator=0, text='9', value=9, variable=number,
                            font='Arial 14', command=entry)
buttonNumber9.place(x=135, y=50, width=60, height=40)
buttonMultiplication = Radiobutton(master=frameTasten, bd=1, bg='lightgrey', indicator=0, text='x', value='*',
                                   variable=number, font='Arial 14', command=entry)
buttonMultiplication.place(x=200, y=50, width=60, height=40)

# reihe 3
buttonNumber4 = Radiobutton(master=frameTasten, bg='#F2F2F2', bd=1, indicator=0, text='4', value=4, variable=number,
                            font='Arial 14', command=entry)
buttonNumber4.place(x=5, y=95, width=60, height=40)
buttonNumber5 = Radiobutton(master=frameTasten, bg='#F2F2F2', bd=1, indicator=0, text='5', value=5, variable=number,
                            font='Arial 14', command=entry)
buttonNumber5.place(x=70, y=95, width=60, height=40)
buttonNumber6 = Radiobutton(master=frameTasten, bg='#F2F2F2', bd=1, indicator=0, text='6', value=6, variable=number,
                            font='Arial 14', command=entry)
buttonNumber6.place(x=135, y=95, width=60, height=40)
buttonMinus = Radiobutton(master=frameTasten, bg='lightgrey', bd=1, indicator=0, text='-', value='-', variable=number,
                          font='Arial 14', command=entry)
buttonMinus.place(x=200, y=95, width=60, height=40)

# reihe 4
buttonNumber1 = Radiobutton(master=frameTasten, bg='#F2F2F2', bd=1, indicator=0, text='1', value=1, variable=number,
                            font='Arial 14', command=entry)
buttonNumber1.place(x=5, y=140, width=60, height=40)
buttonNumber2 = Radiobutton(master=frameTasten, bg='#F2F2F2', bd=1, indicator=0, text='2', value=2, variable=number,
                            font='Arial 14', command=entry)
buttonNumber2.place(x=70, y=140, width=60, height=40)
buttonNumber3 = Radiobutton(master=frameTasten, bg='#F2F2F2', bd=1, indicator=0, text='3', value=3, variable=number,
                            font='Arial 14', command=entry)
buttonNumber3.place(x=135, y=140, width=60, height=40)
buttonPlus = Radiobutton(master=frameTasten, bg='lightgrey', bd=1, indicator=0, text='+', value='+', variable=number,
                         font='Arial 14', command=entry)
buttonPlus.place(x=200, y=140, width=60, height=40)

# reihe 5
buttonPosNeg = Button(master=frameTasten, bg='#D8D8D8', bd=1, text='+/-', font='Arial 14', command=signChange)
buttonPosNeg.place(x=5, y=185, width=60, height=40)
buttonNumber0 = Radiobutton(master=frameTasten, bg='#F2F2F2', bd=1, indicator=0, text='0', value=0, variable=number,
                            font='Arial 14', command=entry)
buttonNumber0.place(x=70, y=185, width=60, height=40)
buttonDot = Radiobutton(master=frameTasten, bg='#D8D8D8', bd=1, indicator=0, text='.', value='.', variable=number,
                        font='Arial 14', command=entry)
buttonDot.place(x=135, y=185, width=60, height=40)
buttonEquality = Button(master=frameTasten, bg='#58ACFA', bd=1, text='=', font='Arial 14', command=output)
buttonEquality.place(x=200, y=185, width=60, height=40)

# Aktivieren des Fensters
ProgramWindow.mainloop()
