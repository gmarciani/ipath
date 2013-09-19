from common_mc import get_random_nodes, get_couples_mc, get_couples_mc_isolated_test
from time import clock
from model.tree import RelationTree as Tree
from model.priority_queue import DHeap as PriorityQueue
from sets import Set
from utils.map_utils import geo_distance

INFINITE = float("inf")

#Nessun Vincolo di Minimizzazione
def dijkstra_mc_0(graph, num_nodes, max_distance = INFINITE):
    random_nodes = get_random_nodes(graph, num_nodes)
    groups = get_couples_mc(random_nodes, max_distance)
    result = Set()
    for group in groups.iteritems():
        source = group[0]
        dest_nodes = group[1]
        data = _dijkstra_mc_0(graph, source, dest_nodes, max_distance)
        result.union_update(data)          
    return result

def _dijkstra_mc_0(graph, source, dest_nodes, max_distance):
    
    NOT_WALKABLE = clock()    
        
    pathTree = Tree(source._id)
    pathCost = dict.fromkeys(graph._nodes.iterkeys(), INFINITE)    
    pathCost[source._id] = 0.0
            
    Q = PriorityQueue()
    Q.insert(source._id, 0.0)
        
    while not Q.is_empty():
        minNodeId = Q.delete_min().element            
        for arc in graph.get_incident_arcs(minNodeId):
            if arc.status == NOT_WALKABLE: continue 
                                                
            tailNodeCost = pathCost[minNodeId]
            arcCost = arc.info
            headNodeId = arc._head               
            headNodeCost = pathCost[headNodeId]                
       
            if headNodeCost == INFINITE:
                newCost = tailNodeCost + arcCost
                pathCost[headNodeId] = newCost
                Q.insert(headNodeId, newCost)
                pathTree.insert(minNodeId, headNodeId)
                graph.set_arc_status(headNodeId, minNodeId, NOT_WALKABLE)
            elif (tailNodeCost + arcCost) < headNodeCost:
                prevFatherNodeId = pathTree.get_father(headNodeId)
                graph.set_arc_status(headNodeId, prevFatherNodeId, None)
                newCost = tailNodeCost + arcCost
                pathCost[headNodeId] = newCost
                Q.decrease_key(headNodeId, newCost)
                pathTree.make_son(minNodeId, headNodeId)
                graph.set_arc_status(headNodeId, minNodeId, NOT_WALKABLE)
    
    data = Set()
    for dest in dest_nodes:
        couple = (source._id, dest._id)
        try:
            path = pathTree.get_path_to(dest._id)
        except KeyError:
            path = None
        cost = pathCost[dest._id]
        data.add((couple, path, cost))                
    return data

#Vincolo 1 di minimizzazione di |V(G)| e vincolo di minimizzazione di |K|
def dijkstra_mc_1(graph, num_nodes, max_distance = INFINITE):
    random_nodes = get_random_nodes(graph, num_nodes)
    groups = get_couples_mc(random_nodes, max_distance)
    result = Set()
    for group in groups.iteritems():
        source = groups[0]
        dest_nodes = group[1][0]
        data = _dijkstra_mc_1(graph, source, dest_nodes, max_distance)
        result.union_update(data)
    return result

def _dijkstra_mc_1(graph, source, dest_nodes, max_distance):
        
    OUT_OF_RANGE = - source._id - clock()    
    MAX_DISTANT_NODE_ID = _find_max_distant_node_id(source, dest_nodes)
    NOT_WALKABLE = clock()    
        
    pathTree = Tree(source._id)
    pathCost = dict.fromkeys(graph._nodes.iterkeys(), INFINITE)    
    pathCost[source._id] = 0.0
            
    Q = PriorityQueue()
    Q.insert(source._id, 0.0)
        
    while not Q.is_empty():
        minNodeId = Q.delete_min().element         
        for arc in graph.get_incident_arcs(minNodeId):
            if arc.status == NOT_WALKABLE: continue  
                                  
            headNodeId = arc._head 
            headNode = graph.get_node_by_id(headNodeId)        
                
            if headNode.status == OUT_OF_RANGE: continue
            else:                 
                newCost = pathCost[minNodeId] + arc.info              
                if newCost >= pathCost[MAX_DISTANT_NODE_ID]:
                    headNode.status = OUT_OF_RANGE
                    continue
                        
            tailNodeCost = pathCost[minNodeId]
            arcCost = arc.info               
            headNodeCost = pathCost[headNodeId]               
       
            if headNodeCost == INFINITE:
                newCost = tailNodeCost + arcCost
                pathCost[headNodeId] = newCost
                Q.insert(headNodeId, newCost)
                pathTree.insert(minNodeId, headNodeId)
                graph.set_arc_status(headNodeId, minNodeId, NOT_WALKABLE)
            elif (tailNodeCost + arcCost) < headNodeCost:
                prevFatherNodeId = pathTree.get_father(headNodeId)
                graph.set_arc_status(headNodeId, prevFatherNodeId, None)
                newCost = tailNodeCost + arcCost
                pathCost[headNodeId] = newCost
                Q.decrease_key(headNodeId, newCost)
                pathTree.make_son(minNodeId, headNodeId)
                graph.set_arc_status(headNodeId, minNodeId, NOT_WALKABLE)
    
    data = Set()
    for destNode in dest_nodes:
        couple = (source._id, destNode._id)
        try:
            path = pathTree.get_path_to(destNode._id)
        except KeyError:
            path = None
        cost = pathCost[destNode._id]
        data.add((couple, path, cost))                
    return data

#Vincolo 1 e 2 di minimizzazione di |V(G)| e vincolo di minimizzazione di |K|
def dijkstra_mc_2(graph, num_nodes, max_distance = INFINITE):
    random_nodes = get_random_nodes(graph, num_nodes)
    groups = get_couples_mc_isolated_test(random_nodes, max_distance)
    result = Set()
    for group in groups.iteritems():
        source = group[0]
        dest_nodes = group[1][0]
        data = _dijkstra_mc_2(graph, source, dest_nodes, max_distance)
        result.union_update(data)
        for isolated_dest_node in group[1][1]:
            data = ((source._id, isolated_dest_node._id), None, INFINITE)
            result.union_update(data)
    return result

def _dijkstra_mc_2(graph, source, dest_nodes, max_distance):
    
    OUT_OF_RANGE = - source._id - clock()    
    MAX_DISTANT_NODE_ID = _find_max_distant_node_id(source, dest_nodes)
    NOT_WALKABLE = clock()
        
    pathTree = Tree(source._id)
    pathCost = dict.fromkeys(graph._nodes.iterkeys(), INFINITE)    
    pathCost[source._id] = 0.0
            
    Q = PriorityQueue()
    Q.insert(source._id, 0.0)
        
    while not Q.is_empty():
        minNodeId = Q.delete_min().element            
        for arc in graph.get_incident_arcs(minNodeId):
            if arc.status == NOT_WALKABLE: continue
            
            headNodeId = arc._head 
            headNode = graph.get_node_by_id(headNodeId)        
                
            if headNode.status == OUT_OF_RANGE: continue
            else:                
                newCost = pathCost[minNodeId] + arc.info              
                if newCost >= pathCost[MAX_DISTANT_NODE_ID]:
                    headNode.status = OUT_OF_RANGE
                    continue
                        
            tailNodeCost = pathCost[minNodeId]
            arcCost = arc.info               
            headNodeCost = pathCost[headNodeId]                
       
            if headNodeCost == INFINITE:
                newCost = tailNodeCost + arcCost
                pathCost[headNodeId] = newCost
                Q.insert(headNodeId, newCost)
                pathTree.insert(minNodeId, headNodeId)
                graph.set_arc_status(headNodeId, minNodeId, NOT_WALKABLE)
            elif (tailNodeCost + arcCost) < headNodeCost:
                prevFatherNodeId = pathTree.get_father(headNodeId)
                graph.set_arc_status(headNodeId, prevFatherNodeId, None)
                newCost = tailNodeCost + arcCost
                pathCost[headNodeId] = newCost
                Q.decrease_key(headNodeId, newCost)
                pathTree.make_son(minNodeId, headNodeId)
                graph.set_arc_status(headNodeId, minNodeId, NOT_WALKABLE)
    
    data = Set()
    for destNode in dest_nodes:
        couple = (source._id, destNode._id)
        try:
            path = pathTree.get_path_to(destNode._id)
        except KeyError:
            path = None
        cost = pathCost[destNode._id]
        data.add((couple, path, cost))                
    return data

#Vincolo 1,2 e 3 di minimizzazione di |V(G)| e vincolo di minimizzazione di |K|
def dijkstra_mc_3(graph, num_nodes, max_distance = INFINITE):
    random_nodes = get_random_nodes(graph, num_nodes)
    groups = get_couples_mc_isolated_test(random_nodes, max_distance)
    result = Set()
    for group in groups.itervalues():
        source = group[0]
        dest_nodes = group[1][0]
        data = _dijkstra_mc_3(graph, source, dest_nodes, max_distance)
        result.union_update(data)
        for isolated_dest_node in group[1][1]:
            data = ((source._id, isolated_dest_node._id), None, INFINITE)
            result.union_update(data)
    return result

def _dijkstra_mc_3(graph, source, dest_nodes, max_distance):
    
    OUT_OF_RANGE = - source._id - clock()
    NOT_WALKABLE = clock()    
    
    MAX_DISTANT_NODE_ID = _find_max_distant_node_id(source, dest_nodes)
        
    pathTree = Tree(source._id)
    pathCost = dict.fromkeys(graph._nodes.iterkeys(), INFINITE)    
    pathCost[source._id] = 0.0
            
    Q = PriorityQueue()
    Q.insert(source._id, 0.0)
        
    while not Q.is_empty():
        minNodeId = Q.delete_min().element           
        for arc in graph.get_incident_arcs(minNodeId):
            if arc.status == NOT_WALKABLE: continue
            
            headNodeId = arc._head 
            headNode = graph.get_node_by_id(headNodeId)          
                
            if headNode.status == OUT_OF_RANGE: continue
            else:
                newCost = pathCost[minNodeId] + arc.info                              
                if newCost >= pathCost[MAX_DISTANT_NODE_ID] or (all(headNodeId != node._id for node in dest_nodes) and headNode._deg == 1):
                    headNode.status = OUT_OF_RANGE
                    continue
                        
            tailNodeCost = pathCost[minNodeId]
            arcCost = arc.info               
            headNodeCost = pathCost[headNodeId]                
       
            if headNodeCost == INFINITE:
                newCost = tailNodeCost + arcCost
                pathCost[headNodeId] = newCost
                Q.insert(headNodeId, newCost)
                pathTree.insert(minNodeId, headNodeId)
                graph.set_arc_status(headNodeId, minNodeId, NOT_WALKABLE)
            elif (tailNodeCost + arcCost) < headNodeCost:
                prevFatherNodeId = pathTree.get_father(headNodeId)
                graph.set_arc_status(headNodeId, prevFatherNodeId, None)
                newCost = tailNodeCost + arcCost
                pathCost[headNodeId] = newCost
                Q.decrease_key(headNodeId, newCost)
                pathTree.make_son(minNodeId, headNodeId)
                graph.set_arc_status(headNodeId, minNodeId, NOT_WALKABLE)
    
    data = Set()
    for destNode in dest_nodes:
        couple = (source._id, destNode._id)
        try:
            path = pathTree.get_path_to(destNode._id)
        except KeyError:
            path = None
        cost = pathCost[destNode._id]
        data.add((couple, path, cost))                
    return data

def _find_max_distant_node_id(source, dest_nodes):
    node_id = None
    max_distance = 0
    for dest_node in dest_nodes:
        distance = geo_distance(source.element, dest_node.element)
        if distance > max_distance: 
            max_distance = distance
            node_id = dest_node._id
    return node_id    

def __test(func, graph, num_nodes, max_distance):
    from utils.map_utils import isolation, blocking_nodes, average_node_deg, average_arc_weight
    
    print "### TEST ALGORITHM"
    print "### Type: Shortest Path"
    print "### Implementation: {}".format(str(func.__name__)) 
    print "### Num. Random Nodes: {}".format(str(num_nodes))
    print "### Max Distance: {}".format(str(max_distance))
    print "###"
    print "### Nodes: {}".format(str(graph.get_num_nodes()))   
    print "### Arcs: {}".format(str(graph.get_num_arcs()))
    print "### Deg: {} deg/node".format(str(average_node_deg(graph)))
    print "### Weight: {} meters/arc".format(str(average_arc_weight(graph)))
    print "### Blocking: {} %".format(str(blocking_nodes(graph)))
    print "### Isolation: {} %\n".format(str(isolation(graph))) 
    
    print "Computing Result . . ."
    result = func(graph, num_nodes, max_distance)
    
    print "\n*** RESULT ***\n"
    print result
    
    print "\n### END OF TEST ###\n"

if __name__ == "__main__": 
    from test.__init__ import TEST_SOURCE_REAL_ROME as TEST
    from control.parse.c_element_tree import cElementTreeParser
    
    FUNCS = [dijkstra_mc_2]
    source = TEST
    
    print "Source: {}".format(source)
    print "Parsing Graph . . .\n"
    graph = cElementTreeParser().parse_file(source)
    num_nodes = 200
    max_distance = 100
    
    for func in FUNCS:        
        __test(func, graph, num_nodes, max_distance)