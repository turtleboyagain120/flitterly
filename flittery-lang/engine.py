"""
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "flittery"
version = "7.0.1"
description = "UVAN Engine: High-Performance Administrative DSL (Fortress Mode)"
authors = [{name = "turtl"}]
requires-python = ">=3.8"
dependencies = ["psutil", "js2py"]
"""

import sys, os, psutil, js2py, gc, re, time, getpass
from pathlib import Path

# ============================================================
# 1. PATH & INTEGRITY CONFIG
# ============================================================
VERSION = "7.0.1"
BASE_PATH = Path("FLITTERY LANGUAGE").resolve()
UVAN_PATH = Path("C:/UVAN")
INTEGRITY_FILE = UVAN_PATH / ".integrity"

UVAN_CONFIG = {
    "USER": "turtl", 
    "TERM": "turtleboyagain120",
    "TOTAL_LOCK_GB": 8, 
    "ZZX_GB": 1, 
    "LL_GB": 1, 
    "BRAIN_GB": 3, 
    "CMD_GB": 3
}

COMMAND_MAP = {
    "fixed": {"Edit/%remote": "REMOTE_GATE", "Files^%": "FILE_BRAIN", "Net!STOP": "NET_KILL"},
    "substring": {"ZZX": "ADMIN_ELEVATION", "LL!@M": "ADMIN_WRAPPER", "??PRO": "PRIV_CHECK"}
}

# ============================================================
# 2. INTEGRITY & MAINTENANCE SYSTEM
# ============================================================
def setup_uvan_partitions():
    try:
        UVAN_PATH.mkdir(parents=True, exist_ok=True)
        (UVAN_PATH / "ZZX_Cache").mkdir(exist_ok=True)
        (UVAN_PATH / "LL_Wrapper").mkdir(exist_ok=True)
        INTEGRITY_FILE.write_text(VERSION)
        print(f">> [REPAIR] PARTITIONS REBUILT TO v{VERSION}.")
    except Exception as e:
        print(f"!! [HARDWARE_ERR] UNABLE TO ACCESS {UVAN_PATH}: {e}")

def verify_uvan_integrity():
    if not UVAN_PATH.exists() or not INTEGRITY_FILE.exists():
        print("!! [NEW/OUTDATED] ALLOCATING UVAN SLICES...")
        setup_uvan_partitions()
    elif INTEGRITY_FILE.read_text().strip() != VERSION:
        print(f"!! [UPGRADE] SYNCING v{VERSION}...")
        setup_uvan_partitions()
    else:
        print(">> [SYNCED] ENGINE AND PATHS ARE UP TO DATE.")

def full_system_flush():
    print(">> [SCRUB] CLEARING VOLATILE LOGS...")
    if BASE_PATH.exists():
        for log in BASE_PATH.glob("*.log"):
            try: log.unlink(); print(f"   - {log.name} DELETED.")
            except: pass
    print(">> [LOOP] INITIATING 12-COUNT MAINTENANCE...")
    for i in range(1, 13):
        time.sleep(0.01)
        print(f"   [{i}/12] STATUS: FORCE_M_LVL_1 \"\"")

# ============================================================
# 3. CORE ENGINE (UVAN DSL)
# ============================================================
def verify_identity():
    if getpass.getuser() != UVAN_CONFIG["USER"]:
        print(f"!! [UVAN_AUTH_FAIL] UNAUTHORIZED.")
        sys.exit(1)

def lock_uvan_memory():
    gc.collect(); gc.disable()
    print(f">> [SYSTEM] ALLOCATING {UVAN_CONFIG['TOTAL_LOCK_GB']}GB UVAN SLICES...")
    return [bytearray(UVAN_CONFIG[k] * (1024**3)) for k in ["ZZX_GB", "LL_GB", "BRAIN_GB", "CMD_GB"]]

class UVAN_Brains:
    @staticmethod
    def execute(action, line):
        force_lvl = 2 if line.endswith('""') else 1 if line.endswith('"') else 0
        tag = f"[FORCE_x{force_lvl}] " if force_lvl > 0 else ">> "
        print(f"{tag}[{action}] Executed.")
        if "for 12 in number" in line:
            for i in range(1, 13):
                print(f"  -> {i}/12 COMPLETE"); time.sleep(0.01)

class FlitteryEngine:
    def __init__(self):
        verify_identity()
        verify_uvan_integrity()
        full_system_flush()
        self.mem = lock_uvan_memory()

    def process_line(self, line):
        line = line.strip()
        if not line or line.startswith("#$"): return
        if UVAN_CONFIG["TERM"] in line:
            print("!! [TERMINATOR] SHUTDOWN."); os.system("shutdown /s /t 1"); return

        # Measures
        if "outputx!000" in line and "3 of letters" in line:
            print(">> [BRAIN] MEASURE: LENGTH 3 CACHED."); return

        matched = False
        if line in COMMAND_MAP["fixed"]:
            UVAN_Brains.execute(COMMAND_MAP["fixed"][line], line)
            matched = True
        else:
            for trigger, action in COMMAND_MAP["substring"].items():
                if trigger in line:
                    UVAN_Brains.execute(action, line)
                    matched = True; break
        
        if not matched and "[JS]" in line:
            try:
                js_code = re.search(r'\[JS\](.*?)\[/JS\]', line).group(1)
                print(f">> [UVAN_JS] {js2py.eval_js(js_code)}")
            except Exception as e: print(f"!! [JS_ERR] {e}")

    def shell(self):
        print(f"\nUVAN v{VERSION} SHELL - READY")
        while True:
            try:
                cmd = input(f"{UVAN_CONFIG['USER']}@uvan> ")
                if cmd.lower() in ['exit', 'quit']: break
                self.process_line(cmd)
            except KeyboardInterrupt: break

# ============================================================
# 4. ENTRY POINT
# ============================================================
def main():
    engine = FlitteryEngine()
    if len(sys.argv) > 1:
        # Run one-liner from CMD: python flit.py "ZZX; Files^%"
        full_code = " ".join(sys.argv[1:])
        for part in full_code.split(';'):
            engine.process_line(part)
    else:
        # Start interactive shell
        engine.shell()

if __name__ == "__main__":
    main()
