cat > ~/MicroCode/executor.py << 'EOF'
import json
import asyncio
from tabulate import tabulate

tables = {}
DATA_FILE = 'microcode_data.json'

def save_data():
    with open(DATA_FILE, 'w') as f:
        json.dump(tables, f)
    return f"Data saved to {DATA_FILE}"

def load_data():
    global tables
    try:
        with open(DATA_FILE, 'r') as f:
            tables = json.load(f)
        return f"Data loaded from {DATA_FILE}"
    except FileNotFoundError:
        return "No saved data found"

def execute(cmd):
    if cmd['cmd'] == 'CREATE':
        tables[cmd['table']] = {'rows': [], 'indexes': {}}
        save_data()
        return f"Table '{cmd['table']}' created"

    if cmd['cmd'] == 'INSERT':
        row = {}
        fields = cmd.get('fields', [f'col{i+1}' for i in range(len(cmd['values']))])
        for i, val in enumerate(cmd['values']):
            if i < len(fields):
                row[fields[i]] = val
            else:
                row[f'col{i+1}'] = val
        tables[cmd['table']]['rows'].append(row)
        save_data()
        return f"Inserted into '{cmd['table']}'"

    if cmd['cmd'] == 'SELECT':
        rows = tables.get(cmd['table'], {}).get('rows', [])
        if rows:
            return tabulate(rows, headers='keys', tablefmt='grid')
        return "No data"

    if cmd['cmd'] == 'SAVE':
        return save_data()

    if cmd['cmd'] == 'LOAD':
        return load_data()

    return "Unknown command"

# Асинхронная версия (как Go goroutines)
async def async_select(table, condition):
    await asyncio.sleep(0)
    return execute({'cmd': 'SELECT', 'table': table, 'condition': condition})

def parallel_queries(queries):
    loop = asyncio.new_event_loop()
    tasks = [async_select(q['table'], q['condition']) for q in queries]
    return loop.run_until_complete(asyncio.gather(*tasks))
EOF
