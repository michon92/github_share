def get_formatted_city(city, country, population=''):
    """Funkcja generuje nazwę miasta i państwa, w którym się znajduje"""
    if population:
        # Zadanie 11.2
        full_city_country = f"{city}, {country }, populacja: {str(population)}"
    else:
        # Zadanie 11.1
        full_city_country = f"{city}, {country}"
    return full_city_country.title()
