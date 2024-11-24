while True:
    city=input("Please enter the name of a city you have to visit:")
    print(str(city))
    prompt=input("\nEnter 'quit' when you are finished.")
    if prompt == 'quit':
        break
    else:
        print("I'd love to go to " ,city, "!")
    print()