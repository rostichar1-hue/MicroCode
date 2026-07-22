import json
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
        tables[cmd['table']] = {'rows': []}
        save_data()
        return f"Table '{cmd['table']}' created"

    if cmd['cmd'] == 'INSERT':
        row = {}
        for i, val in enumerate(cmd['values']):
            row[f'col{i+1}'] = val
        tables[cmd['table']]['rows'].append(row)
        save_data()
        return f"Inserted into '{cmd['table']}'"

    if cmd['cmd'] == 'SELECT':
        rows = tables.get(cmd['table'], {}).get('rows', [])
        if rows:
            headers = list(rows[0].keys())
            return tabulate(rows, headers=headers, tablefmt='grid')
        return "No data"

    if cmd['cmd'] == 'SAVE':
        return save_data()

    if cmd['cmd'] == 'LOAD':
        return load_data()

    return "Unknown command"
