#A function that maps a value (var) tha's in a initial range (min -> max) to another range (n_min -> n_max)
#inspired by the map() function in the p5.js framework: https://p5js.org/reference/#/p5/map

def map(var, min, max, new_min, new_max):
	#raises value error if the number to be mapped is outside the given initial range
	if var < min or var > max:
		raise ValueError("Variable outside initial range")
	#Re-maps a number (var) from one range to another
	mapped_value = ((var - min) / (max -min)) * (new_max - new_min) + new_min
	return mapped_value
