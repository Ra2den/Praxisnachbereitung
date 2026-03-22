
```mermaid
erDiagram
    Mitarbeiter ||--o{ Ausleihen : "leiht aus"
    Geraete ||--o{ Ausleihen : "wird verliehen"

    Mitarbeiter {
        string mitarbeiter_id PK
        string name
        string abteilung
        string standort
    }

    Geraete {
        string geraetenummer PK
        string geraetetyp
        string modell
        date kaufdatum
        float netto_kaufpreis
        string standort
    }

    Ausleihen {
        string geraetenummer FK
        string mitarbeiter_id FK
        date ausgabe_am
        date rueckgabe_am
    }
```
**R1**: Jedes Gerät darf nur eine Aktive zuweisung haben.  
**R2**: Wenn ein Gerät ausgeliehen wird muss ein Rückgabedatum erstellt werden.  
**R3**: Ein Gerät darf nur eine ID haben und diese kann erst nach dem rückgabedatum wieder ausgeliehen werden.  
**R4**: Der Preis darf nicht negativ sein.
