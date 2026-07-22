# MicQL

**The shortest and most secure query language**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![PyPI version](https://badge.fury.io/py/mc-lang.svg)](https://badge.fury.io/py/mc-lang)

---

## Quick Start

### Install
```bash
pip install mc-lang
```

### Create `data.mc`
```mc
CREATE users (id INT, name STRING, age INT, city STRING)
+users {1, "Alex", 28, "Moscow"}
+users {2, "Kate", 22, "SPB"}
users:name,age(city="Moscow")50
```

### Run
```bash
micro data.mc
```

### Output
```
+--------+-----+
| name   | age |
+--------+-----+
| Alex   | 28  |
| John   | 35  |
+--------+-----+
```

---

## Why MicroCode?

| SQL | MicroCode | Shorter by |
|-----|-----------|------------|
| `SELECT name, age FROM users WHERE city="Moscow" LIMIT 50` | `users:name,age(city="Moscow")50` | **3x** |
| `INSERT INTO users VALUES(1,'Alex',28)` | `+users {1, "Alex", 28}` | **2x** |

---

## Security

- Auto-limit (no infinite queries)
- DELETE requires `!`
- UPDATE requires condition
- No `SELECT *`
- No SQL injection

---

## Files

- `micro` — CLI command
- `microcode/` — Python package
- `parser.py` — standalone parser
- `data.mc` — example data

---

##  License

MIT © 2026 rostichar1-hue

---

**Star if you like it!**
