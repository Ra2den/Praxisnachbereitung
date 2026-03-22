
```mermaid
erDiagram
    Employee ||--o{ Assignment : "performs"
    Device ||--o{ Assignment : "is assigned in"
    Category ||--o{ Device : "classifies"

    Employee {
        int employee_id PK
        string personal_number UK
        string first_name
        string last_name
        string email UK
        string department
    }

    Device {
        int device_id PK
        string serial_number UK
        string inventory_number UK
        string model_name
        int category_id FK
        date purchase_date
        string status "e.g., active, defective, retired"
    }

    Category {
        int category_id PK
        string name UK "e.g., Laptop, Smartphone, Tablet"
    }

    Assignment {
        int assignment_id PK
        int employee_id FK
        int device_id FK
        date start_date
        date end_date "nullable"
        string note
    }
