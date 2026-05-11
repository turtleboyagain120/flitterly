import sys, json, js2py, re, os, subprocess

# Try to load YAML/TOML support if installed
try: import yaml
except ImportError: yaml = None
try: import tomllib
except ImportError: tomllib = None

def main():
    if len(sys.argv) < 2:
        print("!! ERROR: No .flit file provided !!")
        return

    # 1. LOAD CONFIG (Supports JSON, YAML, or TOML)
    cfg = {"user": "default", "admin": False, "access": 0}
    for ext in ['config.json', 'config.yml', 'config.toml']:
        if os.path.exists(ext):
            with open(ext, 'r') as f:
                if ext.endswith('.json'): cfg.update(json.load(f))
                elif ext.endswith('.yml') and yaml: cfg.update(yaml.safe_load(f))
                elif ext.endswith('.toml') and tomllib: cfg.update(tomllib.loads(f.read()))
            print(f"[SYSTEM] Configuration loaded from {ext}")
            break

    # 2. READ SOURCE CODE
    with open(sys.argv[1], 'r') as f:
        code = f.read()

    # 3. PRE-SCANNER (Requirements Check)
    print("--- SCANNING FOR REQUIREMENTS ---")
    if "UVAN .7.0" in code or "ubuntulatest" in code:
        if not os.path.exists("C:/UVAN"):
            print("!! FATAL ERROR: UVAN .7.0 (ubuntulatest) NOT FOUND !!")
            return
        print("[CHECK] UVAN .7.0 Verified.")

    # 4. JAVASCRIPT ENGINE (Isolated Logic)
    if "[JS]" in code:
        print("[JS] Executing Logic Block...")
        js_blocks = re.findall(r'\[JS\](.*?)\[/JS\]', code, re.S)
        for block in js_blocks:
            try:
                js_context = js2py.EvalJs()
                js_context.execute(block)
            except Exception as e:
                print(f"[JS ERROR] {e}")

    # 5. CORE COMMAND PARSER
    print("--- EXECUTING COMMANDS ---")
    for line in code.split('\n'):
        line = line.strip()
        if not line or line.startswith("#$"): continue # Ignore notes

        # Admin Elevation
        if any(tag in line for tag in ["ZZX", "LL!@M", "admin<=else"]):
            print(f"[AUTH] Admin Privilege Escalation: ACTIVE")

        # Identity Checks
        if "@?" in line:
            person = re.search(r'@\?(\w+)', line).group(1)
            print(f"[ID] Verifying Identity: {person}...")

        # System Actions
        if "admin:yes" in line:
            target = cfg.get('user', 'administrator')
            print(f"[SYSTEM] CMD: net user {target} /active:yes")
            # subprocess.run(["net", "user", target, "/active:yes"]) # Uncomment to make live

        if "^%FILE-ACCESS" in line:
            print(f"[ACCESS] Granting Full File Control to {cfg['user']}")

        if "^%REMOTE-COMPUTER" in line:
            print(f"[REMOTE] Opening Connection to Remote Host...")

        if "force net stop else" in line:
            print("[CRITICAL] Forcing Net Stop Services...")

    print("--- PROGRAM FINISHED ---")

if __name__ == "__main__":
    try: main()
    except Exception as e: print(f"!! CRASH: {e} !!")
