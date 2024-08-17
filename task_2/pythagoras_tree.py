import turtle
import math

def draw_pythagoras_tree(t, branch_length, angle, level):
    if level == 0:
        return
    
    t.forward(branch_length)
    
    pos = t.pos()
    heading = t.heading()
    
    t.left(angle)
    draw_pythagoras_tree(t, branch_length * math.sqrt(2) / 2, angle, level - 1)
    t.setpos(pos)
    t.setheading(heading)

    t.right(angle)
    draw_pythagoras_tree(t, branch_length * math.sqrt(2) / 2, angle, level - 1)
    t.setpos(pos)
    t.setheading(heading)


def main():
    recursion_level = int(input("Введіть рівень рекурсії: "))
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed("fastest")
    t.left(90)
    draw_pythagoras_tree(t, 100, 45, recursion_level)
    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()