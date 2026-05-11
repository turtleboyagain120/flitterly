import sys, os, gc, re, time, getpass, json, psutil, js2py, yaml
from pathlib import Path
from collections import ChainMap

# --- CORE ARCHITECTURE ---
VERSION = "7.0.1"
UVAN_DIR = Path("C:/UVAN")
TERM_KEY = "turtleboyagain120"
RESOURCES = {"USER": "turtl", "RAM_GB": 8}

class UVAN_Fortress:
    def __init__(self, script=""):
        self._identity_gate()
        self.scope = ChainMap({}) # Hierarchical Variable Brain
        self.admin = any(k in script for k in ["ZZX", "LL!@M", "admin:yes"])
        self._init_partitions()
        self.ram_vault = self._hardware_sacrifice()

    def _identity_gate(self):
        if getpass.getuser() != RESOURCES["USER"]:
            sys.exit("!! [FATAL] UNAUTHORIZED USER IDENTITY DETECTED.")

    def _init_partitions(self):
        """Builds administrative hierarchy at C:/UVAN."""
        if not UVAN_DIR.exists():
            UVAN_DIR.mkdir(parents=True, exist_ok=True)
            for d in ["ZZX_Cache", "LL_Wrapper", "BSON_Storage"]:
                (UVAN_DIR / d).mkdir(exist_ok=True)
        print(f">> [UVAN_{VERSION}] PARTITIONS SYNCED | ADMIN: {self.admin}")

    def _hardware_sacrifice(self):
        """Locks 8GB RAM as a dedicated buffer for BSON/Command processing."""
        gc.collect()
        gc.disable()
        # Direct allocation of hardware sacrifice
        return bytearray(RESOURCES["RAM_GB"] * (1024**3))

    def process_command(self, cmd_line):
        """Unified Polyglot Parser for JS, YAML, JSON, and BSON-like data."""
        cmd_line = cmd_line.strip()
        if not cmd_line or cmd_line.startswith("#$") or TERM_KEY in cmd_line:
            if TERM_KEY in cmd_line: sys.exit(f">> [SHUTDOWN] SOURCE: {TERM_KEY}")
            return

        # Variable Assignment (@VAR=VALUE)
        assign = re.match(r'@(\w+)=(.*)', cmd_line)
        if assign:
            var, val = assign.groups()
            self.scope[var] = val
            print(f">> [BRAIN] CACHED: @{var}"); return

        # 1. Polyglot JS Engine
        if "[JS]" in cmd_line:
            js_src = re.search(r'\[JS\](.*?)\[/JS\]', cmd_line).group(1)
            print(f">> [UVAN_JS] {js2py.eval_js(js_src)}")

        # 2. Universal Data Loader (YAML/JSON superset)
        if "LOAD:" in cmd_line:
            data = yaml.safe_load(cmd_line.split("LOAD:")[1])
            print(f">> [DATA] LOADED {type(data).__name__.upper()} BLOCK")

        # 3. Force Level Logic
        f_lvl = 2 if cmd_line.endswith('""') else 1 if cmd_line.endswith('"') else 0
        tag = f"[FORCE_x{f_lvl}] " if f_lvl else ">> "

        # 4. Access Control Operators
        if "^%FILE" in cmd_line: print(f"{tag}[ACCESS] FILE-ACCESS GRANTED")
        if "^%REMOTE" in cmd_line: print(f"{tag}[ACCESS] REMOTE GATE OPENED")

        # 5. Maintenance Cycle
        if "for 12 in number" in cmd_line:
            for i in range(1, 13):
                print(f"   - {i}/12 CYCLE COMPLETE")
                time.sleep(0.01)

    def interactive_shell(self):
        print(f"UVAN {VERSION} FORTRESS SHELL | TYPE 'exit' TO QUIT")
        while True:
            try:
                raw = input(f"{RESOURCES['USER']}@uvan_fortress> ")
                if raw.lower() == "exit": break
                self.process_command(raw)
            except KeyboardInterrupt: break

# --- LAUNCHER ---
if __name__ == "__main__":
    # Combined entry: takes CMD args or launches REPL
    fortress = UVAN_Fortress(" ".join(sys.argv[1:]))
    if len(sys.argv) > 1:
        for part in " ".join(sys.argv[1:]).split(';'):
            fortress.process_command(part)
    else:
        fortress.interactive_shell()
