from SharkParameters import *

class Shark:
    def __init__(self, x_location, y_location, parameters):
        #Pos
        self.location = (x_location, y_location)

        #Size
        self.size = parameters.size

        #Speed
        self.speed = parameters.speed #float

        #Detection
        self.detectionRadius = parameters.detection_radius #Units

        #Hunger
        self.hungerLevel = 0.0
        self.maxHungerLevel = parameters.maxHungerLevel
        self.hungerDecay = parameters.hungerDecayRate
        self.fishHungerValue = parameters.fishHungerValue

    def Move(self, x_update, y_update): #Setter
        self.location[0] = x_update * self.speed
        self.location[1] = y_update * self.speed

    def UpdateHunger(self, eaten_fish):
        if (eaten_fish):
            self.hungerLevel -= self.fishHungerValue
        else:
            self.hungerLevel *= self.hungerDecay
