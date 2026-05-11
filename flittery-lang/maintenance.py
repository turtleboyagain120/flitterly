# maintenance.py
import os
import shutil
import time

def wipe_logs():
    print(">> [MAINTENANCE] SCRUBBING LOG FILES...")
    # Code to delete temp files
    if os.path.exists("flittery.log"):
        os.remove("flittery.log")
    print(">> [MAINTENANCE] LOGS CLEARED.")

def verify_uvan_integrity():
    print(">> [MAINTENANCE] CHECKING UVAN STRUCTURE...")
    uvan_path = "C:/UVAN"
    if not os.path.exists(uvan_path):
        print("!! [CRITICAL] UVAN MISSING. REPAIRING...")
        os.makedirs(uvan_path, exist_ok=True)
        print(">> [REPAIR] UVAN DIRECTORY RESTORED.")
    else:
        print(">> [STATUS] UVAN CORE HEALTHY.")

def full_system_flush():
    wipe_logs()
    verify_uvan_integrity()
    print(">> [MAINTENANCE] SYSTEM FLUSH COMPLETE.")
