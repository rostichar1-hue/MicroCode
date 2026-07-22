from parser import parse
from executor import execute

def run_file(filename):
    with open(filename) as f:
        lines = [line.strip() for line in f if line.strip() and not line.startswith('//')]

    out = [f"\n{'='*50}\n  MicroCode: {filename}\n{'='*50}\n"]
    for line in lines:
        cmd = parse(line)
        out.append(execute(cmd) if cmd else f"Unknown: {line}")
    return '\n'.join(out)
