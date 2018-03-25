import random

class Snake:
    blockInput = False
    nextState = False
    
    #snake array
    snake = [[0,0],[0,0],[0,0]]
    #velocity
    vX = 1
    vY = 0

    #food position
    foodX = 0
    foodY = 0

    def __init__(self):
        random.seed()
        self.setFood()

    #randomly spawn food, keep trying until a free spot is found
    #will freeze if there is no free spot lol
    def setFood(self):
        done = False
        while not done:
            self.foodX = random.randrange(7)
            self.foodY = random.randrange(7)
            if(self.isFree(self.foodX,self.foodY)):
                    done = True


    def input(self, char):
        #on q key press return to menu
        if(char == 113):
            self.nextState = "menu"

        #only allow one keypress per frame
        if(self.blockInput):
            return

        if(char == 259): #up
            if(self.vY == 0):
                self.vY = -1
                self.vX = 0
                self.blockInput = True
        elif(char == 258): #down
            if(self.vY == 0):
                self.vY = 1
                self.vX = 0
                self.blockInput = True
        elif(char == 260): #left
            if(self.vX == 0):
                self.vY = 0
                self.vX = -1
                self.blockInput = True
        elif(char == 261): #right
            if(self.vX == 0):
                self.vY = 0
                self.vX = 1
                self.blockInput = True

    def step(self):
        #get head and add velocity
        head = self.snake[len(self.snake)-1]
        newX = head[0] + self.vX
        newY = head[1] + self.vY
        
        #check what the next position will be
        if(self.isFood(newX, newY)):
            #append without popping bodypart to grow snake
            self.snake.append([newX,newY])
            self.setFood()
        elif(self.isFree(newX, newY)):
            #pop and append to move snake
            self.snake = self.snake[1:]
            self.snake.append([newX,newY])
        else:
            #not food and not free, you dead :(
            self.nextState = "gameover"

        self.blockInput = False

    def draw(self,driver):
        #draw snake
        for part in self.snake:
            driver.set(part[0],part[1],9)
        #draw food
        driver.set(self.foodX, self.foodY, 1)

    #is position food?
    def isFood(self,x,y):
        return (x == self.foodX and y == self.foodY)

    #is position free?
    def isFree(self,x,y):
        if(x<0 or x>7 or y<0 or y>7):
            #nope, its a wall
            return False
        for part in self.snake:
            if(x==part[0] and y==part[1]):
                #nope, its snake itself
                return False
        return True
