import sys
import re
import os
import time
import platform
import psutil # Powers the ZZX force-stop logic
from colorama import init, Fore, Style

# Initialize color for the "Force" commands
init(autoreset=True)

class UVANFortress:
    VERSION = "8.0.0"
    
    def __init__(self):
        self.is_admin = False
        self.uvan_detected = False

    def scan_environment(self):
        """Build Config Check: Ensures we are on the right environment."""
        print(f"{Fore.CYAN}🛡️ UVAN FORTRESS {self.VERSION} - INITIALIZING...")
        
        # Ubuntu Check (from your notes)
        if "linux" in sys.platform.lower():
            print(f"{Fore.GREEN}✅ Environment: Ubuntu/Linux detected.")
        else:
            print(f"{Fore.YELLOW}⚠️ Warning: Non-Ubuntu environment detected.")

    def run_zzx(self, code_text):
        """The core ZZX language engine using Regex & Substring checks."""
        
        # 1. PRE-SCAN (Checks the whole file before starting)
        if "UVAN" in code_text or "ZZX" in code_text:
            self.uvan_detected = True
            print(f"{Fore.MAGENTA}✨ UVAN-ZZX Protocol Active.")

        # 2. STRIP NOTES (#$)
        clean_code = re.sub(r'#\$.*', '', code_text)

        # 3. HANDLE BREAKS (^^ = 2 seconds, ^ = 1 second)
        # Using regex to find all instances
        all_breaks = re.findall(r'\^', clean_code)
        if all_breaks:
            wait_time = len(all_breaks)
            print(f"{Fore.BLUE}⏳ Waiting {wait_time}s for system sync...")
            time.sleep(wait_time)

        # 4. ADMIN & USER LOGIC (@+user)
        user_match = re.search(r'@\+([\w-]+)', clean_code)
        if user_match:
            username = user_match.group(1)
            print(f"{Fore.GREEN}👤 User Identified: {username}")
            if "^%FILE-ACCESS" in clean_code:
                print(f"{Fore.RED}🔓 {username} -> GRANTED %FILE-ACCESS")

        # 5. OUTPUT LOGIC (!{text})
        outputs = re.findall(r'!\{([^}]+)\}', clean_code)
        for msg in outputs:
            # Check for "Force" (quotes at the end)
            if '"}' in clean_code or msg.endswith('"'):
                print(f"{Fore.RED}{Style.BRIGHT}‼️ FORCED OUTPUT: {msg.strip(chr(34))}")
            else:
                print(f"{Fore.WHITE}🗣️ Output: {msg}")

        # 6. FINISHER (The turtleboyagain120 Exit)
        if "turtleboyagain120" in clean_code:
            print(f"{Fore.CYAN}🏁 [SOURCE: turtleboyagain120] - Execution Success.")
            return True
        return False

def main():
    # This part handles the "uvan" command from your .toml
    engine = UVANFortress()
    engine.scan_environment()

    if len(sys.argv) > 1:
        # If user runs 'uvan script.zzx'
        with open(sys.argv[1], 'r') as f:
            engine.run_zzx(f.read())
    else:
        # Default test mode if no file is provided
        print(f"{Fore.WHITE}No file provided. Running internal build test...")
        test_script = 'admin<=else: UVAN ZZX ^^ @+admin ^%FILE-ACCESS !{hello"} source:?turtleboyagain120'
        engine.run_zzx(test_script)

if __name__ == "__main__":
    main()
