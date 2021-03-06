import pygame
from pygame import mixer
from button import button
import ctypes
import os
import var

user32 = ctypes.windll.user32
width1, height1 = user32.GetSystemMetrics(78), user32.GetSystemMetrics(79)
 #initialize the pygame library
width=(width1//3)*2
height=(height1//3)*2
x=(width1//2)-(width//2)
y=height1-height
screen = pygame.display.set_mode((width, height))

os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (x,y)
os.environ['SDL_VIDEO_CENTERED'] = '0'

pygame.display.flip()
background=pygame.image.load(r'py Game\images\bg.png')
background = pygame.transform.scale(background, (width, height))

running=True

mixer.init()
mixer.music.load('py Game\music\\bensound-summer_mp3_music.mp3')
mixer.music.play()

play1= pygame.image.load('py Game\images\start.png')
button1=button((width//2,height-(height//5)-120),30,play1,screen)

play2= pygame.image.load('py Game\images\HS.png')
button2=button((width//2,height-(height//5)-20),30,play2,screen)


play4= pygame.image.load('py Game\images\sound.png')
button4=button((width-60,height-(height//5)-50),30,play4,screen)



play5= pygame.image.load('py Game\images\\about.png')
button5=button((width-60,height-(height//5)+50),30,play5,screen)
pygame.init()


screen.blit(background,(0,0))
button1.draw()
button2.draw()
button4.draw()
button5.draw()
while running:
    
    #button6.draw()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            
        button1.click(event)
        button2.clickHigh(event)
        button4.music(event,var.bol,width=width,height=height)
        button5.about(event)
    pygame.display.update()
    pygame.display.flip()    
     
pygame.quit()


