def make_car(manufacturer, model, **options):
    car_dict = {
        'manufacturer': manufacturer.title(),
        'model': model.title(),
        }
    for option, value in options.items():
        car_dict[option] = value

    return car_dict

my_outback = make_car('subaru', 'outback', 
	color='blue', tow_package=True)
print(my_outback)

my_accord = make_car('ford ,motor company','ford', 
	color='silver', founder='henry ford ')
print(my_accord)