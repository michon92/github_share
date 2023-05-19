from city_function import get_formatted_city

print("Aby zakończyć działanie programu, wpisz proszę 'Q'")
while True:
    city = input("\nPodaj nazwę miasta:\n>").upper()
    if city == 'Q':
        break
    country = input("\nPodaj nazwę państwa:\n>").upper()
    if country == 'Q':
        break
    formatted_city = get_formatted_city(city, country)
    print(f"\tNazwa miasta i państwa: {formatted_city}")