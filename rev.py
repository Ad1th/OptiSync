import json

# Function to reverse a string
def reverse_string(s):
    return s[::-1]

# File path where the message is stored
MESSAGE_FILE = "message.json"

if __name__ == "__main__":
    try:
        print("Attempting to read the message file...")
        # Read the message from the file
        with open(MESSAGE_FILE, "r") as file:
            data = json.load(file)
            print(f"Data read from file: {data}")
            message = data.get("message", "")
        
        if message:
            # Reverse and print the message
            reversed_message = reverse_string(message)
            print(f"Reversed Message: {reversed_message}")
        else:
            print("No message available to reverse.")
    except FileNotFoundError:
        print("Message file not found. Please submit data first.")
    except Exception as e:
        print(f"An error occurred: {e}")
