name_prompt = "What's your name: "
place_prompt = "Place you want to go: "
continue_prompt = "Would you like to let someone else respond?(yes/no):  "

# Responses will be stored in the form {name: place}.
responses = {}

while True:
    # Ask the user where they'd like to go.
    name = raw_input(name_prompt)
    place = raw_input(place_prompt)

    # Store the response.
    responses[name] = place

    # Ask if there's anyone else responding.
    repeat = raw_input(continue_prompt)
    if repeat != 'yes':
        break

# Show results of the survey.
print("\n--- Results ---")
for name, place in responses.items():
    print(name.title() + " would like to visit " + place.title() + ".")