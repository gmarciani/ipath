#Support Data-Structures Import
from sets import Set
#Math Imports
from random import sample
from itertools import combinations
#Map Import
from utils.map_utils import geo_distance

def get_random_nodes(graph, num_nodes):
    nodes_set = frozenset(graph._nodes.itervalues())
    random_nodes = sample(nodes_set, num_nodes)
    return random_nodes

def get_couples_mc(nodes_list, max_distance):
    groups = dict.fromkeys([node for node in nodes_list], [0, Set()])
    for couple in combinations(nodes_list, 2):
        nodeA = couple[0]
        nodeB = couple[1]
        if geo_distance(nodeA.element, nodeB.element) <= max_distance:
            if groups[nodeA][0] >= groups[nodeB][0]:
                groups[nodeA][1].add(nodeB)
                groups[nodeA][0] += 1
            else:
                groups[nodeB][1].add(nodeB)
                groups[nodeB][0] += 1
    res_grouped = {}
    for group in groups.iteritems():
        if group[1][0] > 0:
            res_grouped[group[0]] = group[1][1]
    return res_grouped

def get_couples_mc_isolated_test(nodes_list, max_distance):
    groups = dict.fromkeys([node for node in nodes_list], [0, Set(), Set()])
    for couple in combinations(nodes_list, 2):
        nodeA = couple[0]
        nodeB = couple[1]
        if geo_distance(nodeA.element, nodeB.element) <= max_distance:
            if groups[nodeA][0] >= groups[nodeB][0]:
                if nodeB._deg > 0:
                    groups[nodeA][1].add(nodeB)
                else:
                    groups[nodeA][2].add(nodeB)
                groups[nodeA][0] += 1
            else:
                if nodeA._deg > 0:
                    groups[nodeB][1].add(nodeA)
                else:
                    groups[nodeB][2].add(nodeA)
                groups[nodeB][0] += 1
    res_grouped = {}
    for group in groups.iteritems():
        if group[1][0] > 0:
            res_grouped[group[0]] = [group[1][1], group[1][2]]
    return res_grouped

def __test(source, num_nodes, max_distance):
    from control.parse.c_element_tree import cElementTreeParser as parser
    
    print "Parsing . . ."
    graph = parser().parse_file(source)
    
    nodes_list = get_random_nodes(graph, num_nodes)
    
    couples_mc = get_couples_mc(nodes_list, max_distance)
    
    print "MC Couples: {}".format(str(len(couples_mc)))
    #print "Result: {}\n".format(str(couples_mc))    
    
    couples_mc = get_couples_mc_isolated_test(nodes_list, max_distance)
    
    print "MC Couples Isolated Test: {}".format(str(len(couples_mc)))
    #print "Result: {}\n".format(str(couples_mc))
    
    print "\n### END OF TEST ###\n"    
    
if __name__ == "__main__":
    from test.__init__ import TEST_SOURCE_REAL_ROME as TEST
    
    source = TEST
    num_nodes = 200
    max_distance = 100
    
    __test(source, num_nodes, max_distance)   
    