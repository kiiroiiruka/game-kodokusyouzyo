import pgzrun
l=[0,0,0,0,0,0,0,0]
i=0
l[0]=1
def draw():
    screen.draw.text(str(l[0]),(0,0),fontsize=30)
pgzrun.go()
