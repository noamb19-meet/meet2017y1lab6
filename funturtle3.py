
UP_ARROW="Up"
LEFT_ARROW="Left"
DOWN_ARROW="Down"
RIGHT_ARROW="Right"
SPACEBAR="space"

UP=0
DOWN=1
LEFT=2
RIGHT=3
direction=UP

def up ():
    global direction
    direction=UP
    print("you pressed up")
def down ():
    global direction
    direction=DOWN
    print("down")
    
def left ():
    global direction
    direction=LEFT
    print("left")    
def right():
    global direction
    direction=RIGHT
    print("right")
    
    

    
