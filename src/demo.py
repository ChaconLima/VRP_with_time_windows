import networkx as nx
from networkx import DiGraph, from_numpy_matrix, relabel_nodes, set_node_attributes, compose
from numpy import array
from src.read import readCsv
from src.matrix import generation
from src.windows import create
from src.result import reading
from const import GREEDY,HEURISTIC_ONLY,TIME_LIMIT,MAX_ITER
import numpy as np
import pulp as pl

def execution():
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

    solver = pl.PULP_CBC_CMD(keepFiles=True)
    prob.solve(greedy=GREEDY,max_iter=MAX_ITER,time_limit=TIME_LIMIT,heuristic_only=HEURISTIC_ONLY)

    reading(prob.best_routes, DISTANCES, TRAVEL_TIMES, TIME_WINDOWS_LOWER, TIME_WINDOWS_UPPER, sink, source)
    return
