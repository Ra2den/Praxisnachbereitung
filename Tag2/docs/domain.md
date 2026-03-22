
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