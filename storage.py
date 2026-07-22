cat > microcode/storage.py << 'EOF'
tables = {}

def create(table, fields):
    tables[table] = {
        'fields': [f.strip() for f in fields],
        'rows': []
    }

def insert(table, values):
    row = dict(zip(tables[table]['fields'], values))
    tables[table]['rows'].append(row)

def select(table, fields, condition, limit):
    rows = tables.get(table, {}).get('rows', [])
    
    if condition:
        if '=' in condition:
            key, val = condition.split('=', 1)
            rows = [r for r in rows if str(r.get(key.strip())) == val.strip().strip('"')]
        elif '>' in condition:
            key, val = condition.split('>', 1)
            rows = [r for r in rows if int(r.get(key.strip(), 0)) > int(val)]
    
    return rows[:limit]
EOF
