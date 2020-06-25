import turtle
import winsound
import math
import random


#set up screen
wn=turtle.Screen()
wn.bgcolor("black")
wn.title("Turtle Trigger")
wn.bgpic("giphy.gif")

#draw a border
border_pen=turtle.Turtle()
border_pen.speed(0)
border_pen.color("skyblue")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(2)
for i in range(4):
	border_pen.fd(600)
	border_pen.lt(90)
border_pen.hideturtle()	

#set the score to zero
score=0

score_pen=turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setpos(-290,280)
scorestring="Score: %s" %score
score_pen.write(scorestring,False,align="left",font=("Arial",14,"normal"))
score_pen.hideturtle()



#Create the player turtle
player=turtle.Turtle()
player.color("green")
player.shape("turtle")
player.penup()
player.speed(0)
player.setpos(0,-250)
player.shapesize(2,2)
player.setheading(90)
playerspeed=20



#enemy list
number_of_enemies=5
enemies=[]
for i in range(number_of_enemies):
	enemies.append(turtle.Turtle())

for enemy in enemies:
	enemy.color("red")
	enemy.shape("classic")
	enemy.penup()
	enemy.setheading(270)
	enemy.speed(0)
	enemy.shapesize(2,2)
	x=random.randint(-200,200)
	y=random.randint(-200,250)
	enemy.setposition(x,y)
	enemyspeed=2
	

#create player's weapon
weapon=turtle.Turtle()
weapon.color("gold")
weapon.shape("triangle")
weapon.penup()
weapon.speed(0)
weapon.setheading(90)
weapon.shapesize(1,1)
weapon.hideturtle()
weapon_speed=40

#define bullet state
#ready- ready to fire
#fire -bullet is firing
bulletstate="ready"

def fire_bullet():
	global bulletstate #write global just incase it needs to be changed
	if bulletstate=="ready":
	#move the bullet just above the player
		winsound.PlaySound("ws.wav",winsound.SND_ASYNC)
		bulletstate="fire"
		x=player.xcor()
		y=player.ycor()+20
		weapon.setposition(x,y)
		weapon.showturtle()
def isCollision(t1,t2):
	distance=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
	if distance<20:
		return True
	else:
		return False

#moving the player right
def move_right():
	x=player.xcor()
	x+=playerspeed
	if x>280:
		x=280
	player.setx(x)

#moving the player left
def move_left():
	x=player.xcor()
	x-=playerspeed
	if x<-280:
		x=-280
	player.setx(x)
	
#Create turtle bindings
turtle.listen()
turtle.onkeypress(move_left,"Left")
turtle.onkeypress(move_right,"Right")
turtle.onkeypress(fire_bullet,"space")

#Main game loop
while True:
	#move the enemy
	for enemy in enemies:
		x=enemy.xcor()
		x+=enemyspeed
		enemy.setx(x)
	
		if enemy.xcor()>280:
			for e in enemies:
				y=e.ycor()
				y-=40
				e.sety(y)
			enemyspeed*=-1
			
		if enemy.xcor()<-280:
			for e in enemies:
				y=e.ycor()
				y-=40
				e.sety(y)
			enemyspeed*=-1
		if isCollision(weapon,enemy):
			weapon.hideturtle()
			bulletstate="ready"
			weapon.setposition(0,-400)
			#changed the enemy position
			x=random.randint(-200,200)
			y=random.randint(100,250)
			enemy.setposition(x,y)
			#update the score
			score+=10
			scorestring="Score: %s" %score
			score_pen.clear()
			score_pen.write(scorestring,False,align="left",font=("Arial",14,"normal"))
			
		if enemy.distance(player) <= 50:
			for enemy in enemies:
				enemy.hideturtle()
			player.hideturtle()
			
			wn.clear()
			wn.bgpic("gameover2.gif")
			wn.bgcolor("black")
			turtle.done()
		
	#move the bullet
	if bulletstate=="fire":
		y=weapon.ycor()
		y+=weapon_speed
		weapon.sety(y)
	
	#check to see if bullet has gone to the top
	if weapon.ycor()>270:
		weapon.hideturtle()
		bulletstate="ready"


		
		
turtle.done()