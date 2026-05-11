import sys, os, psutil, js2py, gc, re, time

# ============================================================
# SECTION 1: THE BRAIN STEM (Command Logic)
# ============================================================
# To add a new command, write a function here and register it below.

def cmd_admin_active(line):
    # Logic for: admin:yes
    print(">> [SYSTEM] SETTING ACTIVE USER TO ADMIN...")
    # In real life: os.system("net user administrator /active:yes")
    return True

def cmd_file_access(line):
    # Logic for: ^%FILE-ACCESS
    print(">> [PERM] UNLOCKING FILESYSTEM CONTROL (777)...")
    return True

def cmd_remote_connect(line):
    # Logic for: ^%REMOTE-COMPUTER
    # Extracts IP if written like ^%REMOTE-COMPUTER=192.168.1.5
    target = line.split("=")[1] if "=" in line else "DEFAULT_GATEWAY"
    print(f">> [NET] TUNNELING TO {target}...")
    time.sleep(0.5)
    print(">> [NET] CONNECTION ESTABLISHED.")
    return True

def cmd_network_kill(line):
    # Logic for: force net stop else
    print(">> [KILLSWITCH] TERMINATING NETWORK ADAPTERS...")
    # os.system("ipconfig /release")
    print(">> [KILLSWITCH] OFFLINE.")
    return True

def cmd_custom_hello(line):
    # YOU CAN ADD THIS!
    print(">> [CUSTOM] Hello from your new command!")
    return True

# ============================================================
# SECTION 2: THE REGISTRY (Add your commands here)
# ============================================================
# The engine looks here. If it finds the "Trigger" text, it runs the Function.
COMMAND_MAP = {
    "admin:yes": cmd_admin_active,
    "^%FILE-ACCESS": cmd_file_access,
    "^%REMOTE-COMPUTER": cmd_remote_connect,
    "force net stop else": cmd_network_kill,
    "HELLO_WORLD": cmd_custom_hello,  # Example of a new command
    "ZZX": lambda x: print(">> [ROOT] ELEVATION: SYSTEM"), # Quick inline command
    "LL!@M": lambda x: print(">> [ROOT] ELEVATION: KERNEL"),
}

# ============================================================
# SECTION 3: CORE ENGINE (Do not touch unless upgrading)
# ============================================================
class Flittery:
    def __init__(self, file):
        if not os.path.exists(file): print("!! FILE NOT FOUND"); sys.exit(1)
        self.code = open(file).read()
        self.lock_memory()

    def lock_memory(self):
        # The 8GB Lock Requirement
        req = 8 * (1024**3)
        if psutil.virtual_memory().available < req:
            print("!! FATAL: 8GB RAM REQUIRED FOR VAN ENGINE")
            sys.exit(1)
        self._mem = bytearray(req) # Reserve RAM

    def run(self):
        print(">> VAN ENGINE: ONLINE. MEMORY LOCKED.")
        
        # Pre-Scan for Dependencies
        if "UVAN .7.0" in self.code and not os.path.exists("C:/UVAN"):
            print("!! ERROR: BRAIN [UVAN .7.0] MISSING")
            return

        # Main Execution Loop
        lines = self.code.split('\n')
        for line in lines:
            line = line.strip()
            if not line or line.startswith("#$"): continue

            # 1. Check for JS Blocks
            if "[JS]" in line:
                js = re.search(r'\[JS\](.*?)\[/JS\]', line)
                if js: 
                    try: print(f">> [JS] {js2py.eval_js(js.group(1))}")
                    except Exception as e: print(f"!! [JS ERROR] {e}")
                continue

            # 2. Check Command Registry
            executed = False
            for trigger, function in COMMAND_MAP.items():
                if trigger in line:
                    function(line)
                    executed = True
            
            # 3. Fallback for standard text or unknown commands
            if not executed and "=" in line:
                print(f">> [VAR] PARSED: {line}")

def main():
    if len(sys.argv) > 1:
        app = Flittery(sys.argv[1])
        app.run()
    else:
        print("Usage: flit <your_script.flit>")

if __name__ == "__main__":
    main()
