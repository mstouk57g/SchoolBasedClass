import  turtle

def  ZNBX(sl , n , lc , fc , x , y ):

    turtle.color(lc, fc)
    
    turtle.speed(0)

    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

    turtle.begin_fill()

    for  i  in range(n):

        turtle.forward(sl)
        turtle.left(360/n)

    turtle.end_fill()



def windcar(x, y, ds, h, r, c1, c2, c3, c4):
    turtle.ht()
    turtle.color(c1,c2)
    turtle.begin_fill()
    turtle.pu()
    turtle.goto(x,y-h)
    turtle.pd()
    turtle.forward(ds/2)
    turtle.goto(x,y)
    turtle.pu()
    turtle.goto(x,y-h)
    turtle.pd()
    turtle.right(180)    
    turtle.forward(ds/2)    
    turtle.goto(x,y)    
    turtle.end_fill()
    turtle.color(c3,c4)
    for i in range(4) :
        turtle.begin_fill()
        turtle.circle(r)  
        turtle.end_fill()
        turtle.right(90)  
        
