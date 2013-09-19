from common_sc import get_random_nodes, get_couples_sc, get_couples_sc_isolated_test
from time import clock
from model.tree import RelationTree as Tree
from model.priority_queue import DHeap as PriorityQueue
from sets import Set

INFINITE = float("inf") 

#Nessun vincolo di minimizzazzione
def dijkstra_sc_0(graph, numNodes, maxDistance = INFINITE):
    randomNodes = get_random_nodes(graph, numNodes)
    couples = get_couples_sc(randomNodes, maxDistance)
    result = Set()
    for couple in couples:     
        rootNode = couple[0]
        destNode = couple[1]
        data = _dijkstra_sc_0(graph, rootNode, destNode, maxDistance)
        result.add(data)
    return result

def _dijkstra_sc_0(graph, rootNode, destNode, maxDistance):
    
    NOT_WALKABLE = clock()
        
    pathTree = Tree(rootNode._id)
    pathCost = dict.fromkeys(graph._nodes.iterkeys(), INFINITE)    
    pathCost[rootNode._id] = 0.0
            
    Q = PriorityQueue()
    Q.insert(rootNode._id, 0.0)
        
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
    
    couple = (rootNode._id, destNode._id)
    try:
        path = pathTree.get_path_to(destNode._id)
    except KeyError:
        path = None
    cost = pathCost[destNode._id]                
    return (couple, path, cost)

#Vincolo 1 di minimizzazione |V(G)|
def dijkstra_sc_1(graph, numNodes, maxDistance = INFINITE):
    randomNodes = get_random_nodes(graph, numNodes)
    couples = get_couples_sc(randomNodes, maxDistance)
    result = Set()
    for couple in couples:     
        rootNode = couple[0]
        destNode = couple[1]
        data = _dijkstra_sc_1(graph, rootNode, destNode, maxDistance)
        result.add(data)
    return result   

def _dijkstra_sc_1(graph, rootNode, destNode, maxDistance):
    
    OUT_OF_RANGE = - rootNode._id - clock()
    NOT_WALKABLE = clock()
        
    pathTree = Tree(rootNode._id)
    pathCost = dict.fromkeys(graph._nodes.iterkeys(), INFINITE)    
    pathCost[rootNode._id] = 0.0
            
    Q = PriorityQueue()
    Q.insert(rootNode._id, 0.0)
        
    while not Q.is_empty():
        minNodeId = Q.delete_min().element         
        for arc in graph.get_incident_arcs(minNodeId):
            if arc.status == NOT_WALKABLE: continue
            
            headNodeId = arc._head 
            headNode = graph.get_node_by_id(headNodeId)       
                
            if headNode.status == OUT_OF_RANGE: continue
            else:
                newCost = pathCost[minNodeId] + arc.info               
                if newCost >= pathCost[destNode._id]:
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
    
    couple = (rootNode._id, destNode._id)
    try:
        path = pathTree.get_path_to(destNode._id)
    except KeyError:
        path = None
    cost = pathCost[destNode._id]                
    return (couple, path, cost)

#Vincoli 1 e 2 di minimizzazione di |V(G)|
def dijkstra_sc_2(graph, numNodes, maxDistance = INFINITE):
    randomNodes = get_random_nodes(graph, numNodes)
    couples = get_couples_sc_isolated_test(randomNodes, maxDistance)
    result = Set()
    for couple in [c for c in couples if c[2] is None]:     
        rootNode = couple[0]
        destNode = couple[1]
        data = _dijkstra_sc_2(graph, rootNode, destNode, maxDistance)
        result.add(data)
    for couple in [c for c in couples if c[2] is not None]:
        rootNode = couple[0]
        destNode = couple[1]
        data = ((rootNode._id, destNode._id), None, INFINITE)
        result.add(data)
    return result   

def _dijkstra_sc_2(graph, rootNode, destNode, maxDistance):
    
    OUT_OF_RANGE = - rootNode._id - clock()
    NOT_WALKABLE = clock()
        
    pathTree = Tree(rootNode._id)
    pathCost = dict.fromkeys(graph._nodes.iterkeys(), INFINITE)    
    pathCost[rootNode._id] = 0.0
            
    Q = PriorityQueue()
    Q.insert(rootNode._id, 0.0)
        
    while not Q.is_empty():
        minNodeId = Q.delete_min().element          
        for arc in graph.get_incident_arcs(minNodeId):
            if arc.status == NOT_WALKABLE: continue
            
            headNodeId = arc._head 
            headNode = graph.get_node_by_id(headNodeId)       
                
            if headNode.status == OUT_OF_RANGE: continue
            else:
                newCost = pathCost[minNodeId] + arc.info               
                if newCost >= pathCost[destNode._id]:
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
    
    couple = (rootNode._id, destNode._id)
    try:
        path = pathTree.get_path_to(destNode._id)
    except KeyError:
        path = None
    cost = pathCost[destNode._id]                
    return (couple, path, cost)

#Vincoli 1,2 e 3 di minimizzazione di |V(G)|
def dijkstra_sc_3(graph, numNodes, maxDistance = INFINITE):
    randomNodes = get_random_nodes(graph, numNodes)
    couples = get_couples_sc_isolated_test(randomNodes, maxDistance)
    result = Set()
    for couple in [c for c in couples if c[2] is None]:     
        rootNode = couple[0]
        destNode = couple[1]
        data = _dijkstra_sc_3(graph, rootNode, destNode, maxDistance)
        result.add(data)
    for couple in [c for c in couples if c[2] is not None]:
        rootNode = couple[0]
        destNode = couple[1]
        data = ((rootNode._id, destNode._id), None, INFINITE)
        result.add(data)
    return result   

def _dijkstra_sc_3(graph, rootNode, destNode, maxDistance):
    
    OUT_OF_RANGE = - rootNode._id - clock()
    NOT_WALKABLE = clock()
        
    pathTree = Tree(rootNode._id)
    pathCost = dict.fromkeys(graph._nodes.iterkeys(), INFINITE)    
    pathCost[rootNode._id] = 0.0
            
    Q = PriorityQueue()
    Q.insert(rootNode._id, 0.0)
        
    while not Q.is_empty():
        minNodeId = Q.delete_min().element           
        for arc in graph.get_incident_arcs(minNodeId):
            if arc.status == NOT_WALKABLE: continue
            headNodeId = arc._head 
            headNode = graph.get_node_by_id(headNodeId)         
                
            if headNode.status == OUT_OF_RANGE: continue
            else:
                newCost = pathCost[minNodeId] + arc.info               
                if (headNodeId != destNode._id and headNode._deg == 1) or newCost >= pathCost[destNode._id]:
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
    
    couple = (rootNode._id, destNode._id)
    try:
        path = pathTree.get_path_to(destNode._id)
    except KeyError:
        path = None
    cost = pathCost[destNode._id]                
    return (couple, path, cost)

def __test(func, graph, numNodes, maxDistance):
    from utils.map_utils import isolation, blocking_nodes, average_node_deg, average_arc_weight
    
    print "### iPATH TEST ALGORITHM"
    print "### Type: Shortest Path"
    print "### Implementation: {}".format(str(func.__name__)) 
    print "### Num. Random Nodes: {}".format(str(numNodes))
    print "### Max Distance: {}".format(str(maxDistance))
    print "###"
    print "### Nodes: {}".format(str(graph.get_num_nodes()))   
    print "### Arcs: {}".format(str(graph.get_num_arcs()))
    print "### Deg: {} deg/node".format(str(average_node_deg(graph)))
    print "### Weight: {} meters/arc".format(str(average_arc_weight(graph)))
    print "### Blocking: {} %".format(str(blocking_nodes(graph)))
    print "### Isolation: {} %\n".format(str(isolation(graph))) 
    
    print "Computing Result . . ."
    result = func(graph, numNodes, maxDistance)
    
    print "\n*** RESULT ***\n"
    print result
    
    print "\n### END OF TEST ###\n"
    
if __name__ == "__main__": 
    from test.__init__ import TEST_SOURCE_REAL_ROME as TEST
    from control.parse.c_element_tree import cElementTreeParser  
    
    FUNCS = [dijkstra_sc_0, 
             dijkstra_sc_1, 
             dijkstra_sc_2, 
             dijkstra_sc_3]
    
    source = TEST
    
    print "Source: {}".format(source)
    print "Parsing Graph . . .\n"
    graph = cElementTreeParser().parse_file(source)
    num_nodes = 200
    max_distance = 100
    
    for func in FUNCS:        
        __test(func, graph, num_nodes, max_distance)