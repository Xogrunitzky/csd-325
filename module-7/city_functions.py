

def city_country(city, country, population=None, language=None):
    """
    Return a string in the format:
    City, Country [- population xxx] [, Language]
    Only include population or language if provided.
    """
    result = f"{city.title()}, {country.title()}"

    if population:
        result += f" - population {population}"
    if language:
        result += f", {language.title()}"

    return result

# Call the function at least three times
print(city_country("tokyo", "japan"))                        # City, Country
print(city_country("omaha", "united states", 500000))       # City, Country, Population
print(city_country("santiago", "chile", 5000000, "spanish"))# City, Country, Population, Language