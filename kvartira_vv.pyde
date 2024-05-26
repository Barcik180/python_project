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
            fill(u,n,u)
            rect(u,n,1,1)
    push()
    fill(255,0,239)
    rect(600,700,50,50)
    fill(33,0,255)
    ellipse(625,725,30,30)
    pop()
    rect(600,800,130,80)
    push()
    fill(0)
    text("ррвркери",600,810)
    text("апапваса",600,820)
    text("рпьыргнк",600,830)
    text("ииитттии",600,840)
    text(u"Семён.П.",600,850)
    pop()
    rect(200,300,100,75)
    push()
    fill(0)
    text(u"я 1год назат",202,310)
    text(u"был в китае. Там",200,323)
    text(u"Там было здоро-",200,336)
    text(u"го. Миша нашел ",200,349)
    text(u"_______  ",200,362)
    pop()
    ellipse(340,155,15,40)
    ellipse(360,155,15,40)
    ellipse(350,175,40,40)
    push()
    strokeWeight(5)
    point(345,175)
    point(355,175)
    pop()
    ellipse(350,220,25,50)
    ellipse(380,220,25,50)
    ellipse(410,220,25,50)
    ellipse(440,220,25,50)
    ellipse(445,180,25,60)
    ellipse(400,200,100,50)
    
    rect(500,150,100,75)
    rect(350,500,120,75)
    rect(700,700,130,75)
    rect(700,250,100,75)
    fill(0)
    text(u"дорогой дневник.",700,710)
    text(u"Я сегодня",700,720)
    text(u"писал работу",700,730)
    text(u"по русскому",700,740)
    text(u"языку.",700,750)
    text(u"его кто-то разорвал.",700,760)
    text(u"Пряники имбирные",350,510)
    text(u"Вкусные,любимые.",350,520)
    text(u"Котики пушистые",350,530)
    text(u"И любимые.",350,540)
    text(u"      2",500,160)
    text(u"2пR",500,170)
    text(u"это S круга:)",500,180)
    text(u"a*b*c=V куба:)",500,190)
    text(u"/>___/>",710,260)
    text(u"lO......Ol",710,270)
    text(u"l....VV...l",710,280)
    text(u"l...........l",710,290)
    text(u"l...........l",710,300)
    text(u"l...........l",710,310)
    fill(0,78,255)
    rect(400,300,100,100)
    fill(242,0,255)
    ellipse(450,350,50,50)
    line(750,25,700,0)
    line(750,25,800,0)
    fill(20)
    rect(700,25,100,50)
    fill(0)
    ellipse(720,50,20,20)
    ellipse(780,50,20,20)
    fill(154,55,64)
    ellipse(170,200,100,100)
    fill(0,255,0)
    ellipse(170,200,40,40)
    fill(193,97,0)
    rect(900,950,100,50)
    fill(255,0,0)
    ellipse(950,975,30,30)
    fill(0,255,0)
    ellipse(960,955,40,20)
    fill(147,67,0)
    rect(950,0,50,100)
    fill(247,240,0)
    ellipse(980,60,20,20)
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
    print(u"< deti: privet papa!!!!! ты не.  >-_--___-_-_/Lm/           n      n    ___:")
    print("<________________________________>-_--_-_---_/Lm/            nnnnnn    ___:")
    print("                                             /Lm/")
