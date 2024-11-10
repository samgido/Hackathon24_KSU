from Params.SimulationEngineParmaters import *
from Params.RenderingEngineParameters import *
from Params.FishParameters import *
from Params.SharkParameters import *
import random
import math
from Animals.Fish import *
from Animals.Shark import *
from Position import *

class SimulationEngine:
    def __init__(self, simulation_params: SimulationEngineParameters, game_engine_params: RenderingEngineParameters, shark_params: SharkParameters, fish_params: FishParameters) -> None:
        self.intialFishCount = simulation_params.initialFishCount
        self.sharkCount = simulation_params.sharkCount
        self.cellArraySize = game_engine_params.cell_array_size
        self.fishSpawningVariance = simulation_params.fishSpawingVariance
        self.sharkParams = shark_params
        self.fishParams = fish_params

        self.fishes = []
        self.shark = Shark(random.choice([0, self.cellArraySize - 1]), random.randrange(0, self.cellArraySize - 1), self.sharkParams) #Place Shark
        print(self.shark.location.x)
        print(self.shark.location.y)

        self.CreateFish()

    #Initalize Animals
    def CreateFish(self):
        #Random placement alg for fish (center)
        center = self.cellArraySize // 2
        unique_x = random.sample(range(center - self.fishSpawningVariance, center + self.fishSpawningVariance), self.intialFishCount)
        unique_y = random.sample(range(center - self.fishSpawningVariance, center + self.fishSpawningVariance), self.intialFishCount)
    
        for i in range(self.intialFishCount):
            self.fishes.append(Fish(self.fishParams, Position(unique_x[i], unique_y[i])))

    #Progress Sim and Give pos of animals
    def Progress(self):
        #Shark
        if True:
            closest_fish = self.fishes[0].location
            min_dist = Position.distance(self.shark.location, closest_fish)
            for fish in self.fishes:
                distance_from_shark = Position.distance(fish.location, self.shark.location)
                if (distance_from_shark < .3): #Collision check with fish
                    self.fishes.remove(fish)
                    self.shark.UpdateHunger(True)
                    print("Fish ate")
                elif (distance_from_shark < min_dist): #Find closest fish
                    closest_fish = fish.location
            
            self.shark.UpdateHunger(False)

            #Move
            # print("moving shark by: " + str(closest_fish.x * self.shark.hungerLevel))
            
            self.shark.location.x -= (self.shark.location.x - closest_fish.x) * self.shark.hungerLevel * .6
            self.shark.location.y -= (self.shark.location.y - closest_fish.y) * self.shark.hungerLevel * .6

        #Fish
        fish_processed = 0
        radius = 0
        while fish_processed < len(self.fishes) and radius <= self.cellArraySize:
            ring = self.GetCellsAroundShark(radius)
            for current_fish_position in ring:
                is_fish_here = False
                
                for fish in self.fishes:
                    if Position.equal(fish.location, current_fish_position):
                        is_fish_here = True
                        break

                if (is_fish_here):
                    fish_processed += 1

                    #Min dist Fish
                    min_dist = 1000
                    closest_fish = self.fishes[0]
                    for fish in self.fishes:
                        nearest_fish_distance = Position.distance(fish.location, current_fish_position)
                        if (nearest_fish_distance < min_dist and not Position(current_fish_position, fish.location)):
                            min_dist = nearest_fish_distance
                            closest_fish = fish

                    current_fish = self.fishes[0]
                    for fish in self.fishes:
                        if Position.equal(fish.location, current_fish_position):
                            current_fish = fish
                            break
                    
                    distance_from_shark = Position.distance(self.shark.location, current_fish_position)
                    current_fish.UpdateComfort(Position.distance(self.shark.location, current_fish_position), min_dist)
                    
                    move_less = .2

                    if (current_fish.comfortLevel <= .2): #danger
                        # current_fish.location.x -= self.shark.location.x * (1 + current_fish.comfortLevel)
                        # current_fish.location.y -= self.shark.location.y * (1 + current_fish.comfortLevel)

                        x_difference = current_fish.location.x - self.shark.location.x
                        y_difference = current_fish.location.y - self.shark.location.y

                        if x_difference < 0:
                            current_fish.location.x -= 2
                        else:
                            current_fish.location.x += 2

                        if y_difference < 0:
                            current_fish.location.y -= 2
                        else:
                            current_fish.location.y += 2
                    elif (current_fish.comfortLevel < 1): #normal
                        x_difference = current_fish.location.x - closest_fish.location.x
                        y_difference = current_fish.location.y - closest_fish.location.y

                        # current_fish.location.x += (x_difference * (1 - current_fish.comfortLevel)) * move_less
                        # current_fish.location.y += (y_difference * (1 - current_fish.comfortLevel)) * move_less
                        if x_difference < 0:
                            current_fish.location.x -= 1
                        else:
                            current_fish.location.x += 1

                        if y_difference < 0:
                            current_fish.location.y -= 1
                        else:
                            current_fish.location.y += 1
                    elif (current_fish.comfortLevel > 1):
                        x_difference = current_fish.location.x - closest_fish.location.x
                        y_difference = current_fish.location.y - closest_fish.location.y

                        # current_fish.location.x -= (x_difference * (current_fish.comfortLevel - 1)) 
                        # current_fish.location.y -= (y_difference * (current_fish.comfortLevel - 1)) 
                        
                        if x_difference > 0:
                            current_fish.location.x -= 1
                        else:
                            current_fish.location.x += 1

                        if y_difference > 0:
                            current_fish.location.y -= 1
                        else:
                            current_fish.location.y += 1

                    
                    self.Collision(current_fish) #collision
                    
            radius += 1

        return (self.fishes, self.shark.location)

    def GetCellsAroundShark(self, radius):
        searching = []
        x = int(self.shark.location.x)
        y = int(self.shark.location.y)

        if (y - radius) >= 0: 
            for i in range (x - radius, x + radius):
                if i >= 0 and i < self.cellArraySize:
                    searching.append(Position(i, y-radius))

        if (y + radius) < self.cellArraySize-1: 
            for i in range (x - radius, x + radius):
                if i >= 0 and i < self.cellArraySize:
                    searching.append(Position(i, y+radius))

        if (x - radius) >= 0:
            for i in range(y - radius, y + radius):
                if i >= 0 and i < self.cellArraySize:
                    searching.append(Position(x - radius, i))

        if (x + radius) < self.cellArraySize:
            for i in range(y - radius, y + radius + 1):
                if i >= 0 and i < self.cellArraySize:
                    searching.append(Position(x + radius, i))
        
        return searching
    
    def Collision(self, fish):
        move = 5
        if (fish.location.x < 0):
            fish.location.x += move
        if(fish.location.x >= self.cellArraySize):
            fish.location.x -= move
        if(fish.location.y < 0):
            fish.location.y += move
        if(fish.location.y >= self.cellArraySize):
            fish.location.y -= move