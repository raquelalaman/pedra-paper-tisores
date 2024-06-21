hand = 0

def on_gesture_shake():
    global hand
    hand = randint(1, 3)
    if hand == 1:
        pass
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
