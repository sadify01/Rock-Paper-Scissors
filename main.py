h = None

def on_gesture_shake():
    global h
    h = randint(1, 3)

    if h == 1:
        basic.show_icon(IconNames.SMALL_SQUARE)
    elif h == 2:
        basic.show_icon(IconNames.SQUARE)
    elif h == 3:
        basic.show_icon(IconNames.SCISSORS)

input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_a():
    if True:
        basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    if True:
        basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)