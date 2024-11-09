from SimulationEngineParmaters import *
from RenderingEngineParameters import *
from FishParameters import *
from SharkParameters import *
import random
import math
import Fish
import Shark

class SimulationEngine:
    def __init__(self, simulation_params: SimulationEngineParameters, game_engine_params: RenderingEngineParameters, shark_params: SharkParameters, fish_params: FishParameters) -> None:
        self.intialFishCount = simulation_params.initialFishCount
        self.sharkCount = simulation_params.sharkCount
        self.cellArraySize = game_engine_params.cell_array_size
        self.fishSpawningVariance = simulation_params.fishSpawingVariance
        self.sharkParams = shark_params
        self.fishParams = fish_params

        self.fishes = {}
        self.shark = Shark(random.choice(0, self.cellArraySize - 1), random(0, self.cellArraySize - 1), self.sharkParams) #Place Shark

    #Initalize Animals
    def CreateAnimals(self):
        #Random placement alg for fish (center)
        center = self.cellArraySize // 2
        unique_x = random.sample(range(center - self.fishSpawningVariance, center + self.fishSpawningVariance), self.intialFishCount)
        unique_y = random.sample(range(center - self.fishSpawningVariance, center + self.fishSpawningVariance), self.intialFishCount)
    
        for i in range(self.intialFishCount):
            self.fishes[(unique_x[i], unique_y[i])] = Fish(self.fishParams)

    #Progress Sim and Give pos of animals
    def Progress(self):
        
        #Shark
        min_dist = 1000
        closest_fish = (0, 0)
        for fish in self.fishes.keys:
            if (math.dist(fish, self.shark.location) < .5): #Collision check with fish
                self.fishes.pop(fish)
                self.shark.UpdateHunger(True)
            elif (math.dist(fish, self.shark.location) < min_dist): #Find closest fish
                closest_fish = fish
        
        self.shark.UpdateHunger(False)

        #Move
        self.shark.location[0] += closest_fish[0] * self.shark.hungerLevel
        self.shark.location[1] += closest_fish[1] * self.shark.hungerLevel
        
        #Fish
        fish_processed = 0
        radius = 0
        while fish_processed < len(self.fishes.keys) and radius <= self.cellArraySize:
            for cell in self.GetCellsAroundShark(radius):
                if (self.fishes.keys.Contains(cell)):
                    fish_processed += 1

                    #Min dist Fish
                    min_dist = 1000
                    closest_fish = (0, 0)
                    for fish in self.fishes.keys:
                        if (math.dist(cell, fish) < min_dist):
                            min_dist = math.dist(cell, fish)
                            closest_fish = fish
                    
                    self.fishes[cell].UpdateComfort(math.dist(cell, self.shark.location), min_dist)
                    
                    if (self.fishes[cell].comfortLevel < .2): #danger
                        cell[0] -= self.shark.location[0] * (1 + self.fishes[cell].comfortLevel)
                        cell[1] -= self.shark.location[1] * (1 + self.fishes[cell].comfortLevel)      
                    elif(self.fishes[cell].comfortLevel < 1): #normal
                        cell[0] -= closest_fish[0] * (1 - self.fishes[cell].comfortLevel)
                        cell[1] -= closest_fish[1] * (1 - self.fishes[cell].comfortLevel)
                    
                    self.Collision(cell) #collision
                    
            radius += 1

        return self.fishes.keys

    def GetCellsAroundShark(self, radius):
        searching = []
        x = self.shark.location[0]
        y = self.shark.location[1]

        if (y - radius) >= 0: 
            for i in range (x - radius, x + radius):
                if i >= 0 and i < self.parameters.cell_array_size:
                    searching.append((i, y-radius))

        if (y + radius) < self.parameters.cell_array_size-1: 
            for i in range (x - radius, x + radius):
                if i >= 0 and i < self.parameters.cell_array_size:
                    searching.append((i, y+radius))

        if (x - radius) >= 0:
            for i in range(y - radius, y + radius):
                if i >= 0 and i < self.parameters.cell_array_size:
                    searching.append((x - radius, i))

        if (x + radius) < self.parameters.cell_array_size:
            for i in range(y - radius, y + radius + 1):
                if i >= 0 and i < self.parameters.cell_array_size:
                    searching.append((x + radius, i))
        
        return searching
    
    def Collision(self, xy_tupe):
        if (xy_tupe[0] < 0):
            xy_tupe[0] += 1
        elif(xy_tupe[0] >= self.cellArraySize):
            xy_tupe[0] -= 1
        elif(xy_tupe[1] < 0):
            xy_tupe += 1
        elif(xy_tupe[1] >= self.cellArraySize):
            xy_tupe[1] -= 1