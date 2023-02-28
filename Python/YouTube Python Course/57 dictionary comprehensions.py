#create dictionaries using an expression, can replace for loops and certain lambda functions

#dictionary = {key: expression for (key,value) in iterable}
#dictionary = {key: expression for (key,value) in iterable if conditional}
#dictionary = {key: (if/else) for (key,value) in iterable}
#dictionary = {key: function(value) for (key,value) in iterable}

#===

#convert a ditionary of fahrenheit values to celsius
cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}

#cities_in_C = {key: ((value-32)*(5/9)) for (key,value) in cities_in_F.items()}
cities_in_C = {key: round((value-32)*(5/9)) for (key,value) in cities_in_F.items()} #same as above but using the round method to round the results
print(cities_in_C)

#another example using an if statement
weather = {'New York': "snowing", 'Boston': "sunny", 'Los Angeles': "sunny", 'Chicago': "cloudy"}
sunny_weather = {key: value for (key,value) in weather.items() if value == "sunny"}
print(sunny_weather)

#another example using an if/else statement
cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
desc_cities = {key: ("WARM" if value >= 40 else "COLD") for (key,value) in cities.items()}
print(desc_cities)

#another example, this time calling a function
def check_temp(value):
    if value >= 70:
        return "HOT"
    elif 69 >= value >= 40:
        return "WARM"
    else:
        return "COLD"

cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
desc_cities = {key: check_temp(value) for (key,value) in cities.items()}
print(desc_cities)