class Shark:
    def __init__(self, x_location, y_location, size, speed, detection_radius):
        #Pos
        self.location = (x_location, y_location)

        #Size
        self.size = size

        #Speed
        self.speed = speed #float

        #Detection
        self.detectionRadius = detection_radius #Units

        #Hunger
        self.hungerLevel = 0.0
        self.maxHungerLevel = #const
        self.hungerDecay = #neg const

    def Move(self, x_update, y_update): #Setter
        self.location[0] = x_update * self.speed
        self.location[1] = y_update * self.speed

    def UpdateHunger(self, eaten_fish):
        if (eaten_fish):
            self.hungerLevel -= #const
        else:
            self.hungerLevel *= self.hungerDecay
