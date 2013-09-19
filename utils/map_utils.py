#Math Imports
from math import radians, sin, cos, asin, sqrt
from utils.math_utils import average
#Couples SC/MC Imports
#from control.shortestpath.common import *

def isolation(graph):
    """
    
    isolation(graph) -> percentage_isolation
    """
    num_nodes = graph.get_num_nodes()
    isolated = 0
    for node in graph.get_nodes():
        if node._deg == 0:
            isolated += 1
    return float(isolated  * float(100) / num_nodes)

def blocking_nodes(graph):
    """
    
    blocking_nodes(graph) -> percentage_blocking_nodes
    """
    num_nodes = graph.get_num_nodes()
    blocking = 0
    for node in graph.get_nodes():
        if node._deg == 1:
            blocking += 1
    return float(blocking * float(100) / num_nodes)

def average_node_deg(graph):
    """
    
    average_node_deg(graph) -> average_node_deg
    """
    degs = []
    for node in graph.get_nodes(): degs.append(node._deg)      
    return average(degs)
    
def average_arc_weight(graph):
    """
    
    average_arc_weight(graph) -> average_arc_weight
    """
    weights = []    
    arcs = graph.get_arcs()
    for arc in arcs: weights.append(arc.info)
    return average(weights)

AVERAGE_BOUND = 100
def average_couples_sc(graph, num_nodes, max_distance, average_bound = AVERAGE_BOUND):
    """
    
    average_couples_sc(graph, num_nodes, max_distance, average_bound = AVERAGE_BOUND) -> average_num_of_couples
    """
    num_couples = []
    for r in range(average_bound):
        nodes_list = get_random_nodes(graph, num_nodes)
        couples = get_couples_sc(nodes_list, max_distance)
        num_couples.append(len(couples))
    return average(num_couples)

def average_couples_mc(graph, num_nodes, max_distance, average_bound = AVERAGE_BOUND):
    """
    
    average_couples_mc(graph, num_nodes, max_distance, average_bound = AVERAGE_BOUND) -> average_couples_mc
    """
    num_groups = []
    for r in range(average_bound):
        nodes_list = get_random_nodes(graph, num_nodes)
        couples = get_couples_mc(nodes_list, max_distance)
        num_groups.append(len(couples))
    return average(num_groups)
    
def geo_distance(coordA, coordB):
    """
    
    geo_distance(coordA, coordB) -> meters
    """
    latA = coordA[0]
    lonA = coordA[1]
    latB = coordB[0]
    lonB = coordB[1]    
    return __haversine(lonA, latA, lonB, latB)

def __haversine(lonA, latA, lonB, latB):
    """
    
    __haversine(lonA, latA, lonB, latB) -> meters
    """
    lonA, latA, lonB, latB = map(radians, [lonA, latA, lonB, latB])
    dlon = lonB - lonA 
    dlat = latB - latA 
    a = sin(dlat / 2) ** 2 + cos(latA) * cos(latB) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a)) 
    kilometers = 6367 * c
    return kilometers * 1000 

def __test(source):
    """
    Map Utilities Test.
    
    __test(source) -> None
    
    @type source: string
    @param source: absolute OSM Map's directory.
    """
    
    #Parser Import
    from control.parse.c_element_tree import cElementTreeParser as parser
    #Math Import
    import random
    
    graph = parser().parse_file(source)
    
    num_nodes = 200
    max_distance = 100
    average_bound = 100
    coord_A = random.choice(graph.get_nodes()).element
    coord_B = random.choice(graph.get_nodes()).element
    
    print "### iPATH TEST MAP UTILS"
    print "### Utility: Graph Analysis"
    print "### Functions: isolation, blocking_nodes, average_node_deg, average_arc_weight, average_couples_sc, average_couples_mc, geo_distance"
    print "###"
    print "### Source: {}".format(str(source))
    print "### Average Bound: {}".format(str(average_bound))
    print "###"
    print "### Isolation: {} %".format(str(isolation(graph)))
    print "### Blocking Nodes: {} %".format(str(blocking_nodes(graph)))
    print "### Node Deg: {} arcs/node".format(str(average_node_deg(graph)))
    print "### Arc Weight: {} meters/arc".format(str(average_arc_weight(graph)))
    print "### Couples SC(Nodes: {}, Max Distance: {}): {} couples".format(str(num_nodes), str(max_distance), str(average_couples_sc(graph, num_nodes, max_distance, average_bound)))
    print "### Groups MC (Nodes: {}, Max Distance: {}): {} groups".format(str(num_nodes), str(max_distance), str(average_couples_mc(graph, num_nodes, max_distance, average_bound)))
    print "### Geo Distance ({}, {}): {} meters".format(str(coord_A), str(coord_B), str(geo_distance(coord_A, coord_B)))   
    
    print "\n### END OF TEST ###\n"
    
if __name__ == "__main__":
    #Test Import
    from test.__init__ import TEST_SOURCE_REAL_PARIOLI
    __test(TEST_SOURCE_REAL_PARIOLI)