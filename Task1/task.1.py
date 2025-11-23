import json
import re
import mysql.connector

# 1. Load invalid JSON and fix it
with open("valid.json", "r", encoding="utf-8") as f:
    raw = f.read()

# Fix invalid format: wrap with [] if needed
if not raw.strip().startswith("["):
    raw = "[" + raw + "]"

# Replace Ruby hash syntax => JSON
raw = raw.replace("=>", ":")

data = json.loads(raw)

# 2. Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234567Is!",
    database="books"
)
cursor = db.cursor()

# 3. Insert cleaned data
for item in data:
    price_str = item["price"]
    currency = price_str[0]
    price = float(price_str[1:])

    cursor.execute("""
        INSERT INTO mybooks_table (id, title, author, genre, publisher, year, price, currency)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """, (
        str(item["id"]), item["title"], item["author"], item["genre"],
        item["publisher"], item["year"], price, currency
    ))

db.commit()
cursor.close()
db.close()
