'''
Von: Elias Frank und Benjamin Mair
Ziel: Das Projekt soll eine Eingabe (z.B. aabc) haben und alle möglichen Kombinationen ausgeben
        Der Input darf doppelte Zeichen enthalten
'''

import tkinter as tk

#funktion zur berechnung der kombinationen
def print_combis(chars):
    combis = []
    if len(chars) > 2:
        for i in range(0, len(chars)):
            var = chars
            var = var.replace(chars[i], "")
            combis2 = print_combis(var)
            for combi in combis2:
                combis.append(chars[i] + combi)
    else:
        combis.append(chars)
        combis.append(chars[1] + chars[0])
    return combis

#berechen knopf funtion
def eingabe():
    chars = ein_chars.get()
    if len(chars) > 7:
        erg.config(text="Die Zeichenkette darf höchstens 7 Zeichen lang sein.")
        return

    combis = print_combis(chars)
    combi_count = len(combis)

    erg.config(text=f"Anzahl der einzigartigen Kombinationen: {combi_count}")
    
    ausgabefeld.delete(0, tk.END)
    for combi in combis:
        ausgabefeld.insert(tk.END, combi)

#Graphische oberfläche
root = tk.Tk()
root.title("Kombinationen Rechner")

text = tk.Label(root, text="Geben Sie eine Zeichenkette ein (max. 7 Zeichen):")
text.grid(row=0, column=0)

ein_chars = tk.Entry(root)
ein_chars.grid(row=0, column=1)

button = tk.Button(root, text="Berechnen", command=eingabe)
button.grid(row=1, column=0, columnspan=2)

erg = tk.Label(root, text="Anzahl der einzigartigen Kombinationen: ")
erg.grid(row=2, column=0, columnspan=2)

ausgabefeld = tk.Listbox(root, width=50, height=10)
ausgabefeld.grid(row=3, column=0, columnspan=2)

root.mainloop()



