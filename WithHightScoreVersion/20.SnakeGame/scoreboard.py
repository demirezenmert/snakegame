from turtle import Turtle
FONT_STYLE = ('Courier', 20, 'italic')
FONT_STYLE_GAME_OVER = ('Courier', 30, 'italic')
COLOR = 'white'
class ScoreBoard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.score= 0
        with open("data.txt",'r') as data:
            self.high_score= int(data.read())
        self.penup()
        self.hideturtle()
        self.color(COLOR)
        self.goto(0,280)
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f'Score: {self.score} | High Score: {self.high_score}', font= FONT_STYLE, align='center')
    def increase_score(self):
        self.score += 1
        self.refresh()
    
    def game_over(self):
        if self.score > self.high_score:


            self.high_score= self.score
            self.write_data(self.high_score)
        self.score = 0
        self.refresh()

    def write_data(self,data):
        with open('data.txt', 'w') as file:
            file.write(str(data))
        