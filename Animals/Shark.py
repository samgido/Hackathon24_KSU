from Params.SharkParameters import *
from Position import *

class Shark:
    def __init__(self, x_location, y_location, parameters):
        #Pos
        self.location = Position(x_location, y_location)

        #Size
        self.size = parameters.size

        #Speed
        self.speed = parameters.speed #float

        #Hunger
        self.hungerLevel = 0.5
        self.maxHungerLevel = 1
        self.hungerGrowth = parameters.hungerGrowth
        self.fishHungerValue = parameters.fishHungerValue

    def UpdateHunger(self, eaten_fish):
        if (eaten_fish):
            self.hungerLevel -= self.fishHungerValue
        else:
            if self.hungerLevel < self.maxHungerLevel:
                self.hungerLevel *= self.hungerGrowth
