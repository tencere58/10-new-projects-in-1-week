import turtle
import random
from PIL import Image

img1 = Image.open("nemo_sad.png")
img1.save("nemo_sad.gif")
img2 = Image.open("nemo.png")
img_resized = img2.resize((100, 80)).save("nemo.gif")

board = turtle.Screen()
board.title("NEMOYU YAKALA")
tur = turtle.Turtle()
tur.penup()

try_again = turtle.Turtle()
try_again.hideturtle()
try_again.penup()
try_again.goto(0,-150)

board.register_shape("nemo_sad.gif")  # GIF kullan
board.register_shape("nemo.gif")
tur.shape("nemo.gif")
try_again.shape("nemo_sad.gif")


say_tur = turtle.Turtle()
say_tur.hideturtle()
say_tur.penup()
say_tur.goto(-250,260)

score_tur = turtle.Turtle()
score_tur.hideturtle()
score_tur.penup()
score_tur.goto(250,260)

game_over = turtle.Turtle()
game_over.hideturtle()
game_over.penup()
game_over.goto(0,260)


ttt = 1
saniye = 10


def tık(x, y):
    global ttt
    m = random.randint(-325, 325)
    n = random.randint(-195, 195)

    tur.hideturtle()
    tur.goto(m, n)
    tur.showturtle()

    score_tur.clear()
    score_tur.write(f"SCORE: {ttt} ", align="center", font=("Arial", 24, "normal"))
    ttt += 1


def time():
    global saniye
    say_tur.clear()
    say_tur.write(f"TIME: {saniye}", align="center", font=("Arial", 24, "normal"))
    saniye -= 1
    if saniye >= 0:
        board.ontimer(time, 1000)

    else:
        game_over.write("GAME OVER", align="center", font=("Arial", 30, "normal"))
        tur.onclick(None)
        tur.hideturtle()
        try_again.showturtle()


def restart(x, y):
    global ttt, saniye
    ttt = 1
    saniye = 10
    say_tur.clear()
    score_tur.clear()
    game_over.clear()
    try_again.hideturtle()
    tur.showturtle()
    time()
    tur.onclick(tık)
    try_again.onclick(restart())

time()

tur.onclick(tık)
try_again.onclick(restart)


turtle.done()