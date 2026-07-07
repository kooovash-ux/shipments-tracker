import subprocess, sys

tok = subprocess.run(['gh','auth','token'], capture_output=True, text=True).stdout.strip()
if not tok or tok.startswith('gho_') is False:
    print("Bad token:", tok[:10] if tok else "empty")
    sys.exit(1)

path = 'C:/Users/kovash/Desktop/postavki-github/index.html'
with open(path, encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    "const CLOUD_TOKEN = 'gho_***...L7YQ';",
    "const CLOUD_TOKEN = '" + tok + "';"
)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print('OK, token injected, len:', len(tok))
