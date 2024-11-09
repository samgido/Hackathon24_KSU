class FishParameters:
  def __init__(self, speed, max_comfort_level, max_breed_level, max_comfort_zone, min_comfort_zone, breed_level_increment):
    self.speed = speed

    self.maxComfortLevel = max_comfort_level
    self.maxComfortZone = max_comfort_zone #Units
    self.minComfortZone = min_comfort_zone #Units

    self.maxBreedLevel = max_breed_level
    
    self.breedLevelIncrement = breed_level_increment