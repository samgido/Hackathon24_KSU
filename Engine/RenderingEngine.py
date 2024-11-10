from Params.RenderingEngineParameters import *
from Engine.SimulationEngine import *
import pygame
import cairo
import random

class RenderingEngine:
  def __init__(self, params: RenderingEngineParameters, simulation_engine: SimulationEngine) -> None:
    self.windowHeight = params.window_height
    self.windowWidth = params.window_width
    self.cellArraySize = params.cell_array_size
    self.simulationEngine = simulation_engine

  def Start(self):
    pygame.init()

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, self.windowWidth, self.windowHeight)
    context = cairo.Context(surface)
     
    screen = pygame.display.set_mode((self.windowHeight, self.windowWidth))
     
    running = True
    
    i = 0
    while running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
  
      screen.fill((0, 0, 0))
      # Call step function into cells, replace line beneath this
      if i % 10 == 0:
        animals = self.simulationEngine.Progress()
    
      animal_locations = []
      for fish in animals[0]:
        animal_locations.append(fish.location)
      
      animal_locations.append(animals[1])

      self.DrawCellsToContext(animal_locations, context)
        
      i += 1
      buffer = surface.get_data()
      image = pygame.image.frombuffer(buffer, (self.windowHeight, self.windowWidth), "ARGB")
      screen.blit(image, (0, 0))
      pygame.display.flip()

    pygame.quit()

  def DrawCellsToContext(self, cells: list, context):
    square_size = self.windowWidth / self.cellArraySize
    
    for row in range(self.cellArraySize):
      for col in range(self.cellArraySize):
        x = col * square_size
        y = row * square_size
        
        context.rectangle(x - 1, y - 1, square_size - 1, square_size - 1)
        
        is_fish_here = False
        for fish in cells:
          if row == int(fish.x) and col == int(fish.y):
            is_fish_here = True

        if is_fish_here == True:
          context.set_source_rgb(1, 1, 1)
        else:
          context.set_source_rgb(0, 0, 0)

        context.fill()


  def GetRandomGrid(self):
    final = []
    for i in range(self.cellArraySize):
      row = []
      for j in range(self.cellArraySize):
        num = random.randint(0, 1)
        if num == 1:
          row.append(False)
        else:
          row.append(True)
      final.append(row)
    return final