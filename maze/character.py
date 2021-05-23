import tkinter as tk
import random
import mainGame
#import pygame
#from mutagen.mp3 import MP3 as mp3
ANIMATION = [0,1,0,2]
tmr = 0

key = ""
koff = False
ch_x = 90
ch_y = 90
ch_d = 1
ch_a = 3    


#パターンA敵の座標
ex = 0
ey = 0
ed = 0
ea = 0

#パターンB敵の座標
bx = 0
b_y = 0
bd = 0
ba = 0

#ビームの座標
gx = 0
gy = 0
ga = 0
gd = 0

#idx:(1:ゲームプレイ中,2:敵にぶつかった当たり判定)
idx = 0

tag_enemy = False
tag_enemy2 = False


map_data = [
    [0,1,1,1,1,0,0,1,1,1,1,0],
    [0,2,3,3,2,3,3,2,3,3,2,0],
    [0,3,0,0,3,3,3,3,0,0,3,0],
    [0,3,1,1,3,0,0,3,1,1,3,0],
    [0,3,2,2,3,0,0,3,2,2,3,0],
    [0,3,0,0,3,1,1,3,0,0,3,0],
    [0,3,1,1,3,3,3,3,1,1,3,0],
    [0,2,3,3,2,0,0,2,3,3,2,0],
    [0,0,0,0,0,0,0,0,0,0,0,0]
     ]

map_data_set = map_data
map_data1 = map_data
coin = 34

count = 1

h = 0

#CH = "image/ch.png"
#img_ch = tk.PhotoImage(file=CH)
#ch_x:主人公のx座標
#ch_y:主人公のy座標
#ch_x = 90
#ch_y = 90




#ビームを発射する
 
def move_missible():
    global gx,gy,ch_a,ch_x,ch_y,ga,gd,idx,tmr,ex,ey
    
    
    speed = 90
    if ch_a == 0:#上向きに向いている
        gy = ch_y
        gx = ch_x
        gy = gy - speed
        
    elif ch_a == 3:
        gy = ch_y
        gx = ch_x
        gy = gy + speed        
    elif ch_a == 6:
        gx = ch_x
        gy = ch_y
        gx = gx - speed
    elif ch_a == 9:
        gx = ch_x
        gy = ch_y
        gx = gx + speed
        
    ga = gd*3 + ANIMATION[tmr%4]

def setstage():
    global coin,map_data,map_data1
    map_data = [
    [0,1,1,1,1,0,0,1,1,1,1,0],
    [0,2,3,3,2,3,3,2,3,3,2,0],
    [0,3,0,0,3,3,3,3,0,0,3,0],
    [0,3,1,1,3,0,0,3,1,1,3,0],
    [0,3,2,2,3,0,0,3,2,2,3,0],
    [0,3,0,0,3,1,1,3,0,0,3,0],
    [0,3,1,1,3,3,3,3,1,1,3,0],
    [0,2,3,3,2,0,0,2,3,3,2,0],
    [0,0,0,0,0,0,0,0,0,0,0,0]
     ]
    #map_data = map_data1
    #coin = 34

def set_chara():
    global ch_x,ch_y,ch_d,ch_a
    ch_x = 90
    ch_y = 90
    ch_d = 1
    ch_a = 3

def set_enemyA():
    global ex,ey,ea,ed
    ex = 630
    ey = 450
    ed = 1
    ea = 3

def set_enemyB():
    global bx,b_y,bd,ba
    bx = 630
    b_y = 450
    bd = 0
    ba = 0

def set_fire():
    global gx,gy,gd,ga
    gx = 0
    gy = 0
    gd = 0
    ga = 0

def key_down(e):
    global key, koff
    key = e.keysym
    koff = False

def key_up(e):
    global koff
    koff = True

def check_wall(cx,cy,di,dot):

    chk = False
    if di == 0:
        mx = int((cx-30)/60)
        my = int((cy-30-dot)/60)
        if map_data[my][mx] <= 1: # 左上
            chk = True
        mx = int((cx+29)/60)
        if map_data[my][mx] <= 1: # 右上
            chk = True
    if di == 1:
        mx = int((cx-30)/60)
        my = int((cy+29+dot)/60)
        if map_data[my][mx] <= 1: # 左下
            chk = True
        mx = int((cx+29)/60)
        if map_data[my][mx] <= 1: # 右下
            chk = True
    if di == 2:
        mx = int((cx-30-dot)/60)
        my = int((cy-30)/60)
        if map_data[my][mx] <= 1: # 左上
            chk = True
        my = int((cy+29)/60)
        if map_data[my][mx] <= 1: # 左下
            chk = True
    if di == 3:
        mx = int((cx+29+dot)/60)
        my = int((cy-30)/60)
        if map_data[my][mx] <= 1: # 右上
            chk = True
        my = int((cy+29)/60)
        if map_data[my][mx] <= 1: # 右下
            chk = True
    return chk

#Aパターンの敵
def move_enemy(a):
    global ex,ey,ed,ea,tmr,idx
    global gx,gy
    global tag_enemy,h
    if tag_enemy == False:
        speed = 10
        if ex%60 == 30 and ey%60 == 30:
            ed = random.randint(0, 6)
            if ed >= 4:
                if ch_y < ey:
                    ed = 0
                if ch_y > ey:
                    ed = 1
                if ch_x < ex:
                    ed = 2
                if ch_x > ex:
                    ed = 3
        if ed == 0:
            if check_wall(ex, ey, ed, speed) == False:
                ey = ey - speed
        if ed == 1:
            if check_wall(ex, ey, ed, speed) == False:
                ey = ey + speed
        if ed == 2:
            if check_wall(ex, ey, ed, speed) == False:
                ex = ex - speed
        if ed == 3:
            if check_wall(ex, ey, ed, speed) == False:
                ex = ex + speed
        ea = ed*3 + ANIMATION[tmr%4]
    
        #的にぶつかった当たり判定
        if a == 0:
            if abs(ex-ch_x) <= 40 and abs(ey-ch_y) <= 40:
                idx = 2
                tmr = 0
            elif abs(ex-gx) <= 40 and abs(ey-gy) <= 40:
                if key == "space":
                #idx = 3
            
                    idx = 3
                    tmr = 0
                    h = 1
                
        else:
            if abs(ex - ch_x) <= 40 and abs(ey - ch_y) <= 40:
                idx = 2
                tmr = 0

    elif tag_enemy == True:
        #setstage()
        tag_enemy = False
        move_enemy(0)
            
#Bパターンの敵
def move_enemy_B(b):
    global bx,b_y,bd,ba,tmr,idx
    global tag_enemy2,h
    if tag_enemy2 == False:
        speed = 10
        if bx%60 == 30 and b_y%60 == 30:
            bd = random.randint(0, 6)
            if bd >= 4:
                if ch_y < b_y:
                    bd = 0
                if ch_y > b_y:
                    bd = 1
                if ch_x < bx:
                    bd = 2
                if ch_x > bx:
                    bd = 3
        if bd == 0:
            if check_wall(bx, b_y, bd, speed) == False:
                b_y = b_y - speed
        if bd == 1:
            if check_wall(bx, b_y, bd, speed) == False:
                b_y = b_y + speed
        if bd == 2:
            if check_wall(bx, b_y, bd, speed) == False:
                bx = bx - speed
        if bd == 3: 
            if check_wall(bx, b_y, bd, speed) == False:
                bx = bx + speed
        ba = bd*3 + ANIMATION[tmr%4]
        
        #的にぶつかった当たり判定
        if b == 0:
            if abs(bx-ch_x) <= 40 and abs(b_y-ch_y) <= 40:
                idx = 2
                tmr = 0

            elif abs(bx-gx) <= 40 and abs(b_y-gy) <= 40:
                if key == "space":
                #idx = 3
            
                    idx = 3
                    tmr = 0
                    h = 2
        else:
            if abs(bx-ch_x) <= 40 and abs(b_y - ch_y) <= 40:
                idx = 2
                tmr = 0
    
    elif tag_enemy2 == True:
        tag_enemy2 = False
        move_enemy_B(0)
    
def enemyOnCollision(a):
    global tmr,idx
    if a == 1:
        if abs(90-ch_x) <= 40 and abs(ey-ch_y) <= 40:
            idx = 2
            tmr = 0

def move_ch():
    global ch_x,ch_y,ch_d,ch_a,coin
    
    
    if key == "Up":
        ch_d = 0
        if check_wall(ch_x, ch_y, ch_d,20) == False:
            ch_y = ch_y - 20
    if key == "Down":
        ch_d = 1
        if check_wall(ch_x, ch_y, ch_d,20) == False:
            ch_y = ch_y + 20
    if key == "Left":
        ch_d = 2
        if check_wall(ch_x, ch_y, ch_d,20) == False:
            ch_x = ch_x - 20
    if key == "Right":
        ch_d = 3
        if check_wall(ch_x, ch_y, ch_d,20) == False:
            ch_x = ch_x + 20
            
    ch_a = ch_d * 3 + ANIMATION[tmr%4]
    
    mx = int(ch_x/60)
    my = int(ch_y/60)
    if map_data[my][mx] == 3:
        #pygame.mixer.init()
        #pygame.mixer.music.load('BGM/coin.mp3')
        #pygame.mixer.music.play(1)
        mainGame.score = mainGame.score + 1
        map_data[my][mx] = 2
        coin = coin - 1
        
