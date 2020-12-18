import tkinter as tk
from tkinter.constants import ANCHOR
import random
from figur import *

class Board:
    def __init__(self,n,u):
        self.n,self.u,self.board,self.s = n,u,[[0]*n for i in range(n)],[]
        self.window = tk.Tk()
        self.canvas = tk.Canvas(self.window,width=n+n*u,height=n+n*u,bg="#f3f3f3",highlightthickness=0,cursor="hand1")
        self.canvas.pack()
        for i in range(n):
            for j in range(n):
                if (i+j)%2==1:
                    self.canvas.create_rectangle(j+u*j,i+u*i,j+u*(j+1),i+u*(i+1),fill="#272727",outline="#272727")
                    if i<(n/2-1): self.board[i][j] = Figur(False,[i,j])
                    if i>(n/2): self.board[i][j] = Figur(True,[i,j])
        self.draw_board()
    
    def draw_selected(self, j, i):
        #if self.board[i][j]:
        if i < 8 and i >= 0 and j < 8 and j >= 0:
            self.s.append(self.canvas.create_rectangle(j+self.u*j,i+self.u*i ,(j + 1)+self.u*(j+ 1),(i +1)+self.u*(i + 1),fill="#c9cbff",outline="#98acf8"))
            if self.board[i][j]:
                self.s.append(self.canvas.create_oval(j+self.u*j+(self.u*0.05),i+self.u*i+(self.u*0.05),j+self.u*(j+1)-(self.u*0.05),i+self.u*(i+1)-(self.u*0.05),fill="#333D79" if self.board[i][j].get_player1() else "#A13941",outline="#333D79" if self.board[i][j].get_player1() else "#A13941"))


    def draw_board(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j]: self.canvas.create_oval(j+self.u*j+(self.u*0.05),i+self.u*i+(self.u*0.05),j+self.u*(j+1)-(self.u*0.05),i+self.u*(i+1)-(self.u*0.05),fill="#333D79" if self.board[i][j].get_player1() else "#A13941",outline="#333D79" if self.board[i][j].get_player1() else "#A13941")

    def get_n(self):
        return self.n
    
    def get_u(self):
        return self.u
        
    def get_board(self):
        return self.board

    def delete_selected(self):
        for m in self.s:
            self.canvas.delete(m)
            self.s = []

