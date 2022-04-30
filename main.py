import turtle 
import time

t = turtle.Turtle()


# ==========================  Star One =================================
time.sleep(1)

t.penup()
t.setpos(-185,255)
t.pendown()

t.color('white', 'yellow')
t.begin_fill()
for i in range(5):
    t.forward(150)
    t.right(144)
t.end_fill()

# # ==========================  Star Two =================================
t.penup()
t.setpos(-20,255)
t.pendown()

t.color('white', 'yellow')
t.begin_fill()
for i in range(5):
    t.forward(150)
    t.right(144)
t.end_fill()
# ==========================  Star Logo =================================

t.penup()
t.setpos(-30,-310)
t.pendown()

t.color('black', 'blue')
t.begin_fill()
t.circle(240)
t.end_fill()

t.up()
t.setpos(-30,-290)
t.down()

t.color('black', 'white')
t.begin_fill()
t.circle(220)
t.end_fill()

# ============================================================

t.up()
t.setpos(-230,-100)
t.down()
# time.sleep(10)
t.color('black', 'blue')
t.begin_fill()
t.left(90)
t.circle(-200, extent=180)


t.circle(-80, extent=45)


t.circle(-80, extent=210)
# time.sleep(6)

t.left(105)
t.circle(160, extent=150)
t.end_fill()
# ============================================================

t.left(90)

t.penup()
t.forward(100)
t.right(90)
t.forward(60)
t.left(90)
t.pendown()

t.color('black', 'blue')
t.begin_fill()
t.circle(70)
t.end_fill()

t.up()
t.setpos(-129.27,-152.73)
t.down()

t.color('black', 'white')
t.begin_fill()
t.circle(60)
t.end_fill()

t.up()
t.setpos(-29.27,-162.73)
t.down()


t.color('black', 'blue')
t.begin_fill()
t.circle(70)
t.end_fill()

t.up()
t.setpos(-29.27,-152.73)
t.down()

t.color('black', 'white')
t.begin_fill()
t.circle(60)
t.end_fill()

print(t.position())

t.up()
t.setpos(85.27,-162.73)
t.down()

t.color('white', 'skyblue')
t.begin_fill()
t.circle(65)
t.end_fill()

t.right(90)
t.penup()
t.forward(70)
t.right(90)
t.forward(175)
t.pendown()

# ADD TEXT
t.color('black')
t.write("1945 - 1324", font=("Verdana",15, "normal"))




turtle.done()