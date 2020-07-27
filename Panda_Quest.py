import random
import sys
import pygame
import webbrowser
from pygame.locals import *


pygame.init()

fps = 32 # frames per second

ws = 558 # width of screen
hs = 852 # height of screen

screen = pygame.display.set_mode((ws,hs))

#loading all the images

img = {}

panda = pygame.image.load('assets/sprites/others/panda.png').convert_alpha()

bg = pygame.image.load('assets/sprites/others/bg.jpg').convert_alpha()

pipe = pygame.image.load( 'assets/sprites/others/pipe.png').convert_alpha()

over = pygame.image.load( 'assets/sprites/others/gameover.png' ).convert_alpha()

cherry = pygame.image.load('assets/sprites/others/cherry.png').convert_alpha()


fb = pygame.image.load('assets/sprites/social/fb.png').convert_alpha()

insta = pygame.image.load('assets/sprites/social/insta.png').convert_alpha()

git = pygame.image.load('assets/sprites/social/git.png').convert_alpha()

again = pygame.image.load('assets/sprites/others/again.png').convert_alpha()

name = {
    'P' : pygame.image.load( 'assets/sprites/letters/P.png' ).convert_alpha(),
    'A' : pygame.image.load( 'assets/sprites/letters/A.png' ).convert_alpha(),
    'N' : pygame.image.load( 'assets/sprites/letters/N.png' ).convert_alpha(),
    'D' : pygame.image.load( 'assets/sprites/letters/D.png' ).convert_alpha(),
    'Q' : pygame.image.load( 'assets/sprites/letters/Q.png' ).convert_alpha(),
    'U' : pygame.image.load( 'assets/sprites/letters/U.png' ).convert_alpha(),
    'E' : pygame.image.load( 'assets/sprites/letters/E.png' ).convert_alpha(),
    'S' : pygame.image.load( 'assets/sprites/letters/S.png' ).convert_alpha(),
    'T' : pygame.image.load( 'assets/sprites/letters/T.png' ).convert_alpha(),
    
    }

img['numbers'] = (
    pygame.image.load( 'assets/sprites/numbers/0.png' ).convert_alpha(),
    pygame.image.load( 'assets/sprites/numbers/1.png' ).convert_alpha(),
    pygame.image.load( 'assets/sprites/numbers/2.png' ).convert_alpha(),
    pygame.image.load( 'assets/sprites/numbers/3.png' ).convert_alpha(),
    pygame.image.load( 'assets/sprites/numbers/4.png' ).convert_alpha(),
    pygame.image.load( 'assets/sprites/numbers/5.png' ).convert_alpha(),
    pygame.image.load( 'assets/sprites/numbers/6.png' ).convert_alpha(),
    pygame.image.load( 'assets/sprites/numbers/7.png' ).convert_alpha(),
    pygame.image.load( 'assets/sprites/numbers/8.png' ).convert_alpha(),
    pygame.image.load( 'assets/sprites/numbers/9.png' ).convert_alpha()
)

img['speaker'] = (
    pygame.image.load( 'assets/sprites/others/off.png' ).convert_alpha(),
    pygame.image.load( 'assets/sprites/others/on.png'  ).convert_alpha()
    )

img['pipes'] = ( pygame.transform.rotate(pipe,180),pipe)


#loading all the sounds

sound = {}
sound[ 'die' ] = pygame.mixer.Sound('assets/audio/die.wav')
sound[ 'hit' ] = pygame.mixer.Sound('assets/audio/hit.wav')
sound[ 'point' ] = pygame.mixer.Sound('assets/audio/point.wav')
sound[ 'wing' ] = pygame.mixer.Sound('assets/audio/wing.wav')
sound[ 'swoosh' ] = pygame.mixer.Sound('assets/audio/swoosh.wav')



panda_h = panda.get_height()
panda_w = panda.get_width()

pipe_w = pipe.get_width()
pipe_h = pipe.get_height()
pipe_vel = -6
cherry_w = cherry.get_width()
cherry_h = cherry.get_height()

fb_w = fb.get_width()
insta_w = insta.get_width()
git_w = git.get_width()



clck = pygame.time.Clock()

pygame.display.set_caption('Panda Quest by Aditya Sinha')




def welcome():
    # welcome screen
    
    yy = hs-60
    social = [ [fb,fb_w], [insta,insta_w], [git,git_w] ]
    off = 5 # offset
    xx = ws - 3*off - fb_w - insta_w - git_w
    brows = [ [fb,xx,yy], [insta,xx,yy], [git,xx,yy] ]
    while True:
        for event in pygame.event.get():
            
            if event.type == QUIT or ( event.type == KEYDOWN and event.key == K_ESCAPE ) :
                pygame.quit()
                sys.exit()
            
            elif event.type == KEYDOWN and ( event.key== K_SPACE or event.key == K_UP ):
                return
            
            elif event.type == MOUSEBUTTONDOWN :
                # my accounts

                mx, my =  pygame.mouse.get_pos()
                
                if brows[0][1]    <=  mx  <=  brows[0][1]  +  fb_w     and   brows[0][2]  <=  my  <=  brows[0][2]  +  fb.get_height()    :
                    webbrowser.open( 'https://www.facebook.com/profile.php?id=100038773941060' )
                
                elif brows[1][1]  <=  mx  <=  brows[1][1]  +  insta_w  and   brows[1][2]  <=  my  <=  brows[1][2]  +  insta.get_height() :
                    webbrowser.open( 'https://www.instagram.com/aditya113141' )
                
                elif brows[2][1]  <=  mx  <=  brows[2][1]  +   git_w   and   brows[2][2]  <=  my  <=  brows[2][2]  +  git.get_height()   :
                    webbrowser.open( 'https://github.com/aditya113141/' )
            
            else:
                screen.blit( bg,(0,0) )
                screen.blit( panda,( int(ws/5), int(hs/2) ) ) 
                xx  =  ws - 3 * off - fb_w - insta_w - git_w
                
                for a in social:
                    screen.blit( a[0], (xx, yy ) )

                    for b in brows:
                        if b[0] == a[0]:
                            b[1] =  xx
                  
                    xx +=   a[1] + off
                
                dif = -20
                
                str1    = "PANDA"
                str1_x  = int(ws/5)
                str1_y  = int(hs/20)
                
                for ch in str1:
                    screen.blit( name[ ch ], (str1_x,str1_y) )
                    str1_x += name[ ch ].get_width() +  dif
            
            
                str2   = "QUEST"
                str2_x = int(ws/5-dif/2)
                str2_y = int(str1_y - 4*dif)

                for ch in str2:
                    screen.blit( name[ch], (int(str2_x), str2_y) )
                    str2_x  +=  name[ ch ].get_width()  +  dif
                
                
                pygame.display.update()
                clck.tick(fps)




def game_over():
    #displays game over message
    
    while True:
       
        for event in pygame.event.get() :

            if event.type  ==  QUIT  or  ( event.type  ==  KEYDOWN  and  event.key  ==  K_ESCAPE):
                pygame.quit()
                sys.exit()
            
            elif event.type  ==  KEYDOWN  and ( event.key  ==  K_SPACE  or  event.key  ==  K_UP):
                return
            
            else:
                final_display()
               
                xx = int(ws/2 - over.get_width()/2)
                yy = int(hs/2)
                screen.blit( over, ( xx, yy ) )
               
                yy += 10 + over.get_height()
                xx  = int( ( ws - again.get_width() ) / 2 )
                screen.blit( again, ( xx, yy ) )
                
                pygame.display.update()
                clck.tick(fps)


def display_score():
    

        digits = [int(x) for x in list(str(score))]
       
        width  = 0
       
        for digit in digits:
            width += img[ 'numbers' ][ digit ].get_width()
       
        xoff  =  (ws-width)/2

        for digit in digits:
            screen.blit( img['numbers'][ digit ], ( int(xoff), int( hs* 0.15 ) ) )
            xoff    +=   img[ 'numbers' ][ digit ]. get_width()

        digits  =  [int(x) for x in list(str(cherry_score))]
       
        for digit in digits:
            width  +=  img['numbers'][digit].get_width()
       
        xoff = ( ws-width  -  cherry_w ) - 20

        screen.blit ( cherry, ( int(xoff), int(hs/10)) )
       
        xoff += cherry_w
       
        for digit in digits:
            screen.blit( img['numbers'][ digit ], ( int(xoff), int(hs/10) ) )
            xoff += img['numbers'][ digit ].get_width()
        

def check_crash( panda_x, panda_y, up_pipe, low_pipe ) :
    

    if panda_y  >  hs  -  panda_h - 5:
        return True
    
    for Pipe in up_pipe:
        if( panda_y  <  pipe_h  +  Pipe['y']   and   abs( panda_x  -  Pipe['x'] )  <  pipe_w  -  30 ):
            return True

    for Pipe in low_pipe:
        if(  panda_y  +  panda_h  >  Pipe['y']  and  abs(panda_x  -  Pipe['x'] )   <  pipe_w  -  30 ):
            return True
    
    return False

def final_display():
        
        screen.blit(bg,(0,0))
        
        for  a,b  in  zip(up_pipe,low_pipe):
            screen.blit( img['pipes'][ 0 ], ( int( a['x'] ), int( a['y'] )))
            screen.blit( img['pipes'][ 1 ], ( int( b['x'] ), int( b['y'] )))
        
        for a in Cherries:
            screen.blit( cherry, (a['x'],a['y']) )
        
        screen.blit( panda, ( int(panda_x), int(panda_y) ) )
        
        screen.blit( img['speaker'][music], (10,10) )
        
        display_score()

def game():
    global panda_x, panda_y, score, up_pipe, low_pipe, cherry_score, Cherries, music
   
    score        = 0
    cherry_score = 0

    panda_x = int(ws/5)
    panda_y = int(hs/2)
    
    set_f = ra_pip()
    set_s = ra_pip()
    
    up_pipe  = [ {'x' :  ws +200, 'y' : set_f[0]['y'] }, { 'x' : int( 3*ws/2 +200 ) , 'y' :  set_s[ 0 ][ 'y' ] } ]
    low_pipe = [ {'x' :  ws +200, 'y' : set_f[1]['y'] }, { 'x' : int( 3*ws/2 +200 ) , 'y' :  set_s[ 1 ][ 'y' ] } ]
    
    panda_vel     = -9
    panda_vel_max = 10
    panda_vel_min = -8
    panda_acc     =  1
    
    flap     = False
    flap_vel =  -10
    
    Cherries = []
   
    music = 1
    
    
    
    while True:
        
        for event in pygame.event.get():
            
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            
            if event.type == KEYDOWN  and (event.key == K_SPACE or event.key==K_UP):
                if panda_y>0:
                    panda_vel = flap_vel
                    flap =True
                    if music == 1:
                        sound['wing'].play()
            
            
            if event.type == KEYDOWN and event.key == K_m:
                music = 1-music
           
        crash        =   check_crash(panda_x,panda_y,up_pipe,low_pipe)
        cherry_score =   ate_cherry(panda_x,panda_y,Cherries,cherry_score)
        
        if crash:
            if music == 1:
                sound['hit'].play()
            return
        
        
        panda_mid = int(panda_x + panda_w /2)
        
        
        for p in up_pipe :

            p_mid = p['x'] + pipe_w/2

            if p_mid <= panda_mid < p_mid + 6:
                score +=1
                if music ==1:
                    sound['point'].play()
        
        if panda_vel  <  panda_vel_max  and  flap==False:
            panda_vel += panda_acc
        
        if flap:
            flap = False
        
        panda_y   = panda_y + min( panda_vel, hs - panda_y-panda_h )
        
        if_cherry = random.randint( 0, 1 )
        
        for a,b in zip(up_pipe, low_pipe):
            a['x'] += pipe_vel
            b['x'] += pipe_vel
        
        for a in Cherries:
            a['x']+= pipe_vel
            
        if 0 < up_pipe[0]['x'] < 7 :
            new_pipe     = ra_pip()
            
            if if_cherry == 1:
                new_cherry = ra_cherry()
                Cherries.append(new_cherry)
            
            up_pipe.append  ( new_pipe[0] )
            low_pipe.append ( new_pipe[1] )
            
        if up_pipe[0]['x'] < - pipe_w:
            up_pipe.pop(0)
            low_pipe.pop(0)
        
        if  len(Cherries) != 0   and  Cherries[ 0 ][ 'x' ]  <  -cherry_w  :
            Cherries.pop(0)
        
        final_display()
        pygame.display.update()
        clck.tick(fps)
        
                         
        
def ate_cherry(panda_x,panda_y,Cherries,cherry_score):
    # checks if the panda has eaten a cherry or not
    for a in Cherries:
    
        if abs(panda_x-a['x'])<30 and abs(panda_y-a['y']) < 30:
    
            Cherries.remove(a)
    
            cherry_score = cherry_score + 1 
    
            break
    
    return cherry_score
        
            

def ra_pip():
    # generates random pipes
    gap = hs/3
    
    upper = random.randint(int((hs/12)),int((hs*7)/12))
    
    ylow  = int(upper+gap)
    
    x   = ws + 10
    
    yup = upper - pipe_h

    ret = [ { 'x' : x, 'y' : yup }, { 'x' : x, 'y' : ylow } ]
    
    return ret
    
def ra_cherry():
    # generates random cherries
    offset = 40
    
    x1 = int( ( ws + pipe_w ) / 2 ) + offset
    
    x2 = int(  ws - ( pipe_w) / 2 ) - offset
    
    cherry_x = random.randint(x1,x2)
    
    cherry_y = random.randint(int(offset),int(hs-offset))

    return { 'x' : cherry_x, 'y' : cherry_y }
    

while True:
# main game loop
    welcome()
    game()
    game_over()
