import subprocess
import sys


def main():
    proc = subprocess.Popen(["poetry", "build-ext"])
    code = proc.wait()
    sys.exit(code)

if __name__ == '__main__':
    main()