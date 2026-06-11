import pgzrun


"""
import random
WIDTH = 800
HEIGHT = 600

balls = []
suuji=[1,2,3,4,5]
i=0

def init():
    for _ in range(5):
        ball = Actor('a2')
        ball.pos = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
        balls.append(ball)

def draw():
    screen.clear()
    for ball in balls:
        ball.draw()
def update():
    move_balls()
    for _ in range(5):
        ball = Actor('a2')
        ball.pos = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
        balls.append(ball)
def move_balls():
    for ball in balls:
        ball.x += 2
        if ball.x > WIDTH:
            ball.x = 0

#init()
"""
# 空の辞書の作成
my_dict = {}
a=1
# キーと値の追加
my_dict['name'] = 'John'
my_dict['age'] = 25
my_dict['city'] = 'New York'

# 辞書の表示
print(my_dict)

# キーを指定して値を取得
print("Name:", my_dict['name'])
print("Age:", my_dict['age'])

# キーの存在確認
if 'city' in my_dict:
    print("City:", my_dict['city'])

# キーと値の一覧表示
a=0
def draw():
    screen.clear()
    global a
    screen.draw.text(str(a%10),(200,0),fontsize=1000)
def draw():
    screen.clear()
    global a
    screen.draw.text(str(a%10),(200,0),fontsize=1000)
    
a=2
def on_mouse_down(pos,button):
    global a,b,c
    a+=1
pgzrun.go()
