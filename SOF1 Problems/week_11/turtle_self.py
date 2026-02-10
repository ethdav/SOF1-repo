import turtle
import math

def koch_snowflake(turt, screen, length, degree):
    if degree == 0:
        turt.fd(length)
    else:
        if length >= 3:
            length = length/3
            degree -= 1
            koch_snowflake(turt, screen, length, degree)
            turt.tilt(math.pi/3)
            koch_snowflake(turt, screen, length, degree)
            turt.tilt(4*math.pi/3)
            koch_snowflake(turt, screen, length, degree)
            turt.tilt(math.pi/3)
            koch_snowflake(turt, screen, length, degree)

def main():
    screen = turtle.getscreen()
    turt = turtle.Turtle()
    koch_snowflake(turt, screen, 1000, 90)

if __name__ == "__main__":
    main()