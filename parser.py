import re

def parse(line):
    line = line.strip()
    if not line or line.startswith('//'):
        return None

    if line.upper().startswith('CREATE'):
        m = re.match(r'CREATE\s+([a-z]+)\s*\((.+)\)', line, re.IGNORECASE)
        if m:
            return {'cmd': 'CREATE', 'table': m.group(1), 'fields': [x.strip() for x in m.group(2).split(',')]}

    if line.startswith('+'):
        m = re.match(r'^\+([a-z]+)\s*\{(.+)\}$', line)
        if m:
            return {'cmd': 'INSERT', 'table': m.group(1), 'values': [x.strip().strip('"') for x in m.group(2).split(',')]}

    if line.upper() == 'SAVE':
        return {'cmd': 'SAVE'}

    if line.upper() == 'LOAD':
        return {'cmd': 'LOAD'}

    if ':' in line and '(' in line and ')' in line:
        table, rest = line.split(':', 1)
        fields_part, rest = rest.split('(', 1)
        condition, limit_part = rest.split(')', 1)
        return {
            'cmd': 'SELECT',
            'table': table,
            'fields': [x.strip() for x in fields_part.split(',') if x.strip()],
            'condition': condition.strip(),
            'limit': int(limit_part) if limit_part else 10
        }

    return None
