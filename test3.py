# Test 3: Öffnet ein tkinter-Fenster mit Eingabefeld und Button.
# Nach Klick auf "Übernehmen" wird die eingegebene Note angezeigt.
# Ergebnis: Eingabe und Anzeige funktionieren -> "Bearbeiten" ist machbar.

import tkinter as tk


# 1. Wird beim Klick auf "Übernehmen" ausgeführt
def uebernehmen():
    note = eingabe.get()
    if note:
        ausgabe.config(text=f"Eingegeben: {note}")
    else:
        ausgabe.config(text="Bitte eine Note eingeben.")


# 2. Hauptfenster
fenster = tk.Tk()
fenster.title("Studien-Dashboard – Test")
fenster.geometry("320x160")

# 3. Elemente anlegen und anzeigen
tk.Label(fenster, text="Note eingeben:").pack(pady=5)
eingabe = tk.Entry(fenster)
eingabe.pack()
tk.Button(fenster, text="Übernehmen", command=uebernehmen).pack(pady=10)
ausgabe = tk.Label(fenster, text="")
ausgabe.pack()

# 4. Fenster starten
fenster.mainloop()
# Hinweis: def definiert die Funktion nur. Sie läuft erst beim Klick –
# dann existieren "eingabe" und "ausgabe" bereits.
