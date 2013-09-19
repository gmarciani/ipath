#Support Data-Structures Import
from sets import Set
#Math Imports
from random import sample
from itertools import combinations
#Map Import
from utils.map_utils import geo_distance

ISOLATED_NODE = 1

def get_random_nodes(graph, num_nodes):
    nodes_set = frozenset(graph._nodes.itervalues())
    random_nodes = sample(nodes_set, num_nodes)
    return random_nodes

def get_couples_sc(nodes_list, max_distance):
    couples = Set()
    for couple in combinations(nodes_list, 2):
        nodeA = couple[0]
        nodeB = couple[1]
        if geo_distance(nodeA.element, nodeB.element) <= max_distance:
            couples.add((nodeA, nodeB))
    return couples

def get_couples_sc_isolated_test(nodes_list, max_distance):
    couples = Set()
    for couple in combinations(nodes_list, 2):
        nodeA = couple[0]
        nodeB = couple[1]
        if geo_distance(nodeA.element, nodeB.element) <= max_distance:
            tag = None
            if nodeA._deg is 0 or nodeB._deg is 0: 
                tag = ISOLATED_NODE
            couples.add((nodeA, nodeB, tag))
    return couples

def __test(source, num_nodes, max_distance):
    from control.parse.c_element_tree import cElementTreeParser as parser
    
    print "Parsing . . ."
    graph = parser().parse_file(source)
    
    nodes_list = get_random_nodes(graph, num_nodes)
    
    couples_sc = get_couples_sc(nodes_list, max_distance)
    
    print "SC Couples: {}".format(str(len(couples_sc)))
    print "Result: {}".format(str(couples_sc))    
    
    couples_sc = get_couples_sc_isolated_test(nodes_list, max_distance)
    
    print "SC Couples Isolated Test: {}".format(str(len(couples_sc)))
    print "Result: {}".format(str(couples_sc))
    
    print "\n### END OF TEST ###\n"    
    
if __name__ == "__main__":
    from test.__init__ import TEST_SOURCE_REAL_ROME as TEST
    
    source = TEST
    num_nodes = 200
    max_distance = 100
    
    __test(source, num_nodes, max_distance)   