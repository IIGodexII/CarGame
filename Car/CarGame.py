import turtle, time, random
##from playsound import playsound

pencere = turtle.Screen()
pencere.title('Araba Yarışı')
pencere.bgcolor('gray')
pencere.setup(height=700, width=500)
pencere.tracer(0)

pencere.register_shape('racingback.gif')
pencere.register_shape('racingcar.gif')

araba = turtle.Turtle()
araba.speed(0)
araba.shape('racingcar.gif')
araba.shapesize(2)
araba.color('red')
araba.setheading(90)
araba.penup()
araba.goto(0, -200)

arka = turtle.Turtle()
arka.speed(0)
arka.pensize(3)
arka.shape('square')
arka.color('white')
arka.penup()
arka.hideturtle()
arka.goto(0, 0)

kamera_dy = 0
kamera_y = 0

def sol():
    x = araba.xcor()
    x = x - 10
    if x < -170:
        x = -170
    araba.setx(x)
def sag():
    x = araba.xcor()
    x = x + 10
    if x > 170:
        x = 170
    araba.setx(x)
engeller = []
for i in range(10):
    engel = turtle.Turtle()
    engel.speed(0)
    engel.shape('square')
    engel.shapesize(3, 6)
    engel.color('red')
    engel.setheading(90)
    engel.penup()
    engel.dx = random.randint(-170, 170)
    engel.dy = 500
    engel.goto(engel.dx, engel.dy)
    engeller.append(engel)

pencere.listen()
pencere.onkeypress(sol, "Left")
pencere.onkeypress(sag, "Right")
baslangic_zaman = time.time()
i = -1
while True:
    kamera_dy = -2
    kamera_y = kamera_y + kamera_dy
    kamera_y = kamera_y % 700

    arka.goto(0, kamera_y - 700)
    arka.shape('racingback.gif')
    arka.stamp()
    araba.shape('racingcar.gif')
    araba.stamp()

    arka.goto(0, kamera_y)
    arka.shape('racingback.gif')
    arka.stamp()
    araba.shape('racingcar.gif')
    araba.stamp()

    if time.time()-baslangic_zaman > random.randint(3, 6):
        baslangic_zaman = time.time()
        i = i + 1
        if i == 9:
            i = -1
            for engel in engeller:
                engel.dx = random.randint(-170, 170)
                engel.dy = 500
                engel.goto(engel.dx, engel.dy)
    y = engeller[i].ycor()
    y = y - 2
    engeller[i].sety(y)

    if engeller[i].distance(araba) < 30:
        print('Çarptı')

    pencere.update()

    arka.clear()
    araba.clear()