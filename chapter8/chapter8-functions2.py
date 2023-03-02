#!/usr/bin/env python
"""
def city_country(city, country):
	city1 = 'Santiago' 
	country1 = 'Chile'
	citY2 = 'New York' 
	country2 = 'United States'
	city3 = 'Berlin' 
	country3 = 'Germany'
	
	return '{}.{}'.format 

city_country(city1, country)
"""
"""
def city_country():
	pair = 'santiago, chile'
	pair1 = 'new york, united states'
	pair2 = 'berlin, germany'
	return pair
	return pair1
	return pair2

print(city_country().title())
"""

def city_country(city, country):
	return f"{city.title()}, {country.title()}"

pair0 = city_country('santiage', 'chile')
pair1 = city_country('new york', 'united states')
pair2 = city_country('berlin', 'germany')

print(pair0)
print(pair1)
print(pair2)
