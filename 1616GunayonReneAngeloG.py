size = raw_input("Enter size: ")	
text = raw_input("Enter text: ")

def make_shirt(size, text):
	print("Size of shirt: " + size)
	print("Text on shirt: " + text)
	
print("\nThis is the example shirt")	
make_shirt('medium', 'WE ARE LEGION')

print("\nThis is the shirt you've created")	
make_shirt(size, text)

