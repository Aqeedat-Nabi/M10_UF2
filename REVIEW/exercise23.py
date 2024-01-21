import json

def json_file():
    
    books = []

    books.append({
        "id": 1 ,
        "title": "Cosmos",
        "cover": "Cosmos.jpg",
        "year": 1990,
        "pages": 500
    })

    books.append({
        "id": 2 ,
        "title": "A Journey Through Space",
        "cover": "GalaxyExplorer.jpg",
        "year": 2005,
        "pages": 350
    })

    books.append({
        "id": 3 ,
        "title": "A Brief History of Time",
        "cover": "Time.jpg",
        "year": 2012,
        "pages": 200
    })

    books.append({
        "id": 4 ,
        "title": "Gravity's Rainbow",
        "cover": "Gravity.jpg",
        "year": 1850,
        "pages": 600
    })
    
    books.append({
        "id": 5 ,
        "title": "Black Holes and Baby Universes",
        "cover": "MysticalScrolls.jpg",
        "year": 1850,
        "pages": 600
    })

    json_data = {"book": books}

    print("JSON Content:")
    print(json.dumps(json_data, indent=2))

    with open("exercise23.json", "wt") as json_file:
        json.dump(json_data, json_file, indent=2)

json_file()
