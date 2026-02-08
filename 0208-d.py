import turtle
import random
import time

score=0 # 점수 초기화
screen=turtle.Screen() # turtle 그래픽의 무대 설정 만들기
screen.tracer(0) # 업데이트를 수동으로 해준다
                 # 화면이 깜빡함을 제거해 준다.
screen.addshape("dog.gif") # 강아지 이미지를 불러온다.   
screen.addshape("car.gif")

# 강아지 설정
player=turtle.Turtle() # 거북이 개체 만들기
player.shape("dog.gif") # 거북이 모양을 이미지로 바꿈

player.up() # 경기장을 사각형으로 그린다.
player.goto(-250,250)

# 경기장 그리기
player.down()
player.goto(250,250)
player.goto(250,-250)
player.goto(-250,-250)
player.goto(-250,250)
player.up()
player.goto(0,0)

# 점수 설정
bread=turtle.Turtle()
bread.shape("car.gif")
bread.penup()
x=random.randint(-200,200)
y=random.randint(-200,200)
bread.goto(x,y)

# 점수 설정
score=0
score_turtle=turtle.Turtle()
score_turtle.penup()
score_turtle.goto(0,260)
score_turtle.write("점수: {}".format(score),align="center",font=("Arial",16,"normal"))

# 시간 설정
time_limit=100000
time_turtle=turtle.Turtle()
time_turtle.penup()
time_turtle.goto(0,-280)
time_turtle.write("남은 시간:{}".format(time_limit),align="center",font=("Arial",16,"normal"))

# 키보드 방향 설정
def moveRight():
    player.setheading(0) # 각도 거붕이의 머리 방향-오른쪽
    player.forward(10)
def moveLeft():
    player.setheading(180) # 왼쪽
    player.forward(10)
def moveUp():
    player.setheading(90) # 위쪽
    player.forward(10)
def moveDown():
    player.setheading(270) # 아래쪽
    player.forward(10)            

# 키보드 입력 준비 상태
screen.listen() # 키보드 입력 받을 준비 상태
screen.onkeypress(moveRight,"Right")
screen.onkeypress(moveLeft,"Left")
screen.onkeypress(moveUp,"Up")
screen.onkeypress(moveDown,"Down")

# 게임 루프
while time_limit > 0:
    # 과자이동(자동차)
    if time_limit % 1000 == 0:
        bread.goto(random.randint(-200,200),random.randint(-200,200))
    # 강아지가 과자(자동차)를 먹으면 점수 증가 
    if player.distance(bread) < 30:
        score+=1 # score=score+1
        bread.goto(random.randint(-200,200),random.randint(-200,200))
        score_turtle.clear()
        score_turtle.write("점수: {}".format(score),align="center",font=("Arial",16,"normal"))

    # 시간 감소
    time_limit-=1 # time_limit=time_limit-1
    time_turtle.clear()
    time_turtle.write("남은 시간:{}".format(time_limit),align="center",font=("Arial",16,"normal"))
    screen.update()

# 게임 종료 처리
score_turtle.clear()
time_turtle.clear()
gameover_turtle=turtle.Turtle()
gameover_turtle.penup()
gameover_turtle.goto(0,0)
gameover_turtle.write("Game Over",align="center",font=("Arial",24,"normal"))

turtle.done()