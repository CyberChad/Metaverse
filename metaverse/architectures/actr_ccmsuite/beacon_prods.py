def initializeGame(goal='play beacon:?loc_x beacon:?loc_y'):
    print("initialize the game")

def moveToBeacon(perception='?loc_x ?loc_y'):

    beacon_x = int(loc_x)
    beacon_y = int(loc_y)
    beacon_xy = [beacon_x, beacon_y]
    temp = f"click {beacon_xy}"
    print(temp)
    motor.press(beacon_xy)


