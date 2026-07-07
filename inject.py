import subprocess, re
tok = subprocess.run(['gh','auth','token'], capture_output=True, text=True).stdout.strip()
print('Token len:', len(tok), 'starts:', tok[:7])

path = r'C:\Users\kovash\Desktop\postavki-github\index.html'
with open(path, encoding='utf-8') as f:
    content = f.read()

# Find the placeholder line and replace it
content = re.sub(
    r"const CLOUD_TOKEN\s*=\s*'***'\s*;",
    f"const CLOUD_TOKEN='{tok}';",
    content
)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

# Verify
with open(path, encoding='utf-8') as f:
    c2 = f.read()
m = re.search(r"const CLOUD_TOKEN='([^']+)'", c2)
if m:
    print('Injected:', m.group(1)[:10] + '...')
else:
    print('FAILED - CLOUD_TOKEN line not found')
