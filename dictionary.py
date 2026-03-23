c_dictionary = {
    "Array": "An ordered collection of items, which can be of any type.",
    "Dictionary": "A collection of key-value pairs, where each key is unique"
}
for key in c_dictionary:
    print(f"{key}: {c_dictionary[key]}")

#list in dictionary
travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
}

print(travel_log["France"]["cities_visited"])
print(travel_log["Germany"]["cities_visited"])