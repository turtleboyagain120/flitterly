import sys, os, psutil, js2py, gc, re, time, getpass

# ============================================================
# 1. UVAN CONFIG & HYBRID COMMAND MAP
# ============================================================
UVAN_CONFIG = {
    "USER": "turtl",
    "KEY": "turtl",
    "TERM": "turtleboyagain120",
    "UVAN_PATH": "C:/UVAN",
    "TOTAL_LOCK_GB": 8,
    "ZZX_GB": 1,    # Dedicated ZZX Cache
    "LL_GB": 1,     # Dedicated LL!@M Wrapper
    "BRAIN_GB": 3,  # RAM-based buffer
    "CMD_GB": 3     # Execution engine
}

COMMAND_MAP = {
    "fixed": {
        "Edit/%remote": "REMOTE_GATE",
        "Files^%": "FILE_BRAIN",
        "Net!STOP": "NET_KILL"
    },
    "substring": {
        "ZZX": "ADMIN_ELEVATION",
        "LL!@M": "ADMIN_WRAPPER",
        "??PRO": "PRIV_CHECK"
    }
}

# ============================================================
# 2. SECURITY: IDENTITY & PASSWORD GATE
# ============================================================
def verify_identity():
    if getpass.getuser() != UVAN_CONFIG["USER"]:
        print(f"!! [UVAN_AUTH_FAIL] UNAUTHORIZED ACCESS.")
        sys.exit(1)
    print(f">> [SECURITY] UVAN IDENTITY CONFIRMED: {UVAN_CONFIG['USER']}")

# ============================================================
# 3. UVAN MEMORY LOCK (8GB WITH 1GB DEDICATED SLICES)
# ============================================================
def lock_uvan_memory():
    print(f">> [SYSTEM] INITIATING 8GB UVAN HARDWARE SACRIFICE...")
    gc.collect()
    gc.disable() 
    
    # Dedicated 1GB Admin Slices
    zzx_cache = bytearray(UVAN_CONFIG["ZZX_GB"] * (1024**3))
    ll_bridge = bytearray(UVAN_CONFIG["LL_GB"] * (1024**3))
    
    # Core Engine Partitions
    uvan_brain = bytearray(UVAN_CONFIG["BRAIN_GB"] * (1024**3))
    uvan_cmd = bytearray(UVAN_CONFIG["CMD_GB"] * (1024**3))
    
    print(f">> [SYSTEM] RAM ALLOCATED: ZZX(1GB) | LL!@M(1GB) | BRAIN(3GB) | CMD(3GB)")
    return zzx_cache, ll_bridge, uvan_brain, uvan_cmd

# ============================================================
# 4. UVAN COMMAND BRAIN
# ============================================================
class UVAN_Brains:
    @staticmethod
    def execute(action, line):
        force_lvl = 2 if line.endswith('""') else 1 if line.endswith('"') else 0
        tag = f"[UVAN_FORCE_x{force_lvl}] " if force_lvl > 0 else ">> "

        if action == "ADMIN_ELEVATION":
            print(f"{tag}[ZZX] GLOBAL ADMIN FLAG DETECTED. CACHING PRIVILEGES...")
        elif action == "ADMIN_WRAPPER":
            print(f"{tag}[LL!@M] RUNNING COMMAND THROUGH ADMIN WRAPPER...")
        elif action == "FILE_BRAIN":
            print(f"{tag}[FILE] ^%FILE-ACCESS: FULL CONTROL GRANTED.")
        
        # 12-Count Loop Logic
        if "for 12 in number" in line:
            print(f"{tag}[MAINTENANCE] RUNNING 12-COUNT CYCLE...")
            for i in range(1, 13):
                print(f"  -> {i}/12 COMPLETE")
                time.sleep(0.01)

# ============================================================
# 5. CORE ENGINE (TRANSPILER)
# ============================================================
class FlitteryEngine:
    def __init__(self, script_path):
        verify_identity()
        # Initialize the 8GB sacrifice with the new 1GB slices
        self.zzx, self.ll, self.brain, self.cmd = lock_uvan_memory()
        self.script_path = os.path.abspath(script_path)

    def run(self):
        with open(self.script_path, 'r') as f:
            code = f.read()

        # Creator Terminator (Shutdown Logic)
        if UVAN_CONFIG["TERM"] in code:
            print(f">> [TERMINATOR] SOURCE: {self.script_path} | SYSTEM SHUTDOWN.")
            os.system("shutdown /s /t 1")
            return

        # PRE-SCAN: Find ZZX/LL!@M and map them before running
        print(">> [SCAN] PRE-PROCESSING SCRIPT FOR ADMIN TRIGGERS...")
        if "ZZX" in code: print("   [CACHE] ZZX CACHE ENGAGED (1GB)")
        if "LL!@M" in code: print("   [BRIDGE] LL!@M WRAPPER ENGAGED (1GB)")

        lines = code.splitlines()
        for line in lines:
            line = line.strip()
            if not line or line.startswith("#$"): continue

            # Length-Check Brain (outputx!000)
            if "outputx!000" in line and "3 of letters" in line:
                print(">> [BRAIN] LENGTH MATCH: 3. STORED IN TEMP MEMORY.")
                continue

            # Hybrid Execution (Fixed vs Substring)
            matched = False
            if line in COMMAND_MAP["fixed"]:
                UVAN_Brains.execute(COMMAND_MAP["fixed"][line], line)
                matched = True
            else:
                for trigger, action in COMMAND_MAP["substring"].items():
                    if trigger in line:
                        UVAN_Brains.execute(action, line)
                        matched = True
                        break
            
            # Polyglot JS Bridge
            if not matched and "[JS]" in line:
                js_content = re.search(r'\[JS\](.*?)\[/JS\]', line).group(1)
                try:
                    print(f">> [UVAN_JS] {js2py.eval_js(js_content)}")
                except Exception as e:
                    print(f"!! [JS_ERR] {e}")

def main():
    if len(sys.argv) < 2:
        print("FLITTERY (UVAN ENGINE) - PROVIDE .FLIT FILE")
    else:
        FlitteryEngine(sys.argv[1]).run()

if __name__ == "__main__":
    main()
