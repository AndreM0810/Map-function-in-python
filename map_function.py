#a function that maps a value (var) that is in a initial range (min -> max) to another range (n_min -> n_max)

#this function can be useful for a lot of things. Normalizing a vector, for example.

def map(var, min, max, n_min, n_max):
	if var < min or var > max:
		raise ValueError("Variable outside initial range")
	mapped_value = ((var - min) / (max -min)) * (n_max - n_min) + n_min
	return mapped_value

#One exemplo of the many things it can do.
#Given the value 10 wich goes between 0 and 100 map it to go between 0 and 10.
#The function should return 0.1s
value = 10

new_x = map(value, 0, 100, 0, 10)

print(new_x)	