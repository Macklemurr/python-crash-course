def make_car(manufacturer, model, **features):
	car_dict = {
		'manufacturer': manufacturer.title(),
		'model': model.title(),
	}
	
	for features, value in features.items():
		car_dict[features] = value
		
	return car_dict
