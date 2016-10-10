class car(object):
	type_ = "saloon"
	model = ""
	name = ""
	num_of_doors = 0
	num_of_wheels = 0
	speed = 0

	def __int__ (self,*args):
		num_of_args = len(arg)
		if num_of_args == 0:
			name = "General"
			model = "GM"
		elif num_of_args == 1:
			name = args[0]
			model = args[1]
		elif num_of_args == 2:
			name = args[0]
			model = args[1]
			if name == "Porshe" or name == "Koenigsegg":
				num_of_doors = 2
			else:
				num_of_doors = 4
		elif num_of_args == 3:
			model = args[0]
			name = args[1]
			type_ = args[2]
			if type_ == "trailer":
				num_of_wheels = 8
			else:
				num_of_wheels = 4

	def is_saloon():
		if type_ == "saloon":
			return True
		else:
			return False
	def drive(accelerate):
		if type_ == "trailer":
			speed = accelerate * 11
		else:
			speed = (accelerate * 333) + 1
