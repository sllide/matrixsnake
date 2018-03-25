class Menu:
    scroller = [
            [0,0,0,0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,1,0,0,1,0,1,1,1,0],
            [0,0,0,0,1,0,0,0,0,1,0,0,1,0,1,0,0,1,0,1,1,1,0,0,1,0,0,0],
            [0,0,0,0,1,1,1,1,0,1,0,0,1,0,1,1,1,1,0,1,1,0,0,0,1,1,0,0],
            [0,0,0,0,0,0,0,1,0,1,0,0,1,0,1,0,0,1,0,1,0,1,0,0,1,0,0,0],
            [0,0,0,0,1,1,1,1,0,1,0,0,1,0,1,0,0,1,0,1,0,0,1,0,1,1,1,0],
            ]
    runtime = 0
    nextState = False

    def input(self, char):
        #play on arrow key press
        if(char == 259):
            self.nextState = "snake"
        elif(char == 258):
            self.nextState = "snake"
        elif(char == 260):
            self.nextState = "snake"
        elif(char == 261):
            self.nextState = "snake"
        #quit on q
        elif(char == 113):
            self.nextState = "quit"
    def step(self):
        #advance scroller
        self.runtime += 1

    def draw(self, driver):
        #draw sexy title scroller
        for y in range(0,len(self.scroller)):
            for x in range(0,8):
                pixel = self.scroller[y][(x+self.runtime)%len(self.scroller[y])]
                intensity = 0
                if(pixel):
                    intensity = x+1
                driver.set(x,y,intensity)
