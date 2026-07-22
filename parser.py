import re

def parse(line):
    line = line.strip()
    if not line or line.startswith('//'):
        return None

    if line.upper().startswith('CREATE'):
        match = re.match(r'CREATE\s+([a-z]+)\s*\((.+)\)', line, re.IGNORECASE)
        if match:
            return {'cmd': 'CREATE', 'table': match.group(1), 'fields': match.group(2).split(',')}

    if line.startswith('+'):
        match = re.match(r'^\+([a-z]+)\s*\{(.+)\}$', line)
        if match:
            return {'cmd': 'INSERT', 'table': match.group(1), 'values': [x.strip().strip('"') for x in match.group(2).split(',')]}

    if ':' in line and '(' in line and ')' in line:
        parts = line.split(':', 1)
        if len(parts) == 2:
            table = parts[0]
            rest = parts[1]
            fields_part, rest = rest.split('(', 1)
            condition, limit_part = rest.split(')', 1)
            limit = int(limit_part) if limit_part else 10
            fields = [f.strip() for f in fields_part.split(',') if f.strip()]
            return {'cmd': 'SELECT', 'table': table, 'fields': fields, 'condition': condition.strip(), 'limit': limit}

    return None
