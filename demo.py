import networkx as nx
from networkx import DiGraph, from_numpy_matrix, relabel_nodes, set_node_attributes, compose
from numpy import array
from read import readCsv
from matrix import generation
from windows import create
from result import reading
import numpy as np

csv = readCsv()
windows = create(np.copy(csv[0:,3:]))
generations = generation(np.copy(csv[0:,1:3]))

source = 0
sink = len(np.copy(csv[0:,0:1]))-1

# Distance matrix
DISTANCES = generations['distances']
TRAVEL_TIMES = generations['travelTimes']

# # Time windows (key: node, value: lower/upper bound)
TIME_WINDOWS_LOWER = windows['timeWindowsLower']
TIME_WINDOWS_UPPER = windows['timeWindowsUpper']

# # Transform distance matrix into DiGraph
A = array(DISTANCES, dtype=[("cost", float)])
G_d = from_numpy_matrix(A, create_using=DiGraph())

# # Transform time matrix into DiGraph
A = array(TRAVEL_TIMES, dtype=[("time", float)])
G_t = from_numpy_matrix(A, create_using=DiGraph())

# # Merge
G = compose(G_d, G_t)

# # Set time windows
set_node_attributes(G, values=TIME_WINDOWS_LOWER, name="lower")
set_node_attributes(G, values=TIME_WINDOWS_UPPER, name="upper")

G = relabel_nodes(G, {source: "Source", sink: "Sink"})

from vrpy import VehicleRoutingProblem
prob = VehicleRoutingProblem(G, time_windows=True)
prob.solve()

reading(prob.best_routes, DISTANCES, TRAVEL_TIMES, TIME_WINDOWS_LOWER, TIME_WINDOWS_UPPER, sink, source)
