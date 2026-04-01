# Part 3: File I/O, API & Exception Handling

import requests

def fetch_data():
    try:
        print("🌐 Fetching data from API...")
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
        response.raise_for_status()  # raise error for bad response
        data = response.json()
        return data[:5]  # take first 5 posts only
    except Exception as e:
        log_error(str(e))
        print("❌ Error fetching API data.")
        return []


def write_notes(data):
    try:
        with open("python_notes.txt", "w", encoding="utf-8") as file:
            file.write("📘 Python Notes from API\n\n")
            for item in data:
                file.write(f"Title: {item['title']}\n")
                file.write(f"Body: {item['body']}\n")
                file.write("-" * 40 + "\n")
        print("✅ Notes saved to python_notes.txt")
    except Exception as e:
        log_error(str(e))


def log_error(error_message):
    with open("error_log.txt", "a", encoding="utf-8") as file:
        file.write(error_message + "\n")


def read_notes():
    try:
        print("\n📖 Reading Notes:\n")
        with open("python_notes.txt", "r", encoding="utf-8") as file:
            print(file.read())
    except FileNotFoundError:
        print("⚠️ Notes file not found.")
    except Exception as e:
        log_error(str(e))


def main():
    data = fetch_data()
    
    if data:
        write_notes(data)
    
    read_notes()


if __name__ == "__main__":
    main()