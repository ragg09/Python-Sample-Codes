text = "How old are you?"
text += "\nEnter 'quit' when you are finished. "

while True:
    age = input(text)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("Free ticket\n")
    elif age < 13:
        print("Your ticket is P10\n")
    else:
        print("  Your ticket is P15\n")