from GameEngineParameters import *
import pygame
import cairo
import random

class GameEngine:
  def __init__(self, params: GameEngineParameters) -> None:
    self.parameters = params

  def Start(self):
    pygame.init()

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, self.parameters.window_width, self.parameters.window_height)
    context = cairo.Context(surface)
     
    screen = pygame.display.set_mode((self.parameters.window_height, self.parameters.window_width))
     
    running = True
    
    cells = self.GetRandomGrid()
    while running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
  
      # step function will go here
      self.DrawCellsToContext(cells, context)
        
      buffer = surface.get_data()
      image = pygame.image.frombuffer(buffer, (self.parameters.window_height, self.parameters.window_width), "ARGB")
      screen.blit(image, (0, 0))
      pygame.display.flip()

    pygame.quit()

  def DrawCellsToContext(self, cells: list, context):
    if len(cells) != self.parameters.cell_array_size:
      return
    if len(cells[0]) != self.parameters.cell_array_size:
      return

    square_size = self.parameters.window_width // self.parameters.cell_array_size
    
    for row in range(self.parameters.cell_array_size):
      for col in range(self.parameters.cell_array_size):
        x = col * square_size
        y = row * square_size
        
        context.rectangle(x - 1, y - 1, square_size - 1, square_size - 1)
        is_fish_here = cells[row][col]

        if is_fish_here == True:
          context.set_source_rgb(1, 1, 1)
        else:
          context.set_source_rgb(0, 0, 0)

        context.fill()


  def GetRandomGrid(self):
    final = []
    for i in range(self.parameters.cell_array_size):
      row = []
      for j in range(self.parameters.cell_array_size):
        num = random.randint(0, 1)
        if num == 1:
          row.append(False)
        else:
          row.append(True)
      final.append(row)
    return final