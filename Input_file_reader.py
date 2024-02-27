import json

# Get the path to the JSON file
json_file_path = "input.json"

# Open the JSON file in read mode
with open(json_file_path, "r") as f:
    # Load the JSON data into a Python dictionary
    json_data = json.load(f)

# Print the JSON data
print(json_data)
