import turtle


def draw_pifagoras_tree(t, branch_length, level):
    if level == 0:
        return
    t.forward(branch_length * level)
    t.right(45)
    draw_pifagoras_tree(t, branch_length, level - 1)
    t.left(90)
    draw_pifagoras_tree(t, branch_length, level - 1)
    t.right(45)
    t.backward(branch_length * level)


def main():
    level = int(input("Введіть рівень рекурсії для фрактала дерева Піфагора: "))

    window = turtle.Screen()
    window.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)

    t.left(90)
    t.up()
    t.backward(100)
    t.down()

    draw_pifagoras_tree(t, 10, level)

    window.exitonclick()


if __name__ == "__main__":
    main()
