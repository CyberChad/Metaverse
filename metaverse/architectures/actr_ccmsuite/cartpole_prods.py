def initializeGame(goal='play pole:?polangle pole:?polevel cart:?cartpos cart:?cartvel'):
    print("initialize the game")

def observeCart(perception='?cartpos ?cartvel ?polepol ?polevel'):

    # if float(polepol) > 0.0:
    #     direction = 1

    direction = 0

    if float(cartvel) > 0:
        direction = 0
    elif float(cartvel) < 0:
        direction = 1
    else:
        direction = None

    temp = f"[CCM] ACTR.observeCart() motor.press {direction}"
    print(temp)
    motor.press(direction)


