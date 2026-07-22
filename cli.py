cat > microcode/cli.py << 'EOF'
import sys
from .core import run_file

def main():
    if len(sys.argv) < 2:
        print("Usage: micro <file.mc>")
        sys.exit(1)
    print(run_file(sys.argv[1]))

if __name__ == "__main__":
    main()
EOF
