class Dog:

	def __init__(self, name, age):
		self.name = name
		self.age = age


julz = Dog("Julz", 12)
jb = Dog("JB", 11)
vince = Dog("Vince", 13)

def older_dog(*args):
	return max(args)
def name_dog(*args):
	return max(args)

print("{} years old is the oldest dog".format(older_dog(julz.age, jb.age, vince.age)) + ", {} is the Oldest Dog".format(name_dog(julz.name, jb.name, vince.name)))
