
```mermaid
erDiagram
    Mitarbeiter ||--o{ Zuweisung : "leiht aus"
    Geraet ||--o{ Zuweisung : "wird zugewiesen"
    Kategorie ||--o{ Geraet : "gruppiert"

    Mitarbeiter {
        int mitarbeiter_id PK
        string personalnummer UK
        string vorname
        string nachname
        string email UK
        string abteilung
    }

    Geraet {
        int geraet_id PK
        string seriennummer UK
        string inventarnummer UK
        string modellbezeichnung
        int kategorie_id FK
        date kaufdatum
        string status "z.B. aktiv, defekt, ausgemustert"
    }

    Kategorie {
        int kategorie_id PK
        string name UK "z.B. Laptop, Smartphone"
    }

    Zuweisung {
        int zuweisung_id PK
        int mitarbeiter_id FK
        int geraet_id FK
        date start_datum
        date end_datum "leeres Feld = aktuell aktiv"
        string anmerkung
    }