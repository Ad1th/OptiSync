import json

MESSAGE_FILE = "message.json"

if __name__ == "__main__":
    try:
        print("Attempting to read the message file...")
        
        with open(MESSAGE_FILE, "r") as file:
            data = json.load(file)
            print(f"Data read from file: {data}")

        print("Entered Values:")
        for key, value in data.items():
            print(f"{key}: {value}")
        
    except FileNotFoundError:
        print("Message file not found. Please submit data first.")
    except Exception as e:
        print(f"An error occurred: {e}")
