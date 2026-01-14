from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.score_saving()
        self.penup()
        self.goto(0, 250)
        self.color("white")
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}, Highest Score {self.high_score}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.penup()
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def score_update(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
        self.score_updating_txt()

    def score_updating_txt(self):
        with open("snake_game/score_safe.txt", mode="w") as score_update:
            score_update.write(f"{self.high_score}")
        
    def score_saving(self):
        with open("snake_game/score_safe.txt") as score_file:
            score_safe = score_file.read()
            return int(score_safe)
            
            
        
