# ================================
# PART 3: File I/O, API & Exception Handling
# ================================

import requests
from datetime import datetime

# ================================
# TASK 1 — FILE WRITE & READ
# ================================

# Writing to file
try:
    with open("python_notes.txt", "w", encoding="utf-8") as f:
        f.write("Topic 1: Variables store data. Python is dynamically typed.\n")
        f.write("Topic 2: Lists are ordered and mutable.\n")
        f.write("Topic 3: Dictionaries store key-value pairs.\n")
        f.write("Topic 4: Loops automate repetitive tasks.\n")
        f.write("Topic 5: Exception handling prevents crashes.\n")
    print("File written successfully.")
except Exception as e:
    print("Error writing file:", e)

# Appending to file
try:
    with open("python_notes.txt", "a", encoding="utf-8") as f:
        f.write("Topic 6: Functions help reuse code.\n")
        f.write("Topic 7: APIs allow communication between systems.\n")
    print("Lines appended successfully.")
except Exception as e:
    print("Error appending file:", e)

# Reading file
try:
    with open("python_notes.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    print("\n--- File Content ---")
    for i, line in enumerate(lines, start=1):
        print(f"{i}. {line.strip()}")

    print("Total lines:", len(lines))

    keyword = input("\nEnter keyword to search: ").lower()
    found = False

    for line in lines:
        if keyword in line.lower():
            print(line.strip())
            found = True

    if not found:
        print("No matching lines found.")

except Exception as e:
    print("Error reading file:", e)

# ================================
# TASK 2 — API INTEGRATION
# ================================

BASE_URL = "https://dummyjson.com/products"

def fetch_products():
    try:
        response = requests.get(f"{BASE_URL}?limit=20", timeout=5)
        data = response.json()

        print("\n--- Product List ---")
        print("ID | Title | Category | Price | Rating")

        for p in data["products"]:
            print(f"{p['id']} | {p['title']} | {p['category']} | ${p['price']} | {p['rating']}")

        return data["products"]

    except requests.exceptions.ConnectionError:
        print("Connection failed.")
    except requests.exceptions.Timeout:
        print("Request timed out.")
    except Exception as e:
        print("Error:", e)

products = fetch_products()

# Filter & sort
try:
    filtered = [p for p in products if p["rating"] >= 4.5]
    filtered.sort(key=lambda x: x["price"], reverse=True)

    print("\n--- Filtered Products (Rating >= 4.5) ---")
    for p in filtered:
        print(p["title"], "-", p["price"])
except:
    pass

# Category search
try:
    response = requests.get(f"{BASE_URL}/category/laptops", timeout=5)
    data = response.json()

    print("\n--- Laptops ---")
    for p in data["products"]:
        print(p["title"], "-", p["price"])
except Exception as e:
    print("Error:", e)

# POST request
try:
    new_product = {
        "title": "My Custom Product",
        "price": 999,
        "category": "electronics",
        "description": "A product I created via API"
    }

    response = requests.post(f"{BASE_URL}/add", json=new_product, timeout=5)
    print("\nPOST Response:", response.json())

except Exception as e:
    print("Error:", e)

# ================================
# TASK 3 — EXCEPTION HANDLING
# ================================

# Safe divide
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Invalid input types"

print("\nSafe Divide Tests:")
print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide("ten", 2))

# Safe file read
def read_file_safe(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    finally:
        print("File operation attempt complete.")

print("\nReading existing file:")
print(read_file_safe("python_notes.txt"))

print("\nReading missing file:")
read_file_safe("ghost_file.txt")

# Input validation loop
while True:
    user_input = input("\nEnter product ID (1-100) or 'quit': ")

    if user_input.lower() == "quit":
        break

    if not user_input.isdigit():
        print("Invalid input. Enter a number.")
        continue

    pid = int(user_input)

    if pid < 1 or pid > 100:
        print("Enter ID between 1-100.")
        continue

    try:
        res = requests.get(f"{BASE_URL}/{pid}", timeout=5)

        if res.status_code == 404:
            print("Product not found.")
        else:
            data = res.json()
            print(data["title"], "-", data["price"])

    except Exception as e:
        print("Error:", e)

# ================================
# TASK 4 — ERROR LOGGING
# ================================

def log_error(context, error_type, message):
    with open("error_log.txt", "a", encoding="utf-8") as f:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{time}] ERROR in {context}: {error_type} — {message}\n")

# Trigger ConnectionError
try:
    requests.get("https://this-host-does-not-exist-xyz.com/api", timeout=5)
except requests.exceptions.ConnectionError as e:
    print("Logging connection error...")
    log_error("fetch_products", "ConnectionError", str(e))

# Trigger 404
try:
    res = requests.get(f"{BASE_URL}/999", timeout=5)
    if res.status_code != 200:
        print("Logging 404 error...")
        log_error("lookup_product", "HTTPError", "404 Not Found for product ID 999")
except Exception as e:
    log_error("lookup_product", "Exception", str(e))

# Print log file
print("\n--- Error Log ---")
try:
    with open("error_log.txt", "r", encoding="utf-8") as f:
        print(f.read())
except:
    print("No logs found.")
