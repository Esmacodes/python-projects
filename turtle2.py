import turtle


#---PENCERE OLUŞTURMA-------------------------
screen=turtle.Screen()
screen.title("DRAW")
screen.bgcolor("white")
screen.screensize(600,600)


#---KARAKTER OLUŞTURMA-------------------

character=turtle.Turtle()
character.shape("turtle")

#------YÖN HAREKETLERİ--------------------------------------------
def foward_func():
    character.forward(20)
def back_func():
    character.back(20)
def right_func():
    character.right(10)
def left_func():
    character.left(10)

#--KALEMİ AKTİF/PASİF DURUMA GETİRME--------------------------------------
pen_ctrl=True
def pen_off():
    global pen_ctrl
    character.penup()
    pen_ctrl=False

def pen_on():
    global pen_ctrl
    character.pendown()
    pen_ctrl = True

def toggle_pen():
    if pen_ctrl==True:
        pen_off()
    else:
        pen_on()



#---RENK DEĞİŞTİRME------------------------------------------
colors=["black","yellow","purple","green","pink","grey"]
color_index=0
def color_plus():
    global color_index
    color_index+=1
    if color_index==6:
        color_index=0
    character.color(colors[color_index])

def color_minus():
    global color_index
    color_index -= 1
    if color_index == -1:
        color_index = 5
    character.color(colors[color_index])


#-KALEM BÜYÜKLÜĞÜNÜ/KARAKTER BOYUTUNU DEĞİŞTİRME----------------------
pen_size=2
def size_plus():
    global pen_size
    global character_size
    pen_size +=1
    character_size +=0.05
    character.pensize(pen_size)
    character.shapesize(character_size)

def size_minus():
    global pen_size
    global character_size

    if pen_size>1:
        character_size-=0.05
        pen_size -=-1
    character.pensize(pen_size)
    character.shapesize(character_size)


#-------------------------------------------------
class color_choice(object):
    def __init__(self,color,size,shape,x_cor,y_cor):
        x=turtle.Turtle()
        x.shape(shape)
        x.color(color)
        x.shapesize(size)
        x.penup()
        x.goto(x_cor,y_cor)


#["black","yellow","purple","green","pink","grey"](renklerimiz)
b=color_choice("black",1,"circle",-370,370)
y=color_choice("yellow",1,"circle",-340,370)
p1=color_choice("purple",1,"circle",-310,370)
q1=color_choice("green",1,"circle",-280,370)
p2=color_choice("pink",1,"circle",-250,370)
q2=color_choice("grey",1,"circle",-220,370)


#-------------------------------------------------
screen.onkey(foward_func, "w")
screen.onkey(back_func,"s")
screen.onkey(right_func,"d")
screen.onkey(left_func,"a")
screen.onkey(toggle_pen,"space")
screen.onkey(color_plus,"v")
screen.onkey(color_minus,"c")
screen.onkey(size_plus,"Right")
screen.onkey(size_minus,"Left")

screen.listen()
#-----------------------------------------------------



while True:
    screen.update()