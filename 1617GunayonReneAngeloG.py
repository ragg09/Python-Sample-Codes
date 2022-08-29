size = raw_input("Enter size: ")	
text = raw_input("Enter text: ")

def make_shirt(size = "large", text = "I love PYTHON"):
	print("\tSize of shirt: " + size)
	print("\tText on shirt: " + text)

print("\nDefault shirt (LARGE)")
make_shirt()
	
print("\nDeafault shirt (MEDIUM)")	
make_shirt('medium', 'WE ARE LEGION')

print("\nThis is the shirt you've created")	
make_shirt(size, text)

