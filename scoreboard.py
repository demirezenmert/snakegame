from turtle import Turtle
FONT_STYLE = ('Courier', 20, 'italic')
FONT_STYLE_GAME_OVER = ('Courier', 30, 'italic')
COLOR = 'white'
class ScoreBoard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.score= 0
        self.penup()
        self.hideturtle()
        self.color(COLOR)
        self.goto(0,280)
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f'Score: {self.score}', font= FONT_STYLE, align='center')
        self.score += 1
    def game_over(self):
        self.goto(0,0)
        self.write(f'GAME OVER', font= FONT_STYLE_GAME_OVER, align='center')