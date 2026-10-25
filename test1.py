# Test 1: Prüft, ob Python und alle benötigten Bibliotheken
# (json, datetime, abc, enum, os, tkinter) ohne Installation verfügbar sind.
# Ergebnis: Alle Importe fehlerfrei, Python 3.14.7, Tk 9.0.

import sys                            # Version
import json                           # Speichern
import os                             # Dateien
from abc import ABC, abstractmethod   # Abstrakte Klasse
from datetime import date             # Datum
from enum import Enum                 # Status
import tkinter as tk                  # Fenster
from tkinter import ttk               # Tabelle

print("Python-Version:", sys.version)
print("tkinter-Version:", tk.TkVersion)
print("Alle Bibliotheken verfügbar – keine Installation nötig.")
