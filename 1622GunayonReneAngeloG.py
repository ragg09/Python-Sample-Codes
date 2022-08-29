promtmult = "The product is "
promtadd = "The sum is "
class math():
	def __init__(self,x,y):
		self.x = x
		self.y = y
		
	def mult(self):
		return self.x * self.y
		
	def add(self):
		return self.x + self.y

x = input("Enter first number: ")
y = input("Enter second number: ")

test = math(x,y)
print(promtmult + str(test.mult()))
print(promtadd + str(test.add()))