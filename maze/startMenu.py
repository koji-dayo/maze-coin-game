'''
スタートメニュー
'''
import tkinter as tk
import tkinter.filedialog as fl
import tkinter.messagebox as mb
from PIL import Image, ImageTk
from tkinter import font
#from mutagen.mp3 import MP3 as mp3
#import pygame
import mainGame


FLOOR = "image/stone_00124.png"
BGM = "BGM/start_menu_bgm.mp3"

class StartGame(tk.Frame):
    
    def __init__(self,master):
        super().__init__(master)
        self.pack()
        
        #pygame.mixer.init()
        #pygame.mixer.music.load(BGM)
        #pygame.mixer.music.play(1)
        #========================
        #ウィンドウ生成(1000x700)
        #title:StartMenu
        #========================
        self.width = 720
        self.height = 540
        master.geometry(str(self.width) + "x" + str(self.height))
        master.title("Game")
        self.createWidgets()
        
    def createWidgets(self):
        #=========================
        #背景:floor.jpg
        #label:menu text
        #button:mainmenu移動
        #=========================
        floor = Image.open(FLOOR)
        self.floor = ImageTk.PhotoImage(floor)
        canvas = tk.Canvas(bg = "black",width = 720,height = 540)
        canvas.place(x=0, y=0)
        canvas.create_image(0,0,image = self.floor,anchor = tk.NW)
        
        font_title = font.Font(family='Helvetica', size=20, weight='bold')
        label = tk.Label(self.master, text="コインを集めろ！！ゴールを目指せ！！", fg="white", bg="black", font=font_title)
        label.place(x = 90,y = 50)
        
        self.btn = tk.Button(self.master,text = u'・ゲームスタート！！',width = 20,height = 3,bg = "green",command = self.newWindow)
        self.btn.place(x = 250,y = 250)
        
    def newWindow(self):
        #pygame.mixer.music.stop() 
        mainGame.maingame(self.master)
        
        



def main():
    root = tk.Tk()
    root.resizable(width=False, height=False) 
    start_game = StartGame(master = root)
    start_game.mainloop()
    

if __name__ == '__main__':
    main()
