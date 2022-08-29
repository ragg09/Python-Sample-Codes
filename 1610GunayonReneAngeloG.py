cities = {
	'Madrid': {
			'country': 'Spain',
			'population': '46.56 Million',
			'facts': 'Official language: Spanish',
			},
    'Manila': {
        'country': 'Philippines',
        'population': '103.3 Million',
        'facts': 'Official language: Filipino',
        },
    'Havana': {
        'country': 'Cuba',
        'population': '11.25 Million',
        'facts': 'Official language: Spanish',
        }
    }

for city, information in cities.items():
    country = information['country'].title()
    population = information['population']
    facts = information['facts'].title()

    print("\n" + city.title() + " can be found in " + country + ".")
    print("  The latest recorded population is " + str(population) + ".")
    print("  The " + facts + ".")