from turtle import *

def leftturn():
    for i in range(10):
        forward(15)
        left(9)

def rightturn():
    for i in range(10):
        forward(15)
        right(9)

mode = input("Choose a mode: Pre-defined; Real-time.")

if mode == "Pre-defined":
    route = input("Type a route path: w = forward; a = left; d = right; (try 'aawwwddwdwwwaawdwwwdddwwawwwwawaddww')")

    for i in route:
        if i == "w":
            forward(190)
        elif i == "a":
            leftturn()
        elif i == "d":
            rightturn()
elif mode == "Real-time":
    option = int(input())
    if option == 'w':
        forward(190)
    elif option == 'a':
        leftturn()
    elif option == 'd':
        rightturn()

mainloop()
