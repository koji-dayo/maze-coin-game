import sys
import tkinter as tk
import tkinter.filedialog as fl
import tkinter.messagebox as mb
from tkinter import font
import time
import pygame
from mutagen.mp3 import MP3 as mp3
import character
import startMenu

#ステージ
FLOOR = "image/floor.png"
STONE = "image/stone.png"
COIN = "image/coin.png"
WALL = "image/takenoko.png"

#主人公
CH1 = "image/111.png"
CH2 = "image/222.png"
CH3 = "image/333.png"
CH4 = "image/101010.png"
CH5 = "image/111111.png"
CH6 = "image/1212.png"
CH7 = "image/777.png"
CH8 = "image/888.png"
CH9 = "image/999.png"
CH10 = "image/444.png"
CH11 = "image/555.png"
CH12 = "image/666.png"

#敵
E1 = "image/1.png"
E2 = "image/2.png"
E3 = "image/3.png"
E4 = "image/10.png"
E5 = "image/11.png"
E6 = "image/12.png"
E7 = "image/7.png"
E8 = "image/8.png"
E9 = "image/9.png"
E10 = "image/4.png"
E11 = "image/5.png"
E12 = "image/6.png"


score = 0
coin = 0
time = 0
time1 = 0

class mainGame(tk.Frame):
    #メインゲームウィンドウ
    def __init__(self,master):
        super().__init__(master)
        self.pack()
        self.__secmap = [
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
        mdata= character.map_data
        self.map_data = mdata
        self.master.bind("<KeyPress>", character.key_down)
        self.master.bind("<KeyRelease>", character.key_up)
        
        #ステージをリセットする
        character.set_chara()
        character.set_enemyA()
        character.set_enemyB()
        
        self.createWidgets()
        
    def createWidgets(self):
        
        self.canvas = tk.Canvas(width = 720,height = 540)#キャンパスサイズ
        
        '''
        img_bg:ステージ画像
        img_ch:主人公の画像
        img_enemy:敵の画像
        img_title:タイトル画像
        img_gun:武器画像(炎)
        '''
        self.img_bg = [
            tk.PhotoImage(file = STONE),
            tk.PhotoImage(file = STONE),
            tk.PhotoImage(file = FLOOR),
            tk.PhotoImage(file = COIN)
            ]
        
        self.img_ch = [
            tk.PhotoImage(file=CH1),
                      tk.PhotoImage(file=CH2),
                       tk.PhotoImage(file=CH3),
                       tk.PhotoImage(file=CH4),
                       tk.PhotoImage(file=CH5),
                       tk.PhotoImage(file=CH6),
                       tk.PhotoImage(file=CH7),
                       tk.PhotoImage(file=CH8),
                       tk.PhotoImage(file=CH9),
                       tk.PhotoImage(file=CH10),
                       tk.PhotoImage(file=CH11),
                       tk.PhotoImage(file=CH12)
                       ]
        
        self.img_enemy = [
            tk.PhotoImage(file=E1),
            tk.PhotoImage(file=E2),
            tk.PhotoImage(file=E3),
            tk.PhotoImage(file=E4),
            tk.PhotoImage(file=E5),
            tk.PhotoImage(file=E6),
            tk.PhotoImage(file=E7),
            tk.PhotoImage(file=E8),
            tk.PhotoImage(file=E9),
            tk.PhotoImage(file=E10),
            tk.PhotoImage(file=E11),
            tk.PhotoImage(file=E12),
            ]
        
                
        self.img_gun = [
            tk.PhotoImage(file = "image/gun.png"),
            tk.PhotoImage(file = "image/gun.png"),
            tk.PhotoImage(file = "image/gun.png")
            ]
        
        self.canvas.pack()               
        self.main_game()
        

        
    def draw_txt(self,txt, x, y, siz, col): # 文字をウィンドウに表示する
        fnt = ("Times New Roman", siz, "bold")
        self.canvas.create_text(x+2, y+2, text=txt, fill="black", font=fnt, tag="SCREEN")
        self.canvas.create_text(x, y, text=txt, fill=col, font=fnt, tag="SCREEN")
        
    def draw_screen(self): #画像をウィンドウに配置する
        self.canvas.delete("SCREEN")
        for y in range(9):
            for x in range(12):
                self.canvas.create_image(x * 60 + 30,y * 60 + 30,image = self.img_bg[character.map_data[y][x]],tag = "SCREEN") #ステージ
        self.canvas.create_image(character.ch_x, character.ch_y, image=self.img_ch[character.ch_a], tag="SCREEN") #主人公
        if character.tag_enemy == False:
            self.canvas.create_image(character.ex,character.ey,image = self.img_enemy[character.ea],tag = "SCREEN") #敵キャラ
             
        
        if character.key == "space":
            character. move_missible()    
            self.canvas.create_image(character.gx,character.gy,image = self.img_gun[character.ga],tag = "SCREEN")#ビーム

        global time1
        if character.tag_enemy2 == False:
            if time1 > 3:
                self.canvas.create_image(character.bx,character.b_y,image = self.img_enemy[character.ba],tag = "SCREEN")#敵キャラ
            
        self.draw_txt("制限時間 " + str(time1) + "/180",600,20,20,"red")#制限時間
        self.draw_txt("獲得メダル "+str(score) + "枚", 200, 30, 30, "red")
        


    '''
    メインループ
    ゲームスタート画面、ゲームプレイ画面、ゲームクリア画面、ゲームオーバー画面の処理を行う
    '''
    def main_game(self):
        character.tmr = character.tmr + 1        
        self.draw_screen()
        
        
        #タイトル画面
        if character.idx == 0:
            self.canvas.create_image(360,200,tag = "SCREEN")
            if character.tmr % 10 < 5:
                self.draw_txt("Press SPACE!",360,380,30,"yellow")
            if character.key == "space":
                global score
                score = 0
                character.set_chara()
                character.set_enemyA()
                character.set_enemyB()
                character.idx = 1
        
        #ゲームプレイ画面
        if character.idx == 1:
            #制限時間起動
            global time,time1
            time = time + 10
            time1 = int(time/100)            
                            
            character.move_ch()
            character.move_enemy(0)
            
            
            #3秒後に新しい敵の登場
            if time1 > 3:
                character.move_enemy_B(0)
            
            if time1 == 180:#制限時間
                character.idx = 2
            
            #もしメダルをすべて取ると、ゲームクリア画面に移動する
            if character.coin == 0:
                character.idx = 4
                character.tmr = 0
                
        #敵にぶつかったときの当たり判定でありゲームオーバー画面の表示
        if character.idx == 2:
            #pygame.mixer.music.stop()
            self.draw_txt("GAMME OVER",360,270,40,"red")
            if character.tmr == 50:
                character.map_data = self.__secmap
                time = 0
                character.idx = 0
        #炎に敵が当たったときの処理        
        if character.idx == 3:
            if character.h == 1:
                character.tag_enemy = True
                character.set_enemyA()
            elif character.h == 2:
                character.tag_enemy2 = True
                character.set_enemyB()
            character.idx = 1
        
        #メダルすべて回収であり、ゲームクリア画面に移動する       
        if character.idx == 4:
            self.draw_txt("STAGE CLEAR",360,270,40,"pink")
            if character.tmr == 50:
                character.idx = 0
            character.map_data = self.__secmap
            time = 0
            character.coin = 34

            
        if character.koff == True:
            character.key = ""
            character.koff = False
        self.master.after(100, self.main_game)
                    
        
def maingame(master):
    start_game = mainGame(master)


    
