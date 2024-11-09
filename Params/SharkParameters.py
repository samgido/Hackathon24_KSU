class SharkParameters:
  def __init__(self, size, speed, max_hunger_level, hunger_growth, fish_hunger_value, hunger_soft_cap_ratio):
    self.size = size
    self.speed = speed
    self.maxHungerLevel = max_hunger_level
    self.hungerGrowth = hunger_growth
    self.fishHungerValue = fish_hunger_value
    self.hungerSoftCap = hunger_soft_cap_ratio * max_hunger_level