import sys, os, psutil, js2py, gc, re

# --- BRAIN & MEMORY LOGIC ---
def lock_8gb_ram():
    if psutil.virtual_memory().available < 8*1024**3:
        print("FATAL: NEED 8GB RAM"); sys.exit(1)
    return bytearray(8*1024**3)

class Flittery:
    def __init__(self, file):
        self.code = open(file).read()
        self.lock = lock_8gb_ram()

    def run(self):
        # 1. SCAN FOR BRAINS (UVAN / UBUNTU)
        if "UVAN .7.0" in self.code and not os.path.exists("C:/UVAN"):
            print("ERROR: UVAN BRAIN MISSING"); return
        
        # 2. EXECUTE LINE BY LINE
        for line in self.code.split('\n'):
            line = line.strip()
            if not line or line.startswith("#$"): continue
            
            # Syntax Logic
            if "admin:yes" in line: print("EXEC: net user admin /active:yes")
            if "^%FILE-ACCESS" in line: print("ACCESS: Filesystem Unlocked")
            if "ZZX" in line or "LL!@M" in line: print("ROOT: Elevation Active")

def main():
    if len(sys.argv) > 1:
        app = Flittery(sys.argv[1])
        app.run()
    else:
        print("Usage: flit <filename.flit>")

if __name__ == "__main__":
    main()

