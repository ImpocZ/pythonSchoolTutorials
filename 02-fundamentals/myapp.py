import physics
"""
print(physics.time_to_travel(500, "sound"))
print(physics.fall_distance(15, "moon"))
print(physics.fall_time(500, "sun"))
earth, moon, sun
light, sound, jet
"""

GRAVITY = [
    "earth",
    "moon",
    "sun"
]
SPEEDS = [
    "light",
    "sound",
    "jet"
]

def choice():
    print("Choose a calculation to use:\n"
          "Time-to-Travel | Free Fall distance | Fall time\n"
          "      1.       |         2.         |     3.   \n" 
          )
    while(1):
        try:
            option = int(input("Enter (1-2-3); Press 0 to escape)\nEnter: "))
            if option < 0:
                raise ValueError
            elif option == 0:
                exit(option)
            elif option not in [1, 2, 3]:
                raise ValueError

            else:
                break
        except ValueError:
            print("Please enter only whole numbers and in the valid range!")
    return option

def calculator(option):

    if option == 1:
        while(1):
            try:
                distance = float(input("Please enter the distance it took the point to travel (meters): "))
                
                if distance < 0:
                    raise ValueError("Please enter numbers greater than zero.")
                break
        
            except ValueError as error:
                print(error if str(error) else error)
        
        while(1):
            try:
                speed = int(input("Select by which speed will the point travel\n"
                            "Light - 1 | Sound - 2 | Jet - 3\n"
                            "Enter: "))
                
                if speed not in [1, 2, 3]:
                    raise ValueError("Please enter valid numbers in range.")
                else:
                    speed = SPEEDS[speed - 1]
                    break
            except ValueError as error:
                print(error if str(error) else "Please try again.")
                print("\n")
        
        calcDistance = physics.time_to_travel(distance, speed)
        print(f"If you travel the distance {distance} going by a speed {physics.SPEEDS[speed]}, then you shall travel it whole in {calcDistance:.2f} seconds.", )
    elif option == 2:
        while(1):
            try:
                time = float(input("Please enter the time in seconds.\n"
                                   "Enter: "))
                if time < 0:
                    raise ValueError("Number must be greater than zero.\n")
                else: break
            except ValueError as error:
                print(error if str(error) else "Please try again.")
                print("\n")
        while(1):
            try:
                gravity = int(input("Please select the gravity from the preselected ranges\n"
                                    "Earth | Moon | Sun\n"
                                    "  1.  |  2.  |  3.\n"
                                    "Enter: "))
                if gravity not in range(1, 4):
                    raise ValueError("Please enter a number in the specified range!")
                else: 
                    gravity = GRAVITY[gravity - 1]
                    break
            except ValueError as error:
                print(error if str(error) else "Please try again.")
                print("\n")
        
        result = physics.fall_distance(time, gravity)
        print(f"If we have the gravity of {physics.GRAVITIES[gravity]:.2f} m/s and we free fall for {time} seconds, then we shall free fall {result} {"meter" if result == 1 else "meters"}.\n")
    else:
        while(1):
            try:
                distance = float(input("Please enter the distance free-fallen in meters.\nEnter: "))
                if distance < 0:
                    raise ValueError("Please enter values greater than zero.")
                else: break
            except ValueError as error:
                print(error if str(error) else "Please try again.")
                print("\n")
        while(1):    
            try:
                gravity = int(input("Please select the gravity from the preselected ranges\n"
                                    "Earth | Moon | Sun\n"
                                    "  1.  |  2.  |  3.\n"
                                    "Enter: "))
                if gravity not in range(1, 4):
                    raise ValueError("Only enter numbers in the range!")
                else:
                    gravity = GRAVITY[gravity - 1]
                    break
            except ValueError as error:
                print(error if str(error) else "Please try again.")
                print("\n")
        
        result = physics.fall_time(distance, gravity)
        print(f"If we travel the distance of {distance} {"meter" if distance == 1 else "meters"} with the gravity of {physics.GRAVITIES[gravity]:.2f} m/s, then we have free-falled for {result:.2f} {"second" if result == 1 else "seconds"}.\n")
                

calculator(choice())