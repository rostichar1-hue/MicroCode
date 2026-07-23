import json
from tabulate import tabulate
from index import Index
from groupby import group_by
from join import join

tables = {}
indexes = {}
DATA_FILE = 'micql_data.json'

def save_data():
    with open(DATA_FILE, 'w') as f:
        json.dump(tables, f)
    return "Data saved"

def load_data():
    global tables
    try:
        with open(DATA_FILE, 'r') as f:
            tables = json.load(f)
        return "Data loaded"
    except FileNotFoundError:
        return "No saved data"

def execute(cmd):
    if cmd['cmd'] == 'CREATE':
        tables[cmd['table']] = {'rows': [], 'fields': cmd.get('fields', [])}
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
            return tabulate(rows, headers='keys', tablefmt='grid')
        return "No data"

    if cmd['cmd'] == 'GROUPBY':
        rows = tables.get(cmd['table'], {}).get('rows', [])
        result = group_by(rows, cmd['group'], cmd['field'], cmd.get('agg', 'avg'))
        return tabulate(result, headers='keys', tablefmt='grid') if result else "No data"

    if cmd['cmd'] == 'JOIN':
        left = tables.get(cmd['left'], {}).get('rows', [])
        right = tables.get(cmd['right'], {}).get('rows', [])
        result = join(left, right, cmd['left_key'], cmd['right_key'])
        return tabulate(result, headers='keys', tablefmt='grid') if result else "No data"

    if cmd['cmd'] == 'SAVE':
        return save_data()

    if cmd['cmd'] == 'LOAD':
        return load_data()

    return "Unknown command"
