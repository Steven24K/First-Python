import math
class Vector2D():
    def __init__(self, x, y): #Defines the x and y coordinates of the vector
        self.X = x
        self.Y = y
    def distance(self): #Gives the distance from the start position (0,0)
        res = math.sqrt ( self .X * self .X + self .Y * self .Y)
        return math.ceil (res)
    def __str__(self): #Returns the position as a string
        return "(" + str(self.X) + "," + str(self.Y) + ")"
    def negative(self): #returns the oposite values of x and y
        return Vector2D(-self.X, -self.Y)
    def add(self, add_x, add_y): #Moves an amount of stepps on the x and y 
        return Vector2D(self.X + add_x , self.Y + add_y)
    def multiply(self, mult_x, mult_y):
        return Vector2D(self.X * mult_x, self.Y * mult_y)
    def devide(self, dev_x, dev_y):
        return Vector2D(self.X//dev_x, self.Y//dev_y)

class Wall():
    def __init__(self, position):
        self.Position = position 
 
class Game_Start():
    def __init__(self):
        self.Game = True

class Game_end():
    def __init__(self):
        self.Game = False

position = Vector2D(0,0)
game = Game_Start()
size = 20

print("You are the #, the goal is to reach the dollar sign. Good luck!")

while game.Game == True:
    field = ""
    x_stepps = input("Press r + return to move right:  ")
    y_stepps = input("Press d + return to move down:   ")
    
    if x_stepps == "r": 
        position = position.add(1,0)
    if y_stepps == "d":
        position = position.add(0,1)
    if position.X > size:
        position = position.add(-(size + 1),0)
    if position.Y > size:
        position = position.add(0, -(size + 1))

    for y in range(size + 1):
        for x in range(size + 1):
            if x == size and y == size:
                field = field + "$"
            
            if x == position.X and y == position.Y:
               field = field + "#"
            else:
                field = field + "-"
        field = field + "\n"
    print("Current position:" , position , "Distance from start:" , position.distance())
    print(field , "\n\n")
    if position.X == size and position.Y == size:
        print("You have reached the objective!!")
        ask = input("Do you want to play again yes or no? ")
        if ask == "yes":
            game = Game_Start()
            position = Vector2D(0,0)
        else:
            game = Game_end()
            
           
