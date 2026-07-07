import subprocess, re

tok = subprocess.run(['gh','auth','token'], capture_output=True, text=True).stdout.strip()
print('Token len:', len(tok), 'starts:', tok[:7])

path = r'C:\Users\kovash\Desktop\postavki-github\index.html'
with open(path, encoding='utf-8') as f:
    content = f.read()

# The security tool replaced the token with '***' - find and replace back
content = content.replace(
    "const CLOUD_TOKEN='***';",
    "const CLOUD_TOKEN='" + tok + "';"
)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

# Verify
with open(path, encoding='utf-8') as f:
    c2 = f.read()
line = [l for l in c2.split('\n') if 'CLOUD_TOKEN=' in l][0]
print('Result line:', line.strip())
