import pygame,time,random
pygame.init()
display_width=800
display_height=600
black=(0,0,0)
red=(255,0,0)
white=(255,255,255)

car_width=69
 
carImg=pygame.image.load("carImage.png")
gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Avoid Game')
clock=pygame.time.Clock()


def things(thingx,thingy,thingw,thingh,color):
	pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])




def car(x,y):
	gameDisplay.blit(carImg,(x,y))

def crash():
	message_display('You Crashed')

def text_objects(text,font):
	textSurface=font.render(text,True,black)
	return textSurface,textSurface.get_rect() 


def things_dodged(count):
	font=pygame.font.SysFont(None,25)
	text=font.render("DODGED: "+str(count),True,black)
	gameDisplay.blit(text,(0,0))

def message_display(text):
	largeText=pygame.font.Font('freesansbold.ttf',115)
	TextSurf,TextRect=text_objects(text,largeText)
	TextRect.center=((display_width/2),(display_height/2))
	gameDisplay.blit(TextSurf,TextRect)
	pygame.display.update()

	time.sleep(2)
	game_loop()

def game_loop():
	thing_startx=random.randrange(0,display_width)
	thing_starty=-600
	thing_speed=4
	thing_width=100
	thing_height=100
	x=display_width*.45
	y=display_height*.80
	x_change=0
	gameExit=False
	dodged=0
	while(not gameExit):
		for event in pygame.event.get():
			if(event.type==pygame.QUIT):
				pygame.quit()
				quit()

		if(event.type==pygame.KEYDOWN):
			if(event.key==pygame.K_LEFT):
				x_change=-5
				
			if(event.key==pygame.K_RIGHT):
				x_change=5

		if(event.type==pygame.KEYUP):
			if(event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT):
				x_change=0

		x+=x_change
		if(x<0 or x>display_width-car_width):
			crash()
		if(thing_starty>display_height):
			thing_starty=-thing_height
			thing_startx=random.randrange(0,display_width)
			dodged+=1
			thing_speed+=1
			thing_width+=(dodged*1.2)

		gameDisplay.fill(white)
		#things(thingx,thingy,thingw,thingh,color):
		things(thing_startx,thing_starty,thing_width,thing_height,black)
		thing_starty+=thing_speed
		car(x,y)
		things_dodged(dodged)

		if(y<thing_starty+thing_height):
			print('y crossover')
			if(x>thing_startx and x<thing_startx+thing_width or x+car_width>thing_startx and x+car_width<thing_startx+thing_width):
				print('x crossover')
				crash()
		

		pygame.display.update()

		clock.tick(60)
game_loop()
pygame.quit()
quit()