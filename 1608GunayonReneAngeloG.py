rivers = {
    'Ganghes': 'Vietnam',
    'Amazon': 'America',
    'Pasig': 'Philippines',
    }

for river, country in rivers.items():
    print("The" + river.title() + " can be found in " + country.title() + ".")

print("\nThe Three Rivers in the World:")
for river in rivers.keys():
    print("" + river.title())

print("\nThe countries that rivers were located:")
for country in rivers.values():
    print("" + country.title())