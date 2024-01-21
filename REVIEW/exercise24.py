import json

def json_file_data():
    with open("exercise23.json", "r") as json_file:
        json_data = json.load(json_file)

        print("DISPLAY JSON DATA:")
        print(json.dumps(json_data, indent=2))

json_file_data()
