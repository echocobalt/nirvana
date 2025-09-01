import os
import subprocess

__version__ = "v0.0.1"

def main() -> None:
    while True:
        current = os.getcwd()
        cmd = input(f"{current} -> ").strip()
        
        if not cmd:
            continue

        if "exit" in cmd:
            break

        if cmd.startswith("cd "):
            path = cmd.split(" ", 1)[1]
            os.chdir(path)
            continue
    
        try:
            subprocess.run(cmd, shell=True)
        except Exception as e:
            print(f"E: {e}")

if __name__ == "__main__":
    main()
