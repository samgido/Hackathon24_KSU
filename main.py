from Engine.RenderingEngine import *
from Engine.SimulationEngine import *
from Params.RenderingEngineParameters import *
from Params.SimulationEngineParmaters import *
from Params.FishParameters import *
from Params.SharkParameters import *

rendering_parameters = RenderingEngineParameters(400, 400, 100)

shark_parameters = SharkParameters(1, 1, 2, 1.1, .4, 1)
fish_parameters = FishParameters(1, 1, 10, 4, 2, 1)

simulation_parameters = SimulationEngineParameters(20, 1, 10)
simulation_engine = SimulationEngine(simulation_parameters, rendering_parameters, shark_parameters, fish_parameters)

rendering_engine = RenderingEngine(rendering_parameters, simulation_engine)

rendering_engine.Start()