class Fish:
    def __init__(self, x_location, y_location, speed, max_comfort_level, max_breed_level, max_comfort_zone, min_comfort_zone): #speed, size
        #Pos
        self.location = (x_location, y_location)

        #Speed
        self.speed = speed

        #Comfort
        self.comfortLevel = 0.0
        self.maxComfortLevel = max_comfort_level
        self.maxComfortZone = max_comfort_zone #Units
        self.minComfortZone = min_comfort_zone #Units

        #Breeding
        self.breedLevel = 0.0
        self.maxBreedLevel = max_breed_level
        
        #Impliment Later
        #self.speed = 0.0
        #self.size = ?

    def Move(self, x_update, y_update): #Setter
        self.location[0] += x_update * self.speed
        self.location[1] += y_update * self.speed

    def UpdateComfort(self, distance_to_fish, ): #Alg #Needs to consider Shark
        if (distance_to_fish > self.minComfort and distance_to_fish < self.maxComfort): 
            self.comfortLevel += #func
        pass

    def CanBreed(self, ): #Alg
        if (self.breedLevel == self.maxBreed):
            self.breedLevel = 0
            return True
        else:
            self.breedLevel += #func
        pass

