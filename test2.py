# Test 2: Speichert ein Modul (Titel, ECTS, Status, Note) als JSON-Datei
# und liest es wieder ein. Vergleicht Original und geladene Daten.
# Ergebnis: Daten identisch, Umlaute bleiben erhalten.

import json

# 1. Beispieldaten: ein Modul mit Umlaut im Titel
modul = {
    "titel": "Einführung in die Programmierung mit Python",
    "ects": 5,
    "status": "BESTANDEN",
    "note": 1.7
}

# 2. In die Datei schreiben
with open("test.json", "w", encoding="utf-8") as datei:
    json.dump(modul, datei, ensure_ascii=False, indent=4)
print("Gespeichert:", modul)

# 3. Wieder einlesen
with open("test.json", "r", encoding="utf-8") as datei:
    geladen = json.load(datei)
print("Geladen:   ", geladen)

# 4. Vergleichen
if geladen == modul:
    print("Test bestanden: Daten sind nach dem Einlesen identisch.")
else:
    print("Test fehlgeschlagen: Daten unterscheiden sich.")
