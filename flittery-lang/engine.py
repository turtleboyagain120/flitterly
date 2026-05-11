import sys, os, psutil, js2py, gc, re, time, getpass, json

# ============================================================
# 1. HARDCODED CONFIGURATION & HYBRID COMMAND MAP
# ============================================================
INTERNAL_CONFIG = {
    "AUTHORIZED_USER": "turtl",
    "GATE_PASSWORD": "turtl",
    "UVAN_VERSION": "7.0",
    "UVAN_PATH": "C:/UVAN"
}

# This map handles BOTH fixed (exact line) and substring (keyword) checks
COMMAND_MAP = {
    "fixed": {
        "Edit/%remote": "REMOTE_GATE",
        "admin [SECURITY] IDENTITY CONFIRMED: {current_user}")

def password_gate():
    """Password lock for sensitive commands."""
    print(">> [LOCKED] PROTECTED COMMAND DETECTED.")
    attempt = input("ENTER ACCESS KEY: ")
    if attempt == INTERNAL_CONFIG["GATE_PASSWORD"]:
        print(">> [LOCKED] ACCESS GRANTED.")
        return True
    print("!! INCORRECT KEY. ABORTING.")
    return False

# ============================================================
# 3. VAN MEMORY LOCK (8GB)
# ============================================================
def lock_van_memory():
    LOCK_BYTES = 8 * (1024**3)
    print(f">> [SYSTEM] INITIATING 8GB VAN LOCK...")
    mem = psutil.virtual_memory()
    if mem.available < LOCK_BYTES:
        print(f"!! FATAL: ONLY {mem.available/1e9:.2f}GB RAM FREE. 8GB REQUIRED.")
        sys.exit(1)
    try:
        gc.disable()
        _buffer = bytearray(LOCK_BYTES)
        gc.enable()
        print(">> [SYSTEM] VAN MEMORY LOCK ENGAGED.")
        return _buffer
    except MemoryError:
        print("!! FATAL: PHYSICAL ALLOCATION FAILED.")
        sys.exit(1)

# ============================================================
# 4. COMMAND BRAIN LOGIC
# ============================================================
class Brains:
    @staticmethod
    def execute(action, line):
        if action == "REMOTE_GATE":
            if password_gate():
                print(">> [REMOTE] NETWORK-SHARING CHANNEL OPEN.")
        elif action == "FILE_BRAIN":
            print(">> [FILE] ^%FILE-ACCESS: FULL CONTROL GRANTED.")
        elif action == "NET_KILL":
            print(">> [NET] EXECUTING FORCE STOP...")
        elif action == "ADMIN_MACRO":
            print(">> [CMD] NET USER /ACTIVE:YES")
        elif action == "PRIV_CHECK":
            print(">> [CONTEXT] PRIVILEGE CHECK: OK.")
        elif "FLAG" in action:
            print(f">> [ROOT] EXECUTING: {line}")

# ============================================================
# 5. CORE ENGINE
# ============================================================
class FlitteryEngine:
    def __init__(self, script_path):
        verify_identity()
        self.ram_lock = lock_van_memory()
        
        if not os.path.exists(script_path):
            print(f"!! [ERR] SCRIPT '{script_path}' NOT FOUND.")
            sys.exit(1)
            
        with open(script_path, 'r') as f:
            self.code = f.read()

    def run(self):
        print(">> [VAN] BOOTING... ALL BRAINS ACTIVE.")
        
        # Pre-scan for UVAN
        if "UVAN .7.0" in self.code and not os.path.exists(INTERNAL_CONFIG["UVAN_PATH"]):
            print("!! [ERR] BRAIN UVAN .7.0 NOT FOUND AT C:/UVAN")
            return

        lines = self.code.split('\n')
        for line in lines:
            line = line.strip()
            if not line or line.startswith("#$"): continue

            # 1. FIXED COMMANDS (Exact Match)
            if line in COMMAND_MAP["fixed"]:
                Brains.execute(COMMAND_MAP["fixed"][line], line)
                continue

            # 2. SUBSTRING COMMANDS (Keywords)
            executed = False
            for trigger, action in COMMAND_MAP["substring"].items():
                if trigger in line:
                    Brains.execute(action, line)
                    executed = True
            
            # 3. POLYGLOT JS
            if "[JS]" in line:
                js_match = re.search(r'\[JS\](.*?)\[/JS\]', line)
                if js_match:
                    try:
                        res = js2py.eval_js(js_match.group(1))
                        print(f">> [JS_RES] {res}")
                    except Exception as e:
                        print(f"!! [JS_ERR] {e}")

# ============================================================
# 6. RUNTIME ENTRY (Used by pip install)
# ============================================================
def main():
    if len(sys.argv) < 2:
        print("Usage: flit <filename.flit>")
    else:
        # sys.argv[1] is the filename passed after 'flit'
        engine = FlitteryEngine(sys.argv[1])
        engine.run()

if __name__ == "__main__":
    main()
