```markdown
# Micql — Minimalistic Query Language

Micql (pronounced "my-queue-l") is a query language that is 3–5 times shorter than SQL.  
It works with JSON, requires no database server, and runs on Termux, Linux, macOS, and Windows.

---

## Why Micql?

| SQL | Micql |
|-----|-------|
| `SELECT name FROM users WHERE age > 18 LIMIT 10` | `users:name(age>18)10` |
| `INSERT INTO users VALUES (1, 'Alex', 28)` | `+users {1, "Alex", 28}` |
| Requires a server | Works with JSON files |
| Long syntax | Minimal and clean |

---

## Quick Install

```bash
pip install git+https://github.com/rostichar1-hue/Micql.git
```

---

## Tutorial: Your First Database

### 1. Create a file named `data.mc`

```mc
CREATE users (id INT, name STRING, age INT)
+users {1, "Alex", 28}
+users {2, "Kate", 22}
users:name(age>20)10
SAVE
```

### 2. Run it

```bash
micro data.mc
```

### 3. Output

```
+--------+
| name   |
+--------+
| Alex   |
| Kate   |
+--------+
```

---

## Syntax Overview

| Command | Description | Example |
|---------|-------------|---------|
| `CREATE` | Create a table | `CREATE users (id INT, name STRING)` |
| `+` | Insert a row | `+users {1, "Alex", 28}` |
| `:` | Select data | `users:name(age>18)10` |
| `SAVE` | Save data to JSON | `SAVE` |
| `LOAD` | Load data from JSON | `LOAD` |

---

## More Examples

### Select with condition

```mc
users:name,age(city="Moscow")10
```

### Insert multiple rows

```mc
+users {1, "Alex", 28, "Moscow"}
+users {2, "Kate", 22, "SPB"}
+users {3, "John", 35, "Moscow"}
```

### Save and load

```mc
SAVE
LOAD
```

---

## Installation on Different Systems

**Linux / Termux**
```bash
git clone https://github.com/rostichar1-hue/Micql.git
cd Micql
./install.sh
source ~/.bashrc
```

**Windows (PowerShell)**
```powershell
pip install git+https://github.com/rostichar1-hue/Micql.git
```

**macOS**
```bash
brew install python3
pip3 install git+https://github.com/rostichar1-hue/Micql.git
```

---

## Commands

| Command | Description |
|---------|-------------|
| `micro data.mc` | Run a script |
| `micro` | Auto-create `data.mc` with sample data |
| `micro file.mc` | Run a specific file |

---

## Where to Use Micql

- Log processing
- Configuration files
- Telegram bots
- Prototyping and MVPs
- Scripts on mobile (Termux)
- Small JSON-based projects

---

## Author

**rostichar1-hue**  
Telegram: @darzx3  
GitHub: https://github.com/rostichar1-hue/Micql

---

## License

MIT
```
