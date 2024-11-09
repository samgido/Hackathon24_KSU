from FishParameters import *

class Fish:
    def __init__(self, parameters):
        #Speed
        self.speed = parameters.speed

        # Comfort
        self.comfortLevel = 0.0
        self.maxComfortLevel = parameters.max_comfort_level
        self.maxComfortZone = parameters.max_comfort_zone #Units
        self.minComfortZone = parameters.min_comfort_zone #Units

        #Breeding
        self.breedLevel = 0.0
        self.maxBreedLevel = parameters.max_breed_level
        self.breedLevelIncrement = parameters.breedLevelIncrement
        
        #Impliment Later
        #self.speed = 0.0
        #self.size = ?

    def UpdateComfort(self, distance_to_shark, distance_to_fish, ): #Alg
        if (distance_to_shark < self.maxComfortZone):
            self.comfortLevel *= .2
        elif (distance_to_fish < self.minComfort or distance_to_fish > self.maxComfort): 
            self.comfortLevel *= .9
        else:
            self.comfortLevel = 1

    def TryBreed(self): #Alg
        if (self.breedLevel == self.maxBreed):
            self.breedLevel = 0
            return True
        else:
            self.breedLevel += self.breedLevelIncrement
        pass

