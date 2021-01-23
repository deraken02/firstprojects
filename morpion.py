from turtle import*
from random import randint
penup()
goto(-150,0)
pendown()
forward(300)
penup()
goto(-150,100)
pendown()
forward(300)
penup()
goto(-50,-100)
left(90)
pendown()
forward(300)
penup()
goto(50,-100)
pendown()
forward(300)
right(90)
a=str(input('joueur1 '))
b=str(input('joueur2 '))
c=randint(1,2)
if c==1:
    print(a,'commence')
if c==2:
    print(b,'commence')
cpt1=0
def croix():
    width(5)
    left(45)
    pendown()
    forward(95)
    penup()
    left(135)
    forward(70)
    left(135)
    pendown()
    forward(95)
    left(45)
d=1
q='True'
r='True'
s='True'
t='True'
u='True'
v='True'
w='True'
x='True'
y='True'
a1=10
a2=11
a3=2
a4=3
a5=4
a6=5
a7=6
a8=7
a9=8
while cpt1<9 and d!=0:
    width(5)
    cpt1+=1
    d=int(input('choisi ta case '))
    if d==7:
        if q=='True':
            if cpt1%2==0:
                penup()
                goto(-140,110)
                croix()
                a7=0
            else:
                penup()
                goto(-100,105)
                pendown()
                circle(45)
                a7=1
        if q=='False':
            cpt1=cpt1-1
            print('erreur case déjà prise réessaye')
        q='False'
    if d==8:
        if r=='True':
            if cpt1%2==0:
                penup()
                goto(-30,110)
                croix()
                a8=0
            else:
                penup()
                goto(0,105)
                pendown()
                circle(45)
                a8=1
        else:
            cpt1=cpt1-1
            print('erreur cette case est déjà prise réessayer')
        r='False'
    if d==9:
        if s=='True':
            if cpt1%2==0:
                penup()
                goto(60,110)
                croix()
                a9=0
            else:
                penup()
                goto(100,105)
                pendown()
                circle(45)
                a9=1
        else:
            cpt1=cpt1-1
            print('erreur case déjà prise réessaye')
        s='False'
    if d==4:
        if t=='True':
            if cpt1%2==0:
                penup()
                goto(-140,10)
                croix()
                a4=0
            else:
                penup()
                goto(-100,5)
                pendown()
                circle(45)
                a4=1
        else:
            cpt1=cpt1-1
            print('erreur case déjà prise réessaye')
        t='False'
    if d==5:
        if u=='True':
            if cpt1%2==0:
                penup()
                goto(-30,10)
                croix()
                a5=0
            else:
                penup()
                goto(0,5)
                pendown()
                circle(45)
                a5=1
        else:
            cpt1=cpt1-1
            print('erreur case déjà prise réessaye')
        u='False'
    if d==6:
        if v=='True':
            if cpt1%2==0:
                penup()
                goto(60,10)
                croix()
                a6=0
            else:
                penup()
                goto(100,5)
                pendown()
                circle(45)
                a6=1
        else:
            cpt1=cpt1-1
            print('erreur case déjà prise réessaye')
        v='False'
    if d==1:
        if w=='True':
            if cpt1%2==0:
                penup()
                goto(-140,-90)
                croix()
                a1=0
            else:
                penup()
                goto(-100,-95)
                pendown()
                circle(45)
                a1=1
        else:
            cpt1=cpt1-1
            print('erreur case déjà prise réessaye')
        w='False'
    if d==2:
        if x=='True':
            if cpt1%2==0:
                penup()
                goto(-30,-90)
                croix()
                a2=0
            else:
                penup()
                goto(0,-95)
                pendown()
                circle(45)
                a2=1
        else:
            cpt1=cpt1-1
            print('erreur case déjà prise réessaye')
        x='False' 
    if d==3:
        if y=='True':
            if cpt1%2==0:
                penup()
                goto(60,-90)
                croix()
                a3=0
            else:
                penup()
                goto(100,-95)
                pendown()
                circle(45)
                a3=1
        else:
            cpt1=cpt1-1
            print('erreur case déjà prise réessaye')
        y='False'
    if (a1==a2==a3):
        penup()
        goto(-150,-60)
        pendown()
        forward(300)
        penup()
        goto(0,-200)
        pendown()
        if (c==1 and cpt1%2==0) or (c==2 and cpt1%2!=0):
            write(b+' gagne')
            print(b,'gagne')
            cpt1=9
        else:
            write(a+' gagne')
            print(a,'gagne')
            cpt1=9
    if(a1==a4==a7):
        penup()
        goto(-100,-100)
        left(90)
        pendown()
        forward(300)
        penup()
        right(90)
        goto(0,-200)
        pendown()
        if (c==1 and cpt1%2==0) or (c==2 and cpt1%2!=0):
            write(b+' gagne')
            print(b,'gagne')
            cpt1=9
        else:
            write(a+' gagne')
            print(a,'gagne')
            cpt1=9
    if(a2==a5==a8):
        penup()
        goto(0,-100)
        left(90)
        pendown()
        forward(300)
        penup()
        right(90)
        goto(0,-200)
        pendown()
        if (c==1 and cpt1%2==0) or (c==2 and cpt1%2!=0):
            write(b+' gagne')
            print(b,'gagne')
            cpt1=9
        else:
            write(a+' gagne')
            print(a,'gagne')
            cpt1=9
    if(a3==a6==a9):
        penup()
        goto(100,-100)
        left(90)
        pendown()
        forward(300)
        penup()
        right(90)
        goto(0,-200)
        pendown()
        if (c==1 and cpt1%2==0) or (c==2 and cpt1%2!=0):
            write(b+' gagne')
            print(b,'gagne')
            cpt1=9
        else:
            write(a+' gagne')
            print(a,'gagne')
            cpt1=9
    if(a4==a5==a6):
        penup()
        goto(-150,50)
        pendown()
        forward(300)
        penup()
        goto(0,-200)
        pendown()
        if (c==1 and cpt1%2==0) or (c==2 and cpt1%2!=0):
            write(b+' gagne')
            print(b,'gagne')
            cpt1=9
        else:
            write(a+' gagne')
            print(a,'gagne')
            cpt1=9
    if(a7==a8==a9):
        penup()
        goto(-150,150)
        pendown()
        forward(300)
        penup()
        goto(0,-200)
        pendown()
        if (c==1 and cpt1%2==0) or (c==2 and cpt1%2!=0):
            write(b+' gagne')
            print(b,'gagne')
            cpt1=9
        else:
            write(a+' gagne')
            print(a,'gagne')
            cpt1=9
    if(a1==a5==a9):
        penup()
        goto(-150,-100)
        left(45)
        pendown()
        forward(420)
        penup()
        right(45)
        goto(0,-200)
        pendown()
        if (c==1 and cpt1%2==0) or (c==2 and cpt1%2!=0):
            write(b+' gagne')
            print(b,'gagne')
            cpt1=9
        else:
            write(a+' gagne')
            print(a,'gagne')
            cpt1=9
    if(a7==a5==a3):
        penup()
        goto(-150,200)
        left(-45)
        pendown()
        forward(420)
        penup()
        right(-45)
        goto(0,-200)
        pendown()
        if (c==1 and cpt1%2==0) or (c==2 and cpt1%2!=0):
            write(b+' gagne')
            print(b,'gagne')
            cpt1=9
        else:
            write(a+' gagne')
            print(a,'gagne')
            cpt1=9