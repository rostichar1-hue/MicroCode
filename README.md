 mc-lang

The shortest and most secure query language

 Install

```bash
pip install mc-lang
```
Usage
```bash
micro data.mc
```
Example
```mc
CREATE users (id INT, name STRING, age INT, city STRING)
+users {1, "Alex", 28, "Moscow"}
users:name,age(city="Moscow")50
```
License
```Text

**Commit new file**

---

### 4. Файл: `data.mc`

**Name your file:** `data.mc`
```
CREATE users (id INT, name STRING, age INT, city STRING)
+users {1, "Alex", 28, "Moscow"}
+users {2, "Kate", 22, "SPB"}
+users {3, "John", 35, "Moscow"}
+users {4, "Anna", 19, "SPB"}
users:name,age()50
```

**Commit new file**

---

### 5. Файл: `examples.mc`

**Name your file:** `examples.mc`
```
users:name,age(city="Moscow")50
users:name,age(age>25)50
users:city="London"(id=1)
-users(id=4)!
users#
### 6. Файл: `parser.py`

**Name your file:** `parser.py`

```python
import re

def parse(cmd):
    cmd = cmd.strip()
    
    match = re.match(r'^([a-z]+):([a-z,]+)\((.+)\)(\d+)$', cmd)
    if match:
        return {
            'command': 'SELECT',
            'table': match.group(1),
            'fields': match.group(2).split(','),
            'condition': match.group(3),
            'limit': int(match.group(4))
        }
    
    match = re.match(r'^\+([a-z]+)\s*\{(.+)\}$', cmd)
    if match:
        return {
            'command': 'INSERT',
            'table': match.group(1),
            'values': [x.strip() for x in match.group(2).split(',')]
        }
    
    match = re.match(r'^([a-z]+):([a-z]+)="(.+)"\((.+)\)$', cmd)
    if match:
        return {
            'command': 'UPDATE',
            'table': match.group(1),
            'field': match.group(2),
            'value': match.group(3),
            'condition': match.group(4)
        }
    
    match = re.match(r'^-([a-z]+)\((.+)\)!$', cmd)
    if match:
        return {
            'command': 'DELETE',
            'table': match.group(1),
            'condition': match.group(2)
        }
    
    match = re.match(r'^([a-z]+)#$', cmd)
    if match:
        return {
            'command': 'COUNT',
            'table': match.group(1)
        }
    
    return {'error': 'Unknown command'}

if __name__ == "__main__":
    print(parse("users:name,age(city=\"Moscow\")50"))
```

Commit new file

