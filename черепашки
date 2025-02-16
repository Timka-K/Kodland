import turtle
import random

t = turtle.Turtle()
t.up()
t.goto(-100,100)
t.down()
t.speed(0)

# поле
for i in range(15):
    t.write(i)
    t.rt(90)
    t.fd(200)
    t.lt(180)
    t.fd(200)
    t.rt(90)
    t.fd(20)
    #первая черепашка
first = turtle.Turtle()
first.shape("turtle")
first.color("red")
first.up()
first.goto(-120,70)
first.down()
#вторая черепашка
second = turtle.Turtle()
second.shape("turtle")
second.color("blue")
second.up()
second.goto(-120,40)
second.down()
#третья черепашка
third = turtle.Turtle()
third.shape("turtle")
third.color("yellow")
third.up()
third.goto(-120,10)
third.down()
#твоя черепашка
colort = input("выбери цвет для своей черепашки(на английском)")
yourt = turtle.Turtle()
yourt.shape("turtle")
yourt.color(colort)
yourt.up()
yourt.goto(-120,-20)
yourt.down()
#болельщики
x = random.randint(1,10)
for i in range(x):
    bol = turtle.Turtle()
    bol.shape("turtle")
    color1 = random.randint(0,255)
    color2 = random.randint(0,255)
    color3 = random.randint(0,255)
    bol.color( color1,  color2,  color3)
    bol.up()
    bol.goto(-90 + 25 * i,-120)
    bol.down()
    bol.lt(90)
win = input("Какая черепаха победит:")
text = turtle.Turtle()
text.up()
text.goto(-120,120)
text.write("Ты считаешь, что победит " + win)
x_first = 0
x_second = 0
x_third = 0
x_yourt = 0
while True:
    if x_first >=305 or x_second >=305 or x_third >=305 or x_yourt >=305:
        break
    first_step=random.randint(1,5)
    x_first = x_first + first_step
    first.fd(first_step)
    
    second_step=random.randint(1,5)
    x_second = x_second + second_step
    second.fd(second_step)
    
    third_step=random.randint(1,5)
    x_third = x_third + third_step
    third.fd(third_step)
    
    yourt_step = random.randint(1,5)
    x_yourt = x_yourt + yourt_step
    yourt.fd(yourt_step)
#победитель
if x_first > 305:
    t=turtle.Turtle()
    t.up()
    t.goto(-120,150)
    t.write("победила красная черепашка")
elif x_second >305:
    t=turtle.Turtle
    t.up()
    t.goto(-120,150)
    t.write("победила синяя черепашка")
elif x_third >305:
    t=turtle.Turtle()
    t.up()
    t.goto(-120,150)
    t.write("победила жёлтая черепашка")
elif x_third >305:
    t=turtle.Turtle()
    t.up()
    t.goto(-120,150)
    t.write("победила жёлтая черепашка")
elif x_yourt >305:
    t=turtle.Turtle()
    t.up()
    t.goto(-120,150)
    t.write("поздравляю,вы победили")
