from turtle import Turtle
from random import randint
class Food(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color('red')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        random_x = randint(-285,285)
        random_y = randint(-285,285)
        self.goto(random_x,random_y)