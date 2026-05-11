import sys, os, psutil, js2py, gc, re, time, getpass, json

# ============================================================
# 1. HARDCODED CONFIGURATION (The "Built-in" JSON)
# ============================================================
INTERNAL_CONFIG = {
    "AUTHORIZED_USER": "turtl",
    "GATE_PASSWORD": "turtl",
    "UVAN_VERSION": "7.0",
    "UVAN_PATH": "C:/UVAN",
    "ACTIVE_CONTEXT": "ROOT_ADMIN"
}

# ============================================================
# 2. SECURITY & IDENTITY BRAIN
# ============================================================
def run_security_protocol():
    """Verifies the OS user is 'turtl'."""
    current_os_user = getpass.getuser()
    if current_os_user != INTERNAL_CONFIG["AUTHORIZED_USER"]:
        print(f"!! SECURITY BREACH: User '{current_os_user}' is unauthorized.")
        print("!! ACCESS PERMANENTLY DENIED.")
        sys.exit(1)
    print(f">> [AUTH] IDENTITY CONFIRMED: {current_os_user}")

def password_gate():
    """The password check for protected commands."""
    print(">> [LOCKED] PROTECTED COMMAND DETECTED.")
    attempt = input("ENTER ACCESS KEY: ")
    if attempt == INTERNAL_CONFIG["GATE_PASSWORD"]:
        print(">> [LOCKED] ACCESS GRANTED.")
        return True
    else:
        print("!! INCORRECT KEY. COMMAND ABORTED.")
        return False

# ============================================================
# 3. VAN MEMORY LOCK (8GB Zero-Latency)
# ============================================================
def engage_memory_lock():
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
        print("!! FATAL: MEMORY ALLOCATION FAILED.")
        sys.exit(1)

# ============================================================
# 4. COMMAND BRAINS
# ============================================================
class Brains:
    @staticmethod
    def remote_control(line):
        """Logic for Edit/%remote with Password Gate"""
        if password_gate():
            print(">> [REMOTE] OPENING NETWORK-SHARING CHANNEL...")
            print(">> [REMOTE] SYNCING PACKETS... [99.9%]")
            print(">> [REMOTE] CONTROL ESTABLISHED.")

    @staticmethod
    def file_access():
        print(">> [FILE] ^%FILE-ACCESS: GRANTED.")

    @staticmethod
    def network_kill():
        print(">> [NET] EXECUTING FORCE STOP...")
        # os.system("net stop 'Workstation' /y")

# ============================================================
# 5. CORE ENGINE & POLYGLOT PARSER
# ============================================================
class FlitteryEngine:
    def __init__(self, script_path):
        # Initial Boot Sequence
        run_security_protocol()
        self.ram_lock = engage_memory_lock()
        
        if not os.path.exists(script_path):
            print("!! [ERR] SCRIPT NOT FOUND.")
            sys.exit(1)
            
        with open(script_path, 'r') as f:
            self.code = f.read()

    def run(self):
        print(">> [VAN] BOOTING ENGINE... ALL BRAINS LOADED.")
        
        # Pre-scan for UVAN
        if "UVAN .7.0" in self.code:
            if not os.path.exists(INTERNAL_CONFIG["UVAN_PATH"]):
                print("!! [ERR] BRAIN UVAN .7.0 NOT INSTALLED AT C:/UVAN")
                return

        # Line-by-Line Execution
        lines = self.code.split('\n')
        for line in lines:
            line = line.strip()
            if not line or line.startswith("#$"): continue

            # ADMIN LOGIC
            if "admin<=else" in line:
                print(">> [CONTEXT] PRIVILEGE CHECK: OK.")

            # PASSWORD PROTECTED COMMAND
            if "Edit/%remote" in line:
                Brains.remote_control(line)

            # STANDARD CMDS
            if "^%FILE-ACCESS" in line: Brains.file_access()
            if "force net stop else" in line: Brains.network_kill()
            if "admin:yes" in line: print(">> [CMD] NET USER /ACTIVE:YES")
            
            # ROOT FLAGS
            if "ZZX" in line or "LL!@M" in line:
                print(f">> [ROOT] EXECUTING: {line}")

            # POLYGLOT: JAVASCRIPT
            if "[JS]" in line:
                js_match = re.search(r'\[JS\](.*?)\[/JS\]', line)
                if js_match:
                    try:
                        res = js2py.eval_js(js_match.group(1))
                        print(f">> [JS_RES] {res}")
                    except Exception as e:
                        print(f"!! [JS_ERR] {e}")

# ============================================================
# 6. RUNTIME ENTRY
# ============================================================
def main():
    if len(sys.argv) < 2:
        print("Usage: flit <filename.flit>")
    else:
        # Pass the first argument (the script name) to the engine
        engine = FlitteryEngine(sys.argv[1])
        engine.run()

if __name__ == "__main__":
    main()
