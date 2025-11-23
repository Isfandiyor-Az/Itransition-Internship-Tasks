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
with open("valid.json", "w", encoding="utf-8") as out:
    json.dump(data, out, indent=4, ensure_ascii=False)

print("Valid JSON saved to valid.json")






# Table 1
# CREATE TABLE mybooks_table (
#     id VARCHAR(30) PRIMARY KEY,  
#     title VARCHAR(255),
#     author VARCHAR(255),
#     genre VARCHAR(100),
#     publisher VARCHAR(255),
#     year INT,
#     price DECIMAL(10,2),
#     currency CHAR(1)
# );


# Table 2
<<<<<<< HEAD
# CREATE TABLE summary AS
=======
# CREATE OR REPLACE VIEW summary AS
>>>>>>> 70c32a6c6d1219b9cea93eabd9ff7a8557ac0c5f
# SELECT
#     year AS publication_year,
#     COUNT(*) AS book_count,
#     ROUND(
<<<<<<< HEAD
#         AVG(
#             CASE 
#                 WHEN currency = '€' THEN price * 1.2
#                 ELSE price
#             END
#         ), 2
=======
#         AVG(CASE WHEN currency = '€' THEN price * 1.2 ELSE price END), 2
>>>>>>> 70c32a6c6d1219b9cea93eabd9ff7a8557ac0c5f
#     ) AS average_price
# FROM mybooks_table
# GROUP BY year
# ORDER BY year;
