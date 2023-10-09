def add_new_country(Country, Visits, Cities):
    new_country = {}
    new_country["Country"] = Country
    new_country["Visits"] = Visits
    new_country["Cities"] = Cities
    travel_log.append(new_country)


travel_log = [
{
    "Country": "France",
    "Visits": 12, 
    "Cities": ["Paris", "Lille", "Dijon"],
},
{
    "Country": "Germany",
    "Visits": 5,
    "Cities": ["Berlin", "Hamburg", "Stuttgart"],
},
]



add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

print(travel_log)