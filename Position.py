import math

class Position:
  def __init__(self, x, y) -> None:
    self.x = x
    self.y = y
  
  def distance(p1, p2):
    return math.dist((p1.x, p1.y), (p2.x, p2.y))

  def equal(p1, p2):
    return int(p1.x) == int(p2.x) and int(p1.y) == int(p2.y)