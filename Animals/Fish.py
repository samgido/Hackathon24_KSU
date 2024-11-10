from Params.FishParameters import *
import Position

class Fish:
    def __init__(self, parameters, location: Position):
        #Speed
        self.speed = parameters.speed
        
        self.location: Position = location

        # Comfort
        self.comfortLevel = 1.0
        self.maxComfortLevel = parameters.maxComfortLevel
        self.maxComfortZone = parameters.maxComfortZone #Units
        self.minComfortZone = parameters.minComfortZone #Units

        #Breeding
        self.breedLevel = 0.0
        self.maxBreedLevel = parameters.maxBreedLevel
        self.breedLevelIncrement = parameters.breedLevelIncrement
        
        #Impliment Later
        #self.speed = 0.0
        #self.size = ?

    def UpdateComfort(self, distance_to_shark, distance_to_fish, ): #Alg
        if (distance_to_shark < self.maxComfortZone):
            self.comfortLevel = .2
        elif (distance_to_fish < self.minComfortZone):
            self.comfortLevel = .9
        elif (distance_to_fish > self.maxComfortZone): 
            self.comfortLevel = 1.5
        else:
            self.comfortLevel = 1

        # print("comfort level: " + str(self.comfortLevel))

    def TryBreed(self): #Alg
        if (self.breedLevel == self.maxBreedLevel):
            self.breedLevel = 0
            return True
        else:
            self.breedLevel += self.breedLevelIncrement
        pass

