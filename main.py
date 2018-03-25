#!/usr/bin/env python
import curses
from snake import Snake
from menu import Menu
from gameover import Gameover
from driver import Driver
from time import time

class Game:

    FPS = 5
    
    def __init__(self, scr):
        scr.nodelay(1)
        self.driver = Driver()
        self.machine = Menu()
        self.menu = True
        self.scr = scr
        self.menu = True
        self.next = time()
        
    def loop(self):
        try:
            while self.machine:
                char = self.scr.getch()
                if(char == 111): # <o> rotate screen
                    self.driver.rotate()
                self.driver.clear()
                self.step(char)
                self.driver.write()

        except KeyboardInterrupt:
            self.clean()
        self.clean()

    def step(self, char):
        self.machine.input(char)
        if(self.next<time()):
            self.machine.step()
            self.next = time() + (1.0/self.FPS)
        self.machine.draw(self.driver)
        if(self.machine.nextState):
            state = self.machine.nextState
            if(state == "snake"):
                self.machine = Snake()
            elif(state == "gameover"):
                self.machine = Gameover()
            elif(state == "menu"):
                self.machine = Menu()
            elif(state == "quit"):
                self.machine = False
        
    def clean(self):
        self.driver.clean()

def main(scr):
    game = Game(scr)
    game.loop()

if __name__ == '__main__': 
    curses.wrapper(main)
