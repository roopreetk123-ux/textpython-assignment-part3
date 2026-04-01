# Product Explorer & Error-Resilient Logger (Part 3)

## 📌 Overview
This project is a Python-based application that demonstrates file handling, API integration, exception handling, and logging.  
It interacts with a public API to fetch product data, processes it, and handles errors gracefully.

---

## 🚀 Features

### 1. File Handling (Read & Write)
- Writes Python learning notes to `python_notes.txt`
- Appends additional lines to the file
- Reads and displays file content with line numbers
- Counts total lines
- Searches lines based on user input (case-insensitive)

---

### 2. API Integration
- Fetches 20 products from DummyJSON API
- Displays product details in table format
- Filters products with rating ≥ 4.5
- Sorts filtered products by price (descending)
- Fetches products from a specific category (laptops)
- Sends a POST request to simulate product creation

---

### 3. Exception Handling
- Safe division function to handle:
  - Division by zero
  - Invalid data types
- Safe file reader with:
  - FileNotFoundError handling
  - finally block execution
- API calls protected with:
  - ConnectionError
  - Timeout
  - General exception handling
- Input validation loop for product lookup

---

### 4. Error Logging System
- Logs errors into `error_log.txt`
- Includes timestamp for each error
- Handles:
  - Connection errors
  - HTTP errors (e.g., 404)
- Displays log file content at the end

---

## 🛠️ Technologies Used

- Python 3
- requests library
- datetime module
- os module (for file paths)

---

## ▶️ How to Run

1. Open terminal  
2. Navigate to project folder  
3. Run the script:

```bash
python part3_api_files.py
