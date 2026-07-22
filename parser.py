import re

def parse(cmd):
    match = re.match(r'^([a-z])\.([a-z,]+)\(([^)]+)\)(\d+)$', cmd)
    if match:
        return {
            'table': match.group(1),
            'fields': match.group(2).split(','),
            'condition': match.group(3),
            'limit': int(match.group(4))
        }
    return None

print(parse("u.n,a(>18)50"))
