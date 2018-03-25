class Gameover:

    #smiley art
    smiley = [0,0,9,0,0,9,0,0,
              0,0,9,0,0,9,0,0,
              0,0,9,0,0,9,0,0,
              0,0,0,0,0,0,0,0,
              0,0,9,9,9,9,0,0,
              0,9,0,0,0,0,9,0,
              9,0,0,0,0,0,0,9]
    nextState = False

    def input(self, char):
        #on arrow key press return to menu
        if(char == 259):
            self.nextState = "menu"
        elif(char == 258):
            self.nextState = "menu"
        elif(char == 260):
            self.nextState = "menu"
        elif(char == 261):
            self.nextState = "menu"
        #on q key press exit game
        elif(char == 113):
            self.nextState = "quit"
    def step(self):
        return

    def draw(self, driver):
        #load smiley into screen driver
        driver.setScreen(self.smiley)
