def make_sandwich(*items):
    print("\nSandwich will be served soon:")
    for item in items:
        print("Putting " + item.title() + " to your sandwich.")
    print("\n\nYOUR SANDWICHES ARE READY!")

make_sandwich('ham burger', 'chicken', 'lettuce', 'egg omellet')
make_sandwich('cheddar cheese', 'ice cream', 'hotdog')
make_sandwich('conred beef', 'paste')
