import pygame
import sys
import random
from itertools import cycle
from pygame.locals import *

# setting speed of game
FPS = 30
FPSCLOCK = pygame.time.Clock()

#setting game screen
SCREENWIDTH = 512
SCREENHEIGHT = 512
SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
pygame.display.set_caption('space')

#creating dictionary
IMAGES = {}
SOUNDS = {}
FONTS = {}

def main():
	pygame.init()
	pygame.font.init()
	
	# background surface created and stored
	IMAGES['background'] = 	pygame.image.load('sprite/Images/Background/background.jpg').convert()

	# player surface resized and stored
	IMAGES['player'] = (	pygame.transform.scale( pygame.image.load('sprite/Images/Blue/Animation/1.png').convert_alpha(), (100,100) ),
				pygame.transform.scale( pygame.image.load('sprite/Images/Blue/Animation/2.png').convert_alpha(), (100,100) ),
				pygame.transform.scale( pygame.image.load('sprite/Images/Blue/Animation/3.png').convert_alpha(), (100,100) ),
				pygame.transform.scale( pygame.image.load('sprite/Images/Blue/Animation/4.png').convert_alpha(), (100,100) ),
				pygame.transform.scale( pygame.image.load('sprite/Images/Blue/Animation/5.png').convert_alpha(), (100,100) ),
				pygame.transform.scale( pygame.image.load('sprite/Images/Blue/Animation/6.png').convert_alpha(), (100,100) ),
				pygame.transform.scale( pygame.image.load('sprite/Images/Blue/Animation/7.png').convert_alpha(), (100,100) ),
				pygame.transform.scale( pygame.image.load('sprite/Images/Blue/Animation/8.png').convert_alpha(), (100,100) ) 
		   	   )
		   	   
	# enemy surface rotated,resized and stored
	IMAGES['enemy'] = (	pygame.transform.rotate(pygame.transform.scale( pygame.image.load('sprite/Images/Red/Enemy_animation/1.png').convert_alpha(), (100,100) ),180),
				pygame.transform.rotate(pygame.transform.scale( pygame.image.load('sprite/Images/Red/Enemy_animation/2.png').convert_alpha(), (100,100) ),180),
				pygame.transform.rotate(pygame.transform.scale( pygame.image.load('sprite/Images/Red/Enemy_animation/3.png').convert_alpha(), (100,100) ),180),
				pygame.transform.rotate(pygame.transform.scale( pygame.image.load('sprite/Images/Red/Enemy_animation/4.png').convert_alpha(), (100,100) ),180),
				pygame.transform.rotate(pygame.transform.scale( pygame.image.load('sprite/Images/Red/Enemy_animation/5.png').convert_alpha(), (100,100) ),180),
				pygame.transform.rotate(pygame.transform.scale( pygame.image.load('sprite/Images/Red/Enemy_animation/6.png').convert_alpha(), (100,100) ),180),
				pygame.transform.rotate(pygame.transform.scale( pygame.image.load('sprite/Images/Red/Enemy_animation/7.png').convert_alpha(), (100,100) ),180),
				pygame.transform.rotate(pygame.transform.scale( pygame.image.load('sprite/Images/Red/Enemy_animation/8.png').convert_alpha(), (100,100) ),180)					
			  ) 
	
	# player dead effects
	IMAGES['dead'] = (	pygame.transform.scale( pygame.image.load('sprite/Images/Effects/Blue_Effects/1_0.png').convert_alpha(),(100,100)),
				pygame.transform.scale( pygame.image.load('sprite/Images/Effects/Blue_Effects/1_1.png').convert_alpha(),(100,100)),
				pygame.transform.scale( pygame.image.load('sprite/Images/Effects/Blue_Effects/1_2.png').convert_alpha(),(100,100)),
				pygame.transform.scale( pygame.image.load('sprite/Images/Effects/Blue_Effects/1_3.png').convert_alpha(),(100,100)),
				pygame.transform.scale( pygame.image.load('sprite/Images/Effects/Blue_Effects/1_4.png').convert_alpha(),(100,100)),
				pygame.transform.scale( pygame.image.load('sprite/Images/Effects/Blue_Effects/1_5.png').convert_alpha(),(100,100)),
				pygame.transform.scale( pygame.image.load('sprite/Images/Effects/Blue_Effects/1_6.png').convert_alpha(),(100,100)),
				pygame.transform.scale( pygame.image.load('sprite/Images/Effects/Blue_Effects/1_7.png').convert_alpha(),(100,100)),
				pygame.transform.scale( pygame.image.load('sprite/Images/Effects/Blue_Effects/1_8.png').convert_alpha(),(100,100)),
				pygame.transform.scale( pygame.image.load('sprite/Images/Effects/Blue_Effects/1_9.png').convert_alpha(),(100,100)),
				pygame.transform.scale( pygame.image.load('sprite/Images/Effects/Blue_Effects/1_10.png').convert_alpha(),(100,100)),
				pygame.transform.scale( pygame.image.load('sprite/Images/Effects/Blue_Effects/1_11.png').convert_alpha(),(100,100)),
				pygame.transform.scale( pygame.image.load('sprite/Images/Effects/Blue_Effects/1_12.png').convert_alpha(),(100,100)),
				pygame.transform.scale( pygame.image.load('sprite/Images/Effects/Blue_Effects/1_13.png').convert_alpha(),(100,100)),
				pygame.transform.scale( pygame.image.load('sprite/Images/Effects/Blue_Effects/1_14.png').convert_alpha(),(100,100)),
				pygame.transform.scale( pygame.image.load('sprite/Images/Effects/Blue_Effects/1_15.png').convert_alpha(),(100,100)),
				pygame.transform.scale( pygame.image.load('sprite/Images/Effects/Blue_Effects/1_16.png').convert_alpha(),(100,100))
				
			 )
			 
	# enemy dead effects
	IMAGES['kill'] = (	pygame.transform.scale( pygame.image.load('sprite/Images/Effects/Red_Effects/1_0.png').convert_alpha(),(100,100)),
				pygame.transform.scale( pygame.image.load('sprite/Images/Effects/Red_Effects/1_1.png').convert_alpha(),(100,100)),
				pygame.transform.scale( pygame.image.load('sprite/Images/Effects/Red_Effects/1_2.png').convert_alpha(),(100,100)),
				pygame.transform.scale( pygame.image.load('sprite/Images/Effects/Red_Effects/1_3.png').convert_alpha(),(100,100)),
				pygame.transform.scale( pygame.image.load('sprite/Images/Effects/Red_Effects/1_4.png').convert_alpha(),(100,100)),
				pygame.transform.scale( pygame.image.load('sprite/Images/Effects/Red_Effects/1_5.png').convert_alpha(),(100,100)),
				pygame.transform.scale( pygame.image.load('sprite/Images/Effects/Red_Effects/1_6.png').convert_alpha(),(100,100)),
				pygame.transform.scale( pygame.image.load('sprite/Images/Effects/Red_Effects/1_7.png').convert_alpha(),(100,100)),
				pygame.transform.scale( pygame.image.load('sprite/Images/Effects/Red_Effects/1_8.png').convert_alpha(),(100,100)),
				pygame.transform.scale( pygame.image.load('sprite/Images/Effects/Red_Effects/1_9.png').convert_alpha(),(100,100)),
				pygame.transform.scale( pygame.image.load('sprite/Images/Effects/Red_Effects/1_10.png').convert_alpha(),(100,100)),
				pygame.transform.scale( pygame.image.load('sprite/Images/Effects/Red_Effects/1_11.png').convert_alpha(),(100,100)),
				pygame.transform.scale( pygame.image.load('sprite/Images/Effects/Red_Effects/1_12.png').convert_alpha(),(100,100)),
				pygame.transform.scale( pygame.image.load('sprite/Images/Effects/Red_Effects/1_13.png').convert_alpha(),(100,100)),
				pygame.transform.scale( pygame.image.load('sprite/Images/Effects/Red_Effects/1_14.png').convert_alpha(),(100,100)),
				pygame.transform.scale( pygame.image.load('sprite/Images/Effects/Red_Effects/1_15.png').convert_alpha(),(100,100)),
				pygame.transform.scale( pygame.image.load('sprite/Images/Effects/Red_Effects/1_16.png').convert_alpha(),(100,100))
			 )
	
	# numbers for score
	IMAGES['numbers'] = (	pygame.image.load('sprite/Images/Digits/0.png').convert_alpha(),
        			pygame.image.load('sprite/Images/Digits/1.png').convert_alpha(),
        			pygame.image.load('sprite/Images/Digits/2.png').convert_alpha(),
        			pygame.image.load('sprite/Images/Digits/3.png').convert_alpha(),
        			pygame.image.load('sprite/Images/Digits/4.png').convert_alpha(),
        			pygame.image.load('sprite/Images/Digits/5.png').convert_alpha(),
        			pygame.image.load('sprite/Images/Digits/6.png').convert_alpha(),
        			pygame.image.load('sprite/Images/Digits/7.png').convert_alpha(),
	        		pygame.image.load('sprite/Images/Digits/8.png').convert_alpha(),
       		 		pygame.image.load('sprite/Images/Digits/9.png').convert_alpha()
        
        		    )  
	
	# bullet surface created, resized and stored
	
	IMAGES['bullet'] = 	pygame.transform.scale( pygame.image.load('sprite/Images/Blue/bullet.png').convert_alpha() , (50,50) )
				
	# bulletX surface created,rotated,resized and stored
	IMAGES['bulletX'] = 	pygame.transform.rotate(pygame.transform.scale( pygame.image.load('sprite/Images/Red/bullet_red.png').convert_alpha() , (50,50) ),180)
	# asteroids....FIND CODE TO RANDOMIZE
	IMAGES['stone'] = (	pygame.transform.scale(pygame.image.load('sprite/Images/Aestroids/aestroid_brown.png').convert_alpha(),(100,100)),
				pygame.transform.scale(pygame.image.load('sprite/Images/Aestroids/aestroid_dark.png').convert_alpha(),(100,100)),
				pygame.transform.scale(pygame.image.load('sprite/Images/Aestroids/aestroid_gay_2.png').convert_alpha(),(100,100)),
				pygame.transform.scale(pygame.image.load('sprite/Images/Aestroids/aestroid_gray.png').convert_alpha(),(100,100))
	
			  )
		
	# game over
	IMAGES['gameover'] = pygame.image.load('sprite/Images/Menu/gameover.png').convert_alpha()
	
	# entering the game
	while True:
		crashInfo = maingame()
		showGameOverScreen(crashInfo)
		
# game over screen

'''
this is difficult to understand....so I am explaining it

when the game is over we need to blit some things on the screen
the background, the score and a game over text will be shown on screen when a player dies as per below code
to show the above images, their position at the exact time of death is needed
this is obtained from dictionary crashinfo
'''
def showGameOverScreen(crashInfo):
	leftStone = crashInfo['leftStone']
	rightStone = crashInfo['rightStone']
	playerX = crashInfo['x']
	playerY = crashInfo['y']
	score = crashInfo['score']
	dead_index = -1
	
	while True:
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
				pygame.quit()
				sys.exit()
			# game restart if space is pressed
			if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
				return
		SCREEN.blit(IMAGES['background'],(0,0))
		for lStone, rStone in zip(leftStone, rightStone):
			SCREEN.blit(IMAGES['stone'][0]    ,(lStone['x']  ,lStone['y'] ))
			SCREEN.blit(IMAGES['stone'][0]    ,(rStone['x']  ,rStone['y'] ))
		
		dead_index+=1
		if dead_index>16:
			SCREEN.blit(IMAGES['gameover'],(SCREENWIDTH/2 - IMAGES['gameover'].get_width()/2,SCREENHEIGHT/2 - IMAGES['gameover'].get_height()/2))
		else:
			SCREEN.blit(IMAGES['dead'][dead_index], (playerX, playerY))
		showScore(score)
		FPSCLOCK.tick(FPS)
		pygame.display.update()	
		
# show score
def showScore(score):
	scoreDigits = str(score)
	Xoffset = 0 
	for digit in scoreDigits:
		SCREEN.blit(IMAGES['numbers'][int(digit)], (Xoffset, SCREENHEIGHT - IMAGES['numbers'][0].get_height()))
		Xoffset += IMAGES['numbers'][int(digit)].get_width()

# get asteroids
def getRandomStone():
	
	stoneGap = random.randrange(250,300)
	stoneNumber = int(random.randrange(0,4))
	
	gapX = random.randrange(0,SCREENWIDTH/2-100)
	stoneY = 0 - 100
	
	LEFTS = {'x':gapX ,'y':stoneY }
	RIGHTS = {'x':gapX + stoneGap,'y':stoneY }
	stonePos = [LEFTS,RIGHTS]
	
	return stonePos
	
# getting the coordinates of bullet
def getBullet(playerX,playerY):
	bulletPos = {'x':playerX+23,'y':playerY} 	# 23 is obtained by playerW/2 - bulletW/2 -2(correction...T/E)
	return bulletPos

# getting the coordinates of bulletX
def getBulletX(enemyX,enemyY):
	bulletXPos = {'x':enemyX+23,'y':enemyY}
	return bulletXPos
	
# player death	
def checkCrash(player,leftStone,rightStone,bulletX):
	playerRect = pygame.Rect(player['x']+10,player['y']+10,80,80) # numbers tweaked to decrease instant death
	
	# stone collision
	for lStone,rStone in zip(leftStone,rightStone):
		lStoneRect = pygame.Rect(lStone['x']+10,lStone['y']+10,80,80)
		rStoneRect = pygame.Rect(rStone['x']+10,rStone['y']+10,80,80)
		collision1 = playerRect.colliderect(lStoneRect)
		collision2 = playerRect.colliderect(rStoneRect)
		if collision1 or collision2:
			return True
			
	# bullet hit
	for ax in bulletX:
		axRect = pygame.Rect(ax['x']+5,ax['y']+5,40,40)
		bulletHit = playerRect.colliderect(axRect)
		if bulletHit:
			return True
	# no crash
	return False

# enemy death
def checkKill(enemy,bullet):
	for e in enemy:
		enemyRect=pygame.Rect(e['x'],e['y'],100,100)
		for a in bullet:
			aRect = pygame.Rect(a['x'],a['y'],50,50)
			bulletHit = enemyRect.colliderect(aRect)
			if bulletHit:
				return True
		return False		

# check bullet clash
def checkClash(bullet,bulletX,leftStone,rightStone):
	
	for a in bullet:						# 10 and 30 used to decrease size of bullet rectangle
		aRect = pygame.Rect(a['x']+10,a['y']+10,30,30)
		for ax in bulletX:
			axRect = pygame.Rect(ax['x']+10,ax['y']+10,30,30)
			bulletClash = aRect.colliderect(axRect)
			if bulletClash:					# return the position of bullet that clashed in list
				axSet = bulletX.index(ax)
				aSet = bullet.index(a) 		
				return [True,aSet,axSet]
			for lStone,rStone in zip(leftStone,rightStone):		# check bullet clash with stone
				lStoneRect = pygame.Rect(lStone['x'],lStone['y'],100,100)
				rStoneRect = pygame.Rect(rStone['x'],rStone['y'],100,100)
				stoneClash1 = aRect.colliderect(lStoneRect)
				stoneClash2 = aRect.colliderect(rStoneRect)
				if stoneClash1 or stoneClash2:
					aSet = bullet.index(a)
					axSet = bulletX.index(ax) 		
					return [True,aSet,axSet]
	return [False,0,0]

def maingame():
	
	# player animation variables
	player_no = cycle([0,1,2,3,4,5,6,7])
	player_index = 0
	loopiter = 0
	
	# score variable
	score = 0
	
	# player control variable
	playerVelX = 0
	leftKeyPressed = False
	rightKeyPressed = False
	
	# enemy control variable
	enemyVelX = 0
	
	# enemy bullet auto-control variable
	loopBullet = 0
	
	# player position
	playerW = IMAGES['player'][0].get_width()
	playerH = IMAGES['player'][0].get_height()
	playerX = ( SCREENWIDTH - playerW )/2
	playerY = SCREENHEIGHT - playerH
	
	# enemy position
	initEnemyPos = {'x':int(random.randrange(0,SCREENWIDTH - 100)),'y':0}
	enemy = [initEnemyPos]

	# Bullet position
	bullet = []
	bulletVelY = -10
	
	# BulletX position
	for e in enemy:
		bulletX = []
		bulletXVelY = 10
		
	kill_effect = False
	kill_index = 0
	damage = 1
	
	# Asteroid position
	
	newStone1 = getRandomStone()
	newStone2  = getRandomStone()
	newStone3 = getRandomStone()
	
	leftStone = [ 	newStone1[0],
			{'x': newStone2[0]['x'], 'y':(newStone2[0]['y']-SCREENHEIGHT/2)},
			{'x': newStone3[0]['x'],'y':(newStone3[0]['y']-SCREENHEIGHT)}
		    ]
	
	rightStone = [ 	newStone1[1],
			{'x': newStone2[1]['x'], 'y':(newStone2[1]['y']-SCREENHEIGHT/2)},
			{'x': newStone3[1]['x'],'y':(newStone3[1]['y']-SCREENHEIGHT)}
		     ]
	
	stoneVelY = 5	
		
	# running the game
	while True:
								
		for event in pygame.event.get():
			
			# quit game
			if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
				pygame.quit()
				sys.exit()
			# player controls
				
			if event.type == KEYDOWN:
				# movement control
				if event.key == K_LEFT:
					leftKeyPressed = True
				if event.key == K_RIGHT:
					rightKeyPressed = True
				# shoot control
				if event.key == K_SPACE:
					ammo = getBullet(playerX,playerY)
					bullet.append(ammo)
			if event.type == KEYUP:
				if event.key == K_LEFT:
					leftKeyPressed = False
				if event.key == K_RIGHT:
					rightKeyPressed = False
			
		# to move player continuously as key is pressed
		if leftKeyPressed == True:
			playerVelX = -5
		elif rightKeyPressed == True:
			playerVelX = 5
		else:
			playerVelX = 0
		
		# animation speed control
		loopiter +=1
		if loopiter%3 == 0:
			player_index = next(player_no)
			enemyVelX = random.randrange(-50,50)
		
		# changing player position and restricting the position of player inside the screen	
		playerX = min( max (playerX + playerVelX , 0) , (SCREENWIDTH - playerW) ) 
		
		# changing enemy position and restricting the position of player inside the screen
		for e in enemy:
			e['x'] = min( max (e['x'] + enemyVelX , 0) , (SCREENWIDTH - playerW) )  
			
		# Aestroid control
		for lStone,rStone in zip(leftStone,rightStone):
			lStone['y']+=stoneVelY
			rStone['y']+=stoneVelY
			
		if leftStone[0]['y']>(SCREENHEIGHT + 100):
			leftStone.pop(0)
			rightStone.pop(0)
			
			newStoneSet = getRandomStone()
			
			leftStone.append(newStoneSet[0])
			rightStone.append(newStoneSet[1])
			
		# Bullet control
		for a in bullet:
			a['y']+=bulletVelY
			if a['y']<-50:
				bullet.pop(0)
			
		# BulletX control
		for ax in bulletX:
			ax['y']+=bulletXVelY
			if ax['y']>(SCREENHEIGHT + 50):
				bulletX.pop(0)
			
		# bulletX auto-shoot
		loopBullet+=1
		if loopBullet%10==0:	# increse number after % to decrease number of enemy bullets 
			for e in enemy:
				ammoX=getBulletX(e['x'],e['y'])
				bulletX.append(ammoX)
		
		# score
		playerMidPos = playerY + IMAGES['player'][0].get_height() / 2
		for lStone in leftStone:
			stoneMidPos = lStone['y'] + IMAGES['stone'][0].get_height() / 2
			if stoneMidPos >= playerMidPos and playerMidPos > stoneMidPos - 4:  # 4 is obtained by trial and error
				score += 1
				
		# drawing image surfaces (stored in dictionary) on screen
		SCREEN.blit(IMAGES['background'],(0,0))
		SCREEN.blit(IMAGES['player'][player_index],( playerX, playerY ) )
		
		for e in enemy:
			SCREEN.blit(IMAGES['enemy'][player_index],(e['x'],e['y']))
		
		# drawing aestroids
		for lStone, rStone in zip(leftStone, rightStone):
			SCREEN.blit(IMAGES['stone'][0]    ,(lStone['x']  ,lStone['y'] ))
			SCREEN.blit(IMAGES['stone'][0]    ,(rStone['x']  ,rStone['y'] ))
		
		# drawing bullet
		for a in bullet:
			SCREEN.blit(IMAGES['bullet'],(a['x'],a['y']))
		
		# drawing bulletX
		for ax in bulletX:
			SCREEN.blit(IMAGES['bulletX'],(ax['x'],ax['y']))
		
		# kill check
		killTest = checkKill(enemy,bullet)
		# what to do if enemy killed
		if killTest or kill_effect:
			damage+=1						# enemy health 0 when 10 bullet hits
			if damage > 10:
				for e in enemy:
					killPos = (e['x'],e['y'])
					enemy.pop(0)
					score+=1				# bonus score on enemy kill
					kill_index = 0
		
				if kill_index==17:				# when enemy dead effect finish, new enemy added
					enemy.append(initEnemyPos)
					damage = 1				# new enemy health reset
					kill_effect = False
				elif kill_index<17:				# enemy dead effect
					SCREEN.blit(IMAGES['kill'][kill_index], (killPos[0],killPos[1]))
					kill_index += 1 
					kill_effect = True
		
		# check bullet clash
		clashTest=checkClash(bullet,bulletX,leftStone,rightStone)
		
		# what to do if bullet clashes
		if clashTest[0]:
			bullet.pop(clashTest[1])
			bulletX.pop(clashTest[2])				
		
		# crash check
		crashTest = checkCrash(	{'x':playerX,'y':playerY},
					leftStone,rightStone,bulletX
					)
		# what to do if player dies
		if crashTest:
			
			return {'x':playerX,
				'y':playerY,
				'leftStone':leftStone,
				'rightStone':rightStone,
				'score':score
			       }
			       
		showScore(score)

		#update changes in every frame
		pygame.display.update()
		
		# slowing down the processor clock to FPS set by us
		FPSCLOCK.tick(FPS)

# program starts from here
if __name__ == '__main__':
	main()
