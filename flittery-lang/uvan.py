import sys, os, gc, re, time, json, psutil, js2py, yaml, ctypes
from pathlib import Path
from collections import ChainMap

# --- BUILD CONFIG ---
VERSION = "8.1.0-STANDALONE"
REQUIRED_FILE = "uvan.py"  # You can change this to "project.py"
RAM_LOCK_GB = 8
UVAN_DIR = Path(os.getenv('LOCALAPPDATA')) / "UVAN"
TERM_KEY = "turtleboyagain120"

class UVAN_Fortress:
    def __init__(self):
        self._check_project_status()
        self.scope = ChainMap({})
        self._init_partitions()
        self.ram_vault = self._allocate_vault()

    def _check_project_status(self):
        """Verifies if the script name matches the build target."""
        current_file = Path(__file__).name
        print(f"-- BUILD CHECK: Detected '{current_file}' --")
        if current_file.lower() == REQUIRED_FILE.lower() or current_file.lower() == "project.py":
            print(f">> [STATUS] YES: Project environment recognized. Launching...")
        else:
            print(f">> [STATUS] NO: Running in ad-hoc mode (Name: {current_file})")

    def _init_partitions(self):
        """Creates user-level folders. No Admin required."""
        UVAN_DIR.mkdir(parents=True, exist_ok=True)
        for d in ["Cache", "Data"]:
            (UVAN_DIR / d).mkdir(exist_ok=True)
        
        if os.name == 'nt':
            ctypes.windll.kernel32.SetConsoleTitleW(f"UVAN_FORTRESS_{VERSION}")
        
        print(f"--- UVAN {VERSION} ONLINE ---")
        print(f">> DATA_ROOT: {UVAN_DIR}")

    def _allocate_vault(self):
        """Commits 8GB of your 32GB RAM."""
        print(f">> ALLOCATING 8GB HARDWARE SACRIFICE...")
        try:
            # We fill it with zeros to force the OS to actually hand over the RAM
            return bytearray(RAM_LOCK_GB * (1024**3))
        except MemoryError:
            print("!! [WARN] Memory request denied. Scaling to 512MB.")
            return bytearray(512 * (1024**2))

    def process_command(self, cmd_line):
        cmd_line = cmd_line.strip()
        if not cmd_line or cmd_line.startswith("#"): return
        if TERM_KEY in cmd_line: sys.exit(f">> [SHUTDOWN] KEY: {TERM_KEY}")

        # JS Sandbox
        if "[JS]" in cmd_line:
            try:
                js_src = re.search(r'\[JS\](.*?)\[/JS\]', cmd_line).group(1)
                print(f">> [JS] {js2py.eval_js(js_src)}")
            except Exception as e: print(f">> [JS_ERR] {e}")

        # Variable Logic
        assign = re.match(r'@(\w+)=(.*)', cmd_line)
        if assign:
            var, val = assign.groups()
            self.scope[var] = val
            print(f">> [BRAIN] @{var} STORED")

        # Data Loading
        if "LOAD:" in cmd_line:
            try:
                data = yaml.safe_load(cmd_line.split("LOAD:")[1])
                print(f">> [DATA] {type(data).__name__.upper()} LOADED")
            except Exception as e: print(f">> [DATA_ERR] {e}")

    def shell(self):
        print(f"FORTRESS ACTIVE. TYPE 'exit' OR '{TERM_KEY}' TO QUIT.")
        while True:
            try:
                raw = input("UVAN> ")
                if raw.lower() in ['exit', 'quit']: break
                self.process_command(raw)
            except (KeyboardInterrupt, EOFError): break

def main():
    # Final check for dependencies
    fortress = UVAN_Fortress()
    fortress.shell()

if __name__ == "__main__":
    main()
