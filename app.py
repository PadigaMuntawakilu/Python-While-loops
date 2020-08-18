command = ""
started = False
while command != "quit":
    command = input("> ").lower()
    if command == "start":
            if started:
                print("Car is already started")
            else:
                started = True
            print("The car started. Ready to go.")
    elif command == "stop":
        if not started:
            print("The car is already stopped!")
        else:
            started = True
            print("The car stopped.")
    elif command == "help":
        print("""
Start to start the car.
Stop to stop the car.
And quit to quit the game
""")
    elif command == "quit":
        break
    else:
        print("I don't understand that.")