class Fruit:
    color = "green"

    def harvest(self, color):
        print("i am: ", color)
        print("nothing --------")
        print("orignial color is: ", Fruit.color)


class Apple(Fruit):
    color = "red"

    def __init__(self):
        print("i am apple")


class Orange(Fruit):
    color = "orange"

    def __init__(self):
        print("i am Orange")


apple = Apple()
apple.harvest(Apple.color)

orange = Orange()
orange.harvest(orange.color)