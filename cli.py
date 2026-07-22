import sys
from parser import parse
from executor import execute

def main():
    if len(sys.argv) < 2:
        print("Usage: micro <file.mc>")
        sys.exit(1)

    filename = sys.argv[1]
    with open(filename) as f:
        lines = [line.strip() for line in f if line.strip() and not line.startswith('//')]

    print(f"\n{'='*50}\n  Micql: {filename}\n{'='*50}\n")
    for line in lines:
        cmd = parse(line)
        if cmd:
            print(execute(cmd))
        else:
            print(f"Unknown: {line}")

if __name__ == "__main__":
    main()
