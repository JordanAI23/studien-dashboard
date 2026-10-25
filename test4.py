# Test 4: Zeichnet mit tkinter Canvas einen grauen Kreis und farbige
# Tortenstücke (create_arc). 5 ECTS = 10 Grad (360 Grad / 180 ECTS).
# Ergebnis: Der Fortschrittskreis aus der Skizze ist umsetzbar.
import tkinter as tk

fenster = tk.Tk()
canvas = tk.Canvas(fenster, width=300, height=300, bg="white")
canvas.pack()

# grauer Kreis = alles offen
canvas.create_oval(50, 50, 250, 250, fill="lightgray")

# ein Modul bestanden: 5 ECTS = 10 Grad
canvas.create_arc(50, 50, 250, 250, start=90, extent=-10, fill="green")

# ein Modul eingebucht: die nächsten 10 Grad
canvas.create_arc(50, 50, 250, 250, start=80, extent=-10, fill="yellow")

fenster.mainloop()
