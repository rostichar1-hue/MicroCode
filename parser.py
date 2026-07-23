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

    if '@' in line and '(' in line and ')' in line:
        table, rest = line.split(':', 1)
        field_group, rest = rest.split('@', 1)
        group_field, rest = rest.split('(', 1)
        condition, limit_part = rest.split(')', 1)
        return {
            'cmd': 'GROUPBY',
            'table': table,
            'field': field_group.strip(),
            'group': group_field.strip(),
            'agg': 'avg',
            'limit': int(limit_part) if limit_part else 10
        }

    if 'JOIN' in line.upper():
        m = re.match(r'JOIN\s+([a-z]+)\s+([a-z]+)\s+ON\s+([a-z]+)\.([a-z]+)\s*=\s*([a-z]+)\.([a-z]+)', line, re.IGNORECASE)
        if m:
            return {
                'cmd': 'JOIN',
                'left': m.group(1),
                'right': m.group(2),
                'left_key': m.group(4),
                'right_key': m.group(6)
            }

    return None
