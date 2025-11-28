import os
import hashlib
from functools import reduce

EMAIL = "isfandiyorazimboyev@email.com".lower()
PATH = "C:/Users/Isfandiyor/Desktop/Itransition-Internship-Tasks/Task2/task2"

def sha3_file(path):
    with open(path, "rb") as f:
        return hashlib.sha3_256(f.read()).hexdigest()

def product_key(hashstr):
    return reduce(lambda a,b: a*b, [(int(c, 16) + 1) for c in hashstr])

# 1. Read all hashes
hashes = []
for filename in sorted(os.listdir(PATH)):
    file_path = os.path.join(PATH, filename)
    if os.path.isfile(file_path):
        h = sha3_file(file_path)
        hashes.append(h)

# 2. Sort by product key
hashes.sort(key=product_key)

# 3. Join without separator
joined = "".join(hashes)

# 4. Add email
joined_with_email = joined + EMAIL

# 5. First SHA3-256
h1 = hashlib.sha3_256(joined_with_email.encode()).hexdigest()

# 6. Second round
# Only one hash, sorting changes nothing
h2_input = h1 + EMAIL
final = hashlib.sha3_256(h2_input.encode()).hexdigest()

print(final)
