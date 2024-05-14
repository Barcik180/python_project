y=1
z=1
e=1
x=1
v=random(500)
h=random(1000)
k=random(1000)
j=random(2000)
def setup():
    size(1000,1000, P3D)
    frameRate(30)
def draw():
    global x,y,z,e,v,h,k,j,v
    background(255)
    #random sphere
    push()
    fill(0)
    stroke(255,255,255)
    translate(x,y,z)
    stroke(255)
    translate(random(1000),random(1000),random(1000))
    sphere(10)
    translate(random(1000),random(1000),random(1000))
    stroke(0)
    sphere(10)
    translate(random(1000),random(1000),random(1000))
    sphere(10)
    pop()
    #
    push()
    fill(0)
    stroke(255,255,255)
    translate(x,y,z)
    translate(h,k,j)
    sphere(v)
    pop()  
    push()
    fill(0)
    stroke(255,255,255)
    translate(x,y,z)
    translate(700,200,50)
    sphere(100)
    pop()
    push()
    fill(0)
    stroke(255,255,255)
    translate(x,y,z)
    translate(900,90,100)
    sphere(200)
    pop()
    translate(x,y,z)
    fill(0)
    stroke(255,255,255)
    sphere(600)
    stroke(0,0,0)
    sphere(598)
    strokeWeight(1)
    fill(255,247,3)
    sphere(100)
    fill(255,0,0)
    sphere(50)
    fill(255,144,8)
    sphere(75)
    fill(0,255,255)
    sphere(200)
    fill(30)
    sphere(150)
    fill(0,255,0)
    sphere(180)
    if key=="w":
        y=y-5
    if key=="s":
        y=y+5
    if key=="d":
        x=x+5
    if key=="a":
        x=x-5
    if key=="e":
        z=z-5
    if key=="q":
        z=z+5
    e=e+0.5
    fill(30)
    rotate(e)
    translate(400,0,0)
    rotateY(radians(frameCount))
    sphere(80)
    rotate(e)
    sphere(50)
    fill(255,0,0)
    sphere(25)
    fill(201,0,0)
    sphere(25)
    if e==360:
        e=0
    print(random(1))
    print("011001")
    print(random(1))
    print("111000110")
    print(random(1)) 
    print("11100100")
    print(random(1)) 
    print("121")
    print(" ")
    print(" g       g")
    print("cat     cat                         /")
    print("g   ggg    g             /         <:>")
    print("g  o    o  g            <:>       <<:>>")
    print("g    uu    g  gggg     <<:>>     <<<:>>>")
    print("gggggggggggggg___________:___________:")
    print("I<cat>I")
    print("error")
    print(" ")
    print(random(1))
    print(random(1))
    print("011001")
    print(random(1))
    print(random(1))
    print("011001")
    print("11100100")
    print(mouseX)
    print(mouseY)
    print(" ")
    print(" ")
