# Database Documentation

## Overview

Smart Calculator Pro uses **SQLite** as its database.

The application uses **SQLAlchemy ORM** for database operations.

---

# Database Name

```
calculator.db
```

---

# Tables

The database contains two main tables:

1. Users
2. History

---

# Users Table

Stores registered user information.

| Column | Type | Description |
|---------|------|-------------|
| id | Integer | Primary Key |
| full_name | String | User Full Name |
| email | String | Unique Email Address |
| password | String | Hashed Password |
| is_active | Boolean | User Status |
| created_at | DateTime | Account Creation Time |

---

# History Table

Stores all calculator operations.

| Column | Type | Description |
|---------|------|-------------|
| id | Integer | Primary Key |
| operation | String | Calculator Operation |
| number1 | Float | First Number |
| number2 | Float | Second Number |
| result | Float | Calculation Result |
| user_id | Integer | Foreign Key |
| created_at | DateTime | Calculation Time |

---

# Relationship

One User

↓

Many History Records

```
Users (1)
    │
    │
    ▼
History (Many)
```

---

# ORM

SQLAlchemy ORM is used for:

- Creating tables
- Reading records
- Updating records
- Deleting records

---

# CRUD Operations

The application supports:

- Create User
- Login User
- Save Calculation
- View History
- Delete History
- View Statistics

---

# Future Improvements

The database can easily be migrated to:

- PostgreSQL
- MySQL
- Microsoft SQL Server

without changing the application architecture.