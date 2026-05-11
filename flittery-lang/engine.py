import sys, json, js2py, re

def main():
    with open(sys.argv[1], 'r') as f: code = f.read()
    with open('config.json', 'r') as j: cfg = json.load(j)

    print(f"User: {cfg['user']} | Admin: {cfg['admin']}")

    if "[JS]" in code:
        js_block = re.search(r'\[JS\](.*?)\[/JS\]', code, re.S).group(1)
        js2py.eval_js(js_block)

    for line in code.split('\n'):
        if "ZZX" in line: print("!!! ADMIN ELEVATION ACTIVE !!!")
        if "admin:yes" in line: print(f"Executing net user {cfg['user']} /active:yes")
        if "^%FILE-ACCESS" in line: print("FILE ACCESS GRANTED")

if __name__ == "__main__": main()
