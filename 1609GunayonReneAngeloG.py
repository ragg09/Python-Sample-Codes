pets = []
pet = {
    'Owner': 'Lelouch',
    'Animal type': 'Bird',
    'Name': 'Mingming',
}
pets.append(pet)
pet = {
    'Owner': 'Evad',
    'Animal type': 'Turtle',
    'Name': 'Tuck',
}
pets.append(pet)
pet = {
    'owner': 'Vince',
    'animal type': 'Crocodile',
    'Name': 'Crocs',
}
pets.append(pet)

for pet in pets:
    print("\nThings about " + pet['Name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))