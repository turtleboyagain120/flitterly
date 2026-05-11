import getpass # This gets the computer's active username

def check_user_identity():
    current_user = getpass.getuser()
    print(f">> [SECURITY] VERIFYING USER: {current_user}")
    
    # THE LOCK: Only "turtl" can pass
    if current_user != "turtl":
        print(f"!! ACCESS DENIED: User '{current_user}' is not authorized.")
        print("!! This engine is locked to 'turtl' only.")
        sys.exit(1) # Kill the program immediately
    
    print(">> [SECURITY] IDENTITY VERIFIED. WELCOME TURTL.")
