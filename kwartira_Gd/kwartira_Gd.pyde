x=0
y=0
u=0
n=0
k=1
b=500
j=4
h=0
r=1
h=1
def setup():
    size(1000,1000)
def draw():
    global x,y,k,b,j,h,r
    strokeWeight(1)
    background(157,113,0)
    fill(255,0,0)
    rect(50,50,900,900)
    for i in range(150):
        n=i*6+51
        for i in range(300):
            u=i*3+51
            rect(u,n,1,1)
    fill(147,67,0)
    rect(950,0,50,100)
    
    push()
    fill(255)
    rect(150,600,400,400)
    fill(0,93,250)
    ellipse(200,650,90,90)
    fill(255,0,0)
    ellipse(300,650,90,90)
    fill(0,255,0)
    ellipse(400,650,90,90)
    fill(250,255,0)
    ellipse(500,650,90,90)
    translate(0,100)
    fill(0,93,250)
    ellipse(200,650,90,90)
    fill(255,0,0)
    ellipse(300,650,90,90)
    fill(0,255,0)
    ellipse(400,650,90,90)
    fill(250,255,0)
    ellipse(500,650,90,90)
    translate(0,100)
    fill(0,93,250)
    ellipse(200,650,90,90)
    fill(255,0,0)
    ellipse(300,650,90,90)
    fill(0,255,0)
    ellipse(400,650,90,90)
    fill(250,255,0)
    ellipse(500,650,90,90)
    translate(0,100)
    fill(0,93,250)
    ellipse(200,650,90,90)
    fill(255,0,0)
    ellipse(300,650,90,90)
    fill(0,255,0)
    ellipse(400,650,90,90)
    fill(250,255,0)
    ellipse(500,650,90,90)
    pop()
    fill(20)
    rect(160,0,200,100)
    fill(20)
    rect(360,0,200,100)
    fill(255)
    rect(400,25,100,50)
    fill(0)
    text(u"kурица:)",420,55)
    fill(0)
    ellipse(210,50,100,100)
    fill(0)
    ellipse(310,50,100,100)
    #
    fill(50)
    ellipse(210,50,25,25)
    fill(50)
    ellipse(310,50,25,25)
    #
    fill(100,0,55)
    rect(500,500,100,100)
    fill(20,76,65)
    ellipse(550,550,50,50)
    fill(0,255,0)
    ellipse(x,y,100,100)
    
    ellipse(b,500,50,50)
    h=h+r
    
    strokeWeight(1)
    stroke(0)
    ellipse(h,400,50,50)
    b=b+j
    if b==1000:
        j=-4
    if b==0:
        j=4
    if h==1000:
        r=-2
    if h==0:
        r=2
    if key=="d":
        x=x+1
    if key=="a":
        x=x-1
    if key=="w":
        y=y-1
    if key=="s":
        y=y+1
    
    
    fill(0,255,0)
    ellipse(100,900,100,100)
    print("                                             /Lm/")
    print("<________________________________>-_---------/Lm/            nnnnnn   ___:")
    print("< ya prijol.                     >-_---------/Lm/           n      n    ___:")
    print("< ya:pochemy mbl kypili twester? >-_--------_/Lm/          n  :  :  n    ___:")
    print("< jena: ya ne znau.              >-_--------_/Lm/          n   ___  n    ___:")
    print("< deti: privet papa!!!!!         >-_--___-_-_/Lm/           n      n    ___:")
    print("<________________________________>-_--_-_---_/Lm/            nnnnnn    ___:")
    print("                                             /Lm/")
