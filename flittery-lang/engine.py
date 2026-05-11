import sys, os, gc, re, time, json, psutil, js2py, yaml, ctypes
from pathlib import Path
from collections import ChainMap

# --- CONFIGURATION ---
VERSION = "8.0.0-UNLEASHED"
# Uses Local AppData to avoid needing Admin permissions for folder creation
UVAN_DIR = Path(os.getenv('LOCALAPPDATA')) / "UVAN"
TERM_KEY = "turtleboyagain120"
RAM_LOCK_GB = 8 

class UVAN_Fortress:
    def __init__(self):
        self.scope = ChainMap({}) 
        self._init_partitions()
        self.ram_vault = self._allocate_vault()

    def _init_partitions(self):
        """Creates working directories in User space (No Admin Required)."""
        UVAN_DIR.mkdir(parents=True, exist_ok=True)
        for d in ["Cache", "Logs", "Data"]:
            (UVAN_DIR / d).mkdir(exist_ok=True)
        
        # Set Console Title
        if os.name == 'nt':
            ctypes.windll.kernel32.SetConsoleTitleW(f"UVAN_FORTRESS_{VERSION}")
        
        print(f"--- UVAN {VERSION} ONLINE ---")
        print(f">> ROOT: {UVAN_DIR}")
        print(f">> VAULT: {RAM_LOCK_GB}GB RESERVED")

    def _allocate_vault(self):
        """Reserved 8GB buffer. Using zeros to ensure OS commits the memory."""
        print(f">> INITIALIZING HARDWARE SACRIFICE...")
        try:
            # We don't disable GC entirely anymore (better security), 
            # but we do a heavy collection before the lock.
            gc.collect()
            return bytearray(RAM_LOCK_GB * (1024**3))
        except MemoryError:
            print("!! [WARN] SYSTEM REJECTED 8GB ALLOCATION. DROPPING TO 1GB.")
            return bytearray(1 * (1024**3))

    def process_command(self, cmd_line):
        cmd_line = cmd_line.strip()
        if not cmd_line or cmd_line.startswith("#"): return
        if TERM_KEY in cmd_line: sys.exit(f">> [SHUTDOWN] KEY_SIG: {TERM_KEY}")

        # 1. Variable Brain (@VAR=VALUE)
        assign = re.match(r'@(\w+)=(.*)', cmd_line)
        if assign:
            var, val = assign.groups()
            self.scope[var] = val
            print(f">> [CACHED] @{var}")
            return

        # 2. JS Execution (The Sandbox)
        if "[JS]" in cmd_line:
            try:
                js_src = re.search(r'\[JS\](.*?)\[/JS\]', cmd_line).group(1)
                result = js2py.eval_js(js_src)
                print(f">> [JS_OUT] {result}")
            except Exception as e:
                print(f">> [JS_ERR] {e}")

        # 3. Data Loading (YAML/JSON)
        if "LOAD:" in cmd_line:
            try:
                data = yaml.safe_load(cmd_line.split("LOAD:")[1])
                print(f">> [DATA] RECEIVED: {type(data).__name__.upper()}")
            except Exception as e:
                print(f">> [DATA_ERR] {e}")

        # 4. Maintenance Cycle
        if "cycle" in cmd_line.lower():
            for i in range(1, 6):
                print(f"   [PURGE] CYCLE {i}/5...")
                time.sleep(0.1)
            gc.collect()

    def shell(self):
        print(f"\nFORTRESS ACTIVE. TYPE '{TERM_KEY}' OR 'exit' TO CLOSE.")
        while True:
            try:
                entry = input("UVAN> ")
                if entry.lower() in ['exit', 'quit']: break
                self.process_command(entry)
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f"!! [ERROR] {e}")

if __name__ == "__main__":
    fortress = UVAN_Fortress()
    fortress.shell()
