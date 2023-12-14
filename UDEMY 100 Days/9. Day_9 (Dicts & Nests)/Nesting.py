# {
    # Key: [List],
    # Key2: {Dict},
# }

capitals = {
    "England": "London",
    "France": "Paris",
    "Germany": "Berlin"
}

# Nest LIST in DICT
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

# Nest DICT in DICT
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"]},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"]},
    "England": {"cities_visited": ["London", "York", "Leeds"]}
}

# Nest Dict in a LIST
travel_log = [
    {"Country": "France", 
     "cities_visited": ["Paris", "Lille", "Dijon"], 
     "total_visits": 12
    },
    {"Country": "England", 
     "cities_visited": ["London", "York", "Leeds"], 
     "total_visits": 5
    },
]