from FishParameters import *

class Fish:
    def __init__(self, x_location, y_location, parameters):
        #Pos
        self.location = (x_location, y_location)

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

    # pass in direction of movement, make distance travelled proportional to comfort level
    # direction is a vector originating from the fish
    def Move(self, x_component, y_component): 
        pass

    def UpdateComfort(self, distance_to_fish, distance_to_shark): #Alg
        if (distance_to_fish > self.minComfort and distance_to_fish < self.maxComfort): 
            # self.comfortLevel += #func
            pass

    def TryBreed(self): #Alg
        if (self.breedLevel == self.maxBreed):
            self.breedLevel = 0
            return True
        else:
            self.breedLevel += self.breedLevelIncrement
        pass

