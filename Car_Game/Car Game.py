# Car Game (Python Console App)
#
# A simple text-based game where the user controls a virtual car using commands.
#
# How to play:
# Type commands when prompted:
# - help → show available commands
# - start → start the car
# - stop → stop the car
# - quit → exit the game
#
# The game runs in a loop until you type "quit".
# Any invalid input will show an error message.
#
# Youssif Mossad - 12 June 2026
print("Welcome to the car game!")
while True:
    operation=input("what to do?")
    if operation =="help":
        print(""" Start _ to start the car
    Stop _ to stop the car
    Quit _ to exit the game""")
    elif operation.lower() == "start":
        print("Car started ...Ready to go!")
    elif operation.lower() == "stop":
        print("Car Stopped!")
    elif operation.lower() == "quit":    
        print("Exiting the game...")
        break
    else:
        print("I don't understand the operation .......")
print("""Thanks for playing the game
I hope you enjoyed it!!!""")
