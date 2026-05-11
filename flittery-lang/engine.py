import sys, os, psutil, js2py, gc, re, time, getpass

# ============================================================
# 1. THE BRAIN CONFIGURATION (Identity & Command Map)
# ============================================================
INTERNAL_CONFIG = {
    "AUTH_USER": "turtl",
    "GATE_PASS": "turtl",
    "CREATOR_ID": "turtleboyagain120",
    "UVAN_REQ": 5 * (1024**3), # 5GB for UVAN Logic
    "CMD_REQ": 3 * (1024**3)   # 3GB for CMD Engine
}

# HYBRID MAP: Fixed (Exact) vs Substring (Keywords)
COMMAND_MAP = {
    "fixed": {
        "Edit/%remote": "REMOTE_GATE",
        "admin [AUTH] WELCOME {INTERNAL_CONFIG['AUTH_USER']}")
    print(f">> [VAN] MEMORY PARTITIONED: 5GB UVAN | 3GB CMD")
    return uvan_core, cmd_core

def password_gate():
    if input("ENTER ACCESS KEY: ") == INTERNAL_CONFIG["GATE_PASS"]:
        print(">> [LOCKED] ACCESS GRANTED."); return True
    print("!! INCORRECT KEY."); return False

# ============================================================
# 3. ADVANCED LOGIC BRAIN
# ============================================================
class Brains:
    @staticmethod
    def execute_hybrid(action, line):
        if action == "REMOTE_GATE":
            if password_gate(): print(">> [REMOTE] CONTROL ESTABLISHED.")
        elif action == "FILE_BRAIN": print(">> [FILE] ^%FILE-ACCESS: UNLOCKED.")
        elif action == "NET_KILL": print(">> [NET] EXECUTING FORCE STOP.")
        elif action == "ADMIN_MACRO": print(">> [CMD] NET USER /ACTIVE:YES")
        elif action == "PRIV_CHECK": print(">> [CONTEXT] PRIVILEGE CHECK: OK.")
        elif "FLAG" in action: print(f">> [ROOT] EXECUTING: {line}")

    @staticmethod
    def execute_complex(line):
        # 1. Conditionals
        if "CMD:yes" in line: print(">> [IF] CMD ACTIVE -> {hello}")
        
        # 2. String Logic (outputx!000)
        if "outputx!000" in line:
            test = "RUN" # 3 letters
            if len(test) == 3: print(f">> [LOGIC] 3 CHARS -> TEMP_MEM: '3'")
        
        # 3. 12x Loop & Force Operators
        if "for 12 in number" in line:
            # Check for Force (") or Double Force ("")
            force = "DOUBLE_FORCE" if '""' in line else ("FORCE" if '"' in line else "NORMAL")
            print(f">> [LOOP] 12x BREAK | MODE: {force}")
            for i in range(12): print(f"   [{i+1}] __break-com!__")
            
        # 4. Terminator
        if INTERNAL_CONFIG["CREATOR_ID"] in line:
            print(f"\n>> [EXIT] CREATOR {INTERNAL_CONFIG['CREATOR_ID']} ENDED PROCESS.")
            print(f">> [LOC] ENGINE AT: {os.path.abspath(__file__)}")
            sys.exit(0)

# ============================================================
# 4. THE ENGINE
# ============================================================
class FlitteryEngine:
    def __init__(self, script_path):
        self.uvan, self.cmd = system_boot()
        if not os.path.exists(script_path): sys.exit(1)
        with open(script_path, 'r') as f: self.code = f.read()

    def run(self):
        print(">> [VAN] ENGINE ONLINE. UVAN RAM BRAIN READY.")
        for line in self.code.split('\n'):
            line = line.strip()
            if not line or line.startswith("#$"): continue

            # Priority 1: Complex Logic & Loops
            Brains.execute_complex(line)

            # Priority 2: Fixed Commands
            if line in COMMAND_MAP["fixed"]:
                Brains.execute_hybrid(COMMAND_MAP["fixed"][line], line)
                continue

            # Priority 3: Substring Triggers
            for trigger, action in COMMAND_MAP["substring"].items():
                if trigger in line: Brains.execute_hybrid(action, line)

            # Priority 4: Polyglot JS
            if "[JS]" in line:
                match = re.search(r'\[JS\](.*?)\[/JS\]', line)
                if match:
                    try: print(f">> [JS] {js2py.eval_js(match.group(1))}")
                    except Exception as e: print(f"!! [JS_ERR] {e}")

def main():
    if len(sys.argv) > 1:
        # Use the actual filename provided to the 'flit' command
        FlitteryEngine(sys.argv[1]).run()
    else:
        print("Usage: flit <script.flit>")

if __name__ == "__main__":
    main()
