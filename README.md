# Tag 1 – ETL mit Tabellenkalkulation & Git-Einstieg

Dieses Repository enthält die Ergebnisse der ersten Übung zum Thema ETL (Extract, Transform, Load) sowie die Versionierung der Arbeitsschritte mit Git. Für die Datenverarbeitung wurde **LibreOffice Calc** (als Alternative zu Microsoft Excel) verwendet.

## Ordnerstruktur & Dateien
- `excel/` – Beinhaltet die originalen Startdateien (`Geraete.csv`, `Ausleihen.csv`, `Mitarbeiter.csv`) sowie die exportierte `Gesamt_bereinigt.csv`.
- `Gesamt.ods` – Die finale Arbeitsmappe inkl. Rohdaten (3 Einzelblätter), der bereinigten Gesamttabelle und der Pivot-Auswertungen.
- `csvExtractor.py` - Kurzes Proof-of-Concept Python-Skript zum Einlesen der exportierten Daten.

---

## Arbeitsablauf (Datenzusammenführung)
1. **Import:** Die drei bereitgestellten CSV-Dateien wurden mit der korrekten Zeichencodierung (UTF-8) in drei separate Tabellenblätter importiert.
2. **Gesamttabelle:** Auf einem neuen Tabellenblatt ("Gesamt") wurden die Daten zusammengeführt.
3. **Verknüpfung:** Um die Geräte- und Mitarbeiterdaten mit den Ausleihen zu verbinden, kam die Funktion **`XLOOKUP` (XVERWEIS)** zum Einsatz. Die Formel wurde für die erste Zeile erstellt und durch das "Herunterziehen" über alle Datensätze der neuen Gesamttabelle angewendet.

---

## Entdeckte Probleme & Datenbereinigung
Bei der Durchsicht und Bereinigung der Rohdaten sind folgende Dinge aufgefallen:
* **Keine leeren Zeilen:** Bei der Prüfung auf komplett leere Zeilen wurden keine fehlerhaften Leerzeilen gefunden.
* **Formatierungsfehler (Datum):** Die Datumswerte wurden beim Import nicht sofort korrekt erkannt. **Lösung:** Das Zellformat wurde nachträglich auf das korrekte Datumsformat (TT.MM.JJJJ) angepasst, um Pivot-Auswertungen zu ermöglichen.
* **Mehrfachausleihen:** Es ist aufgefallen, dass bestimmte Geräte (z. B. `G0035`) mehrfach in der Liste auftauchten. Das sind aber keine Duplikate, sondern wir vermuten, einerseits fehlerhafte Zuordnung und zweitens Mehrfachausleihung hintereinander ohne eingetragene Rückgabe
* **Ausreißer (Preisanomalie):** Bei der Überprüfung der Beträge fiel auf, dass ein Smartphone mit einem unrealistisch niedrigen Preis erfasst war.

---

## Wichtige Erkenntnisse aus der visuellen Analyse
Basierend auf der erstellten Pivot-Tabelle, den Zusammenführungen der Tabellen und den Diagrammen ließen sich folgende Erkenntnisse aus der kombinierten Gesamttabelle ableiten:
1. **Bestand:** Aktuell befinden sich genau **20 Geräte nicht im Einsatz** (Rückgabedatum liegt in der Vergangenheit bzw. keine aktive Ausleihe).
2. **Beliebtestes Gerät:** Die Pivot-Analyse der Ausleihen pro Gerätetyp zeigt deutlich, dass der **Beamer** und der **Drucker** die am häufigsten ausgeliehenen Gerätetypen sind.

---

## Python-Anbindung (Proof of Concept)
Um zu beweisen, dass die bereinigten und exportierten Daten programmgesteuert weiterverarbeitet werden können, wurde ein kurzes Python-Skript erstellt. Anstelle komplexer Bibliotheken reichte hier das in Python integrierte Standard-Modul `csv`. Mithilfe von `csv.reader` konnte die Datei `Gesamt_bereinigt.csv` problemlos eingelesen werden.