def turn_right():
    for n in range(0,3):
        turn_left()      

while not at_goal():
    if right_is_clear() and front_is_clear():
        move()
    elif right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

'''
or
while not at_goal():
    if not wall_on_right() and front_is_clear() and right_is_clear():
        turn_right()
        move()
    elif not wall_on_right() and front_is_clear():
        move()
    elif not wall_on_right() and not front_is_clear() and right_is_clear():
        turn_right()
        move()
    elif wall_on_right() and not front_is_clear():
        turn_left()
    elif not wall_on_right():
        turn_right()
    elif wall_on_right():
        move()
    else:
        turn_left()
'''
# Reeborg's world exercise: Maze

#if , elif, else
#goal is on the right => have to travel to the right

#can turn right => turn right
#can't turn right => go straight
#else: turn left

        

