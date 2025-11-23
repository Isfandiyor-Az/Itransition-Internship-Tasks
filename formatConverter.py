import re
import json

with open("task1_d.json", "r", encoding="utf-8") as f:
    raw = f.read().strip()

# Wrap in array if needed
if not raw.startswith("["):
    raw = "[" + raw + "]"

# Replace Ruby => with :
raw = raw.replace("=>", ":")

# Replace Ruby symbols :key with "key"
raw = re.sub(r':([a-zA-Z_][a-zA-Z0-9_]*)', r'"\1"', raw)

# Now the content is almost JSON; ensure keys are quoted correctly
raw = re.sub(r'([{,]\s*)([a-zA-Z_][a-zA-Z0-9_]*)\s*:', r'\1"\2":', raw)

# Convert to Python object
data = json.loads(raw)

# Save as valid JSON
with open("valid2.json", "w", encoding="utf-8") as out:
    json.dump(data, out, indent=4, ensure_ascii=False)

print("Valid JSON saved to valid.json")
