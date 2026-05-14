# User Login System

A modular, persistent user-login system built in Python. Supports three user types with role-based access, and persists data using **Pickle**, **JSON**, and **SQLite**.

---

## Project Structure

```
user_login_system/
├── AppUser.py              # Base user class
├── AdminUser.py            # Admin user with role and ID
├── FullUser.py             # Full user with UserRole enum
├── object_save.py          # Menu-driven persistence system
├── object_overloading.py   # Operator overloading demos
├── README.md
├── requirements.txt
├── .gitignore
└── data/                   # Pickle, JSON, and SQLite output files
```

---

## Setup

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/user-login-system.git
cd user-login-system
```

### 2. (Optional) Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

No third-party packages are required — this project uses only the Python standard library (`pickle`, `sqlite3`, `json`, `enum`).

---

## Running the App

```bash
python object_save.py
```

### Menu Options

```
1. Display all users
2. Save users using Pickle      → data/users.pkl
3. Save users using JSON        → data/users.json
4. Save users to SQLite         → data/users.db
5. Exit
```

---

## User Types

| Class       | Inherits From | Extra Attributes         |
|-------------|---------------|--------------------------|
| `AppUser`   | —             | `user_name`, `contact`   |
| `AdminUser` | `AppUser`     | + `user_role`, `user_id` |
| `FullUser`  | `AppUser`     | + `user_role`, `user_id` |

### UserRole Enum (from `FullUser.py`)
- `Admin`
- `Operator`
- `Guest`

---

## Example Output

```
Welcome to Lab 24: Persistent User Login System

Menu:
1. Display all users
...

[AppUser]   Name: Alice   | Contact: alice@example.com
[AdminUser] Name: Bob     | Contact: bob@example.com  | Role: Admin    | ID: 101
[FullUser]  Name: Charlie | Contact: charlie@example.com | Role: Operator | ID: 202
```

---

## Persistence

All data files are saved to the `data/` directory:

- **Pickle** (`data/users.pkl`) — Full object serialization, preserves class structure.
- **JSON** (`data/users.json`) — Human-readable metadata export.
- **SQLite** (`data/users.db`) — Relational storage with a BLOB column for pickled objects.

---

## Git Workflow

```bash
git checkout -b feature/your-feature
# make changes
git add .
git commit -m "feat: describe your change"
git checkout main
git merge feature/your-feature
git push origin main
```

---

## License

MIT
