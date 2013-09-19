from model.base.basegraph import basegraph
from model.linkedlist import DoubleLinkedList as LinkedList
from model.queue import QueueLinkedList as Queue
from model.stack import StackLinkedList as Stack    
from sets import Set

class GraphIncidenceList(basegraph):
    
    class Node:
    
        def __init__(self, node_id, element, status = None):
            self._id = node_id
            self._deg = 0
            self.element = element
            self.status = status          
        
        def __eq__(self, other):
            return self.element == other.element
        
        def __cmp__(self, other):
            if self.element > other.element: return 1
            elif self.element < other.element: return -1
            else: return 0
        
        def __hash__(self):
            return hash(self._id)   
        
        def __repr__(self):
            return "*(id: {}, element: {}, status: {})".format(str(self._id), str(self.element), str(self.status))
        
        def __str__(self):
            return self.__repr__()     
        
    class Arc:
    
        def __init__(self, tail, head, info = None, status = None):        
            self._tail = tail
            self._head = head
            self.info = info
            self.status = status        
        
        def __eq__(self, other):
            return self._tail == other._tail and self._head == other._head
        
        def __repr__(self):
            return "^(tail: {}, head: {}, info: {}, status: {})".format(str(self._tail), str(self._head), str(self.info), str(self.status))
        
        def __str__(self):
            return self.__repr__()
    
    def __init__(self):
        self._nodes = {}
        self._inc = {}
        self._next_id = 0
        
    def add_node(self, element, node_id = None):
        """
        Adds a new node in graph, with the specified element.
        
        add_node(element) -> None
        
        @type element: object
        @param element: element to be assigned to the new node.    
        """
        if node_id is None:
            new_node_id = self._next_id
            self._next_id += 1
        else:
            new_node_id = node_id
            self._next_id = node_id + 1
            
        new_node = GraphIncidenceList.Node(new_node_id, element)
        self._nodes[new_node._id] = new_node
        self._inc[new_node._id] = LinkedList()            
    
    def remove_node(self, node_id): 
        """
        Removes from graph the node with the specified id.
        
        remove_node(node_id) -> None
        
        @type node_id: integer
        @param node_id: id of the node to be removed from graph.
        """
        try:       
            del self._nodes[node_id] 
            del self._inc[node_id]
        except KeyError:
            return        
        for arcs_list in self._inc.values():
            record = arcs_list.get_first_record()
            while record is not None:
                arc = record.element
                if arc._head is node_id: arcs_list.delete_record(record)
                record = record._next       
    
    def add_arc(self, nodeA_id, nodeB_id, info = None):
        """
        Adds a new undirected arc in graph, between node_A and node_B with the specified id.
        
        add_arc(nodeA_id, nodeB_id, info) -> None
        
        @type nodeA_id: integer
        @param nodeA_id: id of tail node.
        @type nodeB_id: integer
        @param nodeB_id: id of head node.
        @type info: object
        @param info: element to be added as info to the new arc.    
        """
        try:
            new_arc_AB = GraphIncidenceList.Arc(nodeA_id, nodeB_id, info)
            new_arc_BA = GraphIncidenceList.Arc(nodeB_id, nodeA_id, info)
            self._inc[nodeA_id].add_as_last(new_arc_AB)
            self._inc[nodeB_id].add_as_last(new_arc_BA)
            self._nodes[nodeA_id]._deg += 1
            self._nodes[nodeB_id]._deg += 1  
        except KeyError:
            return 
    
    def remove_arc(self, nodeA_id, nodeB_id):
        """
        Removed from graph the undirected arc between nodeA and nodeB.
        
        remove_arc(nodeA_id, nodeB_id) -> None
        
        @type nodeA_id: integer
        @param nodeA_id: id of tail node.
        @type nodeB_id: integer
        @param nodeB_id: id of head node.    
        """
        try:
            arcs_list_A = self._inc[nodeA_id]
            record = arcs_list_A.get_first_record()
            while record is not None:
                arc = record.element
                if arc._head is nodeB_id:
                    self._inc[nodeA_id].delete_record(record)
                    self._nodes[nodeA_id]._deg -= 1
                    break
                record = record._next
            arcs_list_B = self._inc[nodeB_id]
            record = arcs_list_B.get_first_record()
            while record is not None:
                arc = record.element
                if arc._head is nodeA_id:
                    self._inc[nodeB_id].delete_record(record)
                    self._nodes[nodeB_id]._deg -= 1
                    break
                record = record._next
        except KeyError:
            return
        
    def set_arc_status(self, nodeA_id, nodeB_id, status):
        """
        Sets the status of the directed arc between nodeA and nodeB.
        
        set_arc_status(nodeA_id, nodeB_id, status) -> None
        
        @type nodeA_id: integer
        @param nodeA_id: id of tail node.
        @type nodeB_id: integer
        @param nodeB_id: id of head node.
        @type status: object
        @param status: element to be added as status info to the specified arc.    
        """ 
        try:
            arcs_list = self._inc[nodeA_id]
            record = arcs_list.get_first_record()
            while record is not None:
                arc = record.element
                if arc._head is nodeB_id: 
                    arc.status = status 
                    break
                record = record._next 
        except KeyError:
            return   
        
    def get_nodes(self):
        """
        Returns all nodes in graph        
        get_nodes() -> nodes_list
        
        @rtype: list
        @return: list of nodes in graph.    
        """
        return [node for node in self._nodes.itervalues()]
    
    def get_arcs(self):
        """
        Returns all undirected arcs in graph.
        
        get_arcs() -> arcs_list
        
        @rtype: list
        @return: list of undirected arcs in graph.    
        """
        arcs = []
        for arcs_list in self._inc.values():
            record = arcs_list.get_first_record()
            while record is not None:
                arc = record.element
                arcs.append(arc)
                record = record._next
        return arcs
        
    def get_num_nodes(self):
        """
        Returns the number of nodes in graph.
        
        get_num_nodes() -> number_of_nodes
        
        @rtype: integer
        @return: number of nodes in graph.    
        """
        return len(self._nodes)
    
    def get_num_arcs(self):
        """
        Returns the number of undirected arcs in graph.
        
        get_num_arcs() -> number_of_arcs
        
        @rtype: integer
        @return: number of undirected arcs in graph.    
        """
        num_arcs = 0
        for node in self._nodes.values(): num_arcs += node._deg
        return (num_arcs / 2) + 1
    
    def is_node_in_graph(self, node_id):
        return True if node_id in self._nodes else False   
    
    def get_node_by_id(self, node_id):
        """
        Returns node in graph by id.
        
        get_node_by_id(node_id) -> node
        
        @type node_id: integer
        @param node_id: id of the requested node in graph. 
        
        @rtype: node
        @return: node corresponding to the given id.
        """
        try:
            return self._nodes[node_id]
        except KeyError:
            return None
    
    def get_incident_arcs(self, node_id):
        """
        Returns all incident arcs to the specified node.
        
        get_incident_arcs(node_id) -> list/set
        
        @type node_id: integer
        @param node_id: id of node whos incident arcs have been requested.  
        
        @rtype: list/set
        @return: all arcs that are incident to the node whose id has been specified.  
        """
        try:
            arcs = []
            arc_list = self._inc[node_id]
            record = arc_list.get_first_record()
            while record is not None:
                arc = record.element
                arcs.append(arc)
                record = record._next
            return arcs
        except KeyError:
            return []
    
    def are_adjacent(self, nodeA_id, nodeB_id):
        """
        Returns True if nodeA and nodeB are adjacent, otherwise returns False.
        
        are_adjacent(nodeA_id, nodeB_id) -> True/False
        
        @type nodeA_id: integer
        @param nodeA_id: first node's id.
        @type nodeB_id: integer
        @param nodeB_id: second node's id.
        
        @rtype: boolean
        @return: True if nodeA and nodeB are adjacent, otherwise False.    
        """
        try:        
            record = self._inc[nodeA_id].get_first_record()
            while record is not None:
                arc = record.element
                if arc._head is nodeB_id: return True
                record = record._next
            return False
        except KeyError:
            return False        
        
    def dfs(self, root_node_id):
        """
        Returns the LIFO path-as-list from graph's root to all other nodes in graph.
        
        dfs(root_node_id) -> path
        
        @type root_node_id: integer
        @param root_node_id: graph's root's id.
        
        @rtype: list
        @return: LIFO path from graph's root to all other nodes in graph.
        """
        try: 
            status = dict.fromkeys(self._nodes.iterkeys(), 0)
            status[root_node_id] = 1            
            L = []        
            s = Stack()
            s.push(root_node_id)            
            while not s.is_empty():
                curr_node_id = s.pop()
                status[curr_node_id] = -1
                L.append(self._nodes[curr_node_id])
                arcs_list = self._inc[curr_node_id]
                record = arcs_list.get_first_record()            
                while record is not None:
                    arc = record.element
                    if status[arc._head] is 0:
                        status[arc._head] = 1
                        s.push(arc._head)
                    record = record._next
            return L
        except KeyError:
            return []  

    def bfs(self, root_node_id):
        """
        Returns the FIFO path-as-list from graph's root to all other nodes in graph.
        
        bfs(root_node_id) -> path
        
        @type root_node_id: integer
        @param root_node_id: graph's root's id.
        
        @rtype: list
        @return: FIFO path from graph's root to all other nodes in graph.
        """
        try:       
            status = dict.fromkeys(self._nodes.iterkeys(), 0)
            status[root_node_id] = 1                   
            L = []
            q = Queue()
            q.enqueue(root_node_id)        
            while not q.is_empty():
                curr_node_id = q.dequeue()
                status[curr_node_id] = -1
                L.append(self._nodes[curr_node_id])
                arcs_list = self._inc[curr_node_id]
                record = arcs_list.get_first_record()
                while record is not None:
                    arc = record.element
                    if status[arc._head] is 0:
                        status[arc._head] = 1
                        q.enqueue(arc._head)
                    record = record._next        
            return L
        except KeyError:
            return []          
    
    def __repr__(self):
        s = "{"        
        for node in self._nodes.itervalues():
            arcs_list = []
            record = self._inc[node._id].get_first_record()
            while record is not None:
                arc = record.element
                arcs_list.append(arc)
                record = record._next
            s += "{} : {}\n".format(str(node), str(arcs_list))
        s += "}"
        return s
    
    def __str__(self):
        return self.__repr__()
    
class GraphIncidenceSet(basegraph):
    
    class Node:
    
        def __init__(self, node_id, element, status = None):
            self._id = node_id
            self._deg = 0
            self.element = element
            self.status = status          
        
        def __eq__(self, other):
            return self.element == other.element
        
        def __cmp__(self, other):
            if self.element > other.element: return 1
            elif self.element < other.element: return -1
            else: return 0
        
        def __hash__(self):
            return hash(self._id)   
        
        def __repr__(self):
            return "*(id: {}, element: {}, status: {})".format(str(self._id), str(self.element), str(self.status))
        
        def __str__(self):
            return self.__repr__()     
        
    class Arc:
    
        def __init__(self, tail, head, info = None, status = None):        
            self._tail = tail
            self._head = head
            self.info = info
            self.status = status        
        
        def __eq__(self, other):
            return (self._tail == other._tail and self._head == other._head) or (self._tail == other._head and self._head == other._tail)
        
        def __hash__(self):
            return hash(self._tail + self._head)
        
        def __repr__(self):
            return "^(tail: {}, head: {}, info: {}, status: {})".format(str(self._tail), str(self._head), str(self.info), str(self.status))
        
        def __str__(self):
            return self.__repr__()
    
    def __init__(self):
        self._nodes = {}
        self._inc = {}
        self._next_id = 0
        
    def add_node(self, element, node_id = None):
        """
        Adds a new node in graph, with the specified element.
        
        add_node(element) -> None
        
        @type element: object
        @param element: element to be assigned to the new node.    
        """
        if node_id is None:
            new_node_id = self._next_id
            self._next_id += 1
        else:
            new_node_id = node_id
            self._next_id = node_id + 1
            
        new_node = GraphIncidenceList.Node(new_node_id, element)
        self._nodes[new_node._id] = new_node
        self._inc[new_node._id] = Set()            
    
    def remove_node(self, node_id):
        """
        Removes from graph the node with the specified id.
        
        remove_node(node_id) -> None
        
        @type node_id: integer
        @param node_id: id of the node to be removed from graph.
        """
        try: 
            del self._nodes[node_id] 
            del self._inc[node_id] 
        except KeyError:
            return          
        for arcs_set in self._inc.values():
            arcs_to_remove = Set()
            for arc in arcs_set:
                if arc._head is node_id: arcs_to_remove.add(arc)
            arcs_set.difference_update(arcs_to_remove)                     
    
    def add_arc(self, nodeA_id, nodeB_id, info = None):
        """
        Adds a new undirected arc in graph, between node_A and node_B with the specified id.
        
        add_arc(nodeA_id, nodeB_id, info) -> None
        
        @type nodeA_id: integer
        @param nodeA_id: id of tail node.
        @type nodeB_id: integer
        @param nodeB_id: id of head node.
        @type info: object
        @param info: element to be added as info to the new arc.    
        """
        try:
            new_arc_AB = GraphIncidenceSet.Arc(nodeA_id, nodeB_id, info)
            new_arc_BA = GraphIncidenceSet.Arc(nodeB_id, nodeA_id, info)
            self._inc[nodeA_id].add(new_arc_AB)
            self._inc[nodeB_id].add(new_arc_BA)
            self._nodes[nodeA_id]._deg += 1
            self._nodes[nodeB_id]._deg += 1  
        except KeyError:
            return 
    
    def remove_arc(self, nodeA_id, nodeB_id):
        """
        Removed from graph the undirected arc between nodeA and nodeB.
        
        remove_arc(nodeA_id, nodeB_id) -> None
        
        @type nodeA_id: integer
        @param nodeA_id: id of tail node.
        @type nodeB_id: integer
        @param nodeB_id: id of head node.    
        """
        try:
            arcs_set_A = self._inc[nodeA_id]
            arcs_to_remove = Set()
            for arc in arcs_set_A:
                if arc._head is nodeB_id:
                    arcs_to_remove.add(arc)
                    self._nodes[nodeA_id]._deg -= 1
            arcs_set_A.difference_update(arcs_to_remove)
            arcs_set_B = self._inc[nodeB_id]
            arcs_to_remove = Set()
            for arc in arcs_set_B:
                if arc._head == nodeA_id:
                    arcs_to_remove.add(arc)
                    self._nodes[nodeB_id]._deg -= 1
            arcs_set_B.difference_update(arcs_to_remove)
        except KeyError:
            return
        
    def set_arc_status(self, nodeA_id, nodeB_id, status):
        """
        Sets the status of the directed arc between nodeA and nodeB.
        
        set_arc_status(nodeA_id, nodeB_id, status) -> None
        
        @type nodeA_id: integer
        @param nodeA_id: id of tail node.
        @type nodeB_id: integer
        @param nodeB_id: id of head node.
        @type status: object
        @param status: element to be added as status info to the specified arc.    
        """ 
        try:
            arcs_set_A = self._inc[nodeA_id]
            for arc in arcs_set_A:
                if arc._head == nodeB_id:
                    arc.status = status
                    break
        except KeyError:
            return   
        
    def get_nodes(self):
        """
        Returns all nodes in graph        
        get_nodes() -> nodes_list
        
        @rtype: list
        @return: list of nodes in graph.    
        """
        return [node for node in self._nodes.itervalues()]
    
    def get_arcs(self):
        """
        Returns all undirected arcs in graph.
        
        get_arcs() -> arcs_list
        
        @rtype: list
        @return: list of undirected arcs in graph.    
        """
        arcs = []
        for arcs_set in self._inc.values():
            for arc in arcs_set: arcs.append(arc)
        return arcs
        
    def get_num_nodes(self):
        """
        Returns the number of nodes in graph.
        
        get_num_nodes() -> number_of_nodes
        
        @rtype: integer
        @return: number of nodes in graph.    
        """
        return len(self._nodes)
    
    def get_num_arcs(self):
        """
        Returns the number of undirected arcs in graph.
        
        get_num_arcs() -> number_of_arcs
        
        @rtype: integer
        @return: number of undirected arcs in graph.    
        """
        num_arcs = 0
        for node in self._nodes.values(): num_arcs += node._deg
        return (num_arcs / 2) + 1
    
    def is_node_in_graph(self, node_id):
        return node_id in self._nodes   
    
    def get_node_by_id(self, node_id):
        """
        Returns node in graph by id.
        
        get_node_by_id(node_id) -> node
        
        @type node_id: integer
        @param node_id: id of the requested node in graph. 
        
        @rtype: node
        @return: node corresponding to the given id.
        """
        try:
            return self._nodes[node_id]
        except KeyError:
            return None
    
    def get_incident_arcs(self, node_id):
        """
        Returns all incident arcs to the specified node.
        
        get_incident_arcs(node_id) -> list/set
        
        @type node_id: integer
        @param node_id: id of node whos incident arcs have been requested.  
        
        @rtype: list/set
        @return: all arcs that are incident to the node whose id has been specified.  
        """
        try:
            return self._inc[node_id]
        except KeyError:
            return Set()
    
    def are_adjacent(self, nodeA_id, nodeB_id):
        """
        Returns True if nodeA and nodeB are adjacent, otherwise returns False.
        
        are_adjacent(nodeA_id, nodeB_id) -> True/False
        
        @type nodeA_id: integer
        @param nodeA_id: first node's id.
        @type nodeB_id: integer
        @param nodeB_id: second node's id.
        
        @rtype: boolean
        @return: True if nodeA and nodeB are adjacent, otherwise False.    
        """
        try:
            arcs_set = self._inc[nodeA_id] 
            for arc in arcs_set: 
                if arc._head == nodeB_id: return True
            return False
        except KeyError:
            return False  
        
    def dfs(self, root_node_id):
        """
        Returns the LIFO path-as-list from graph's root to all other nodes in graph.
        
        dfs(root_node_id) -> path
        
        @type root_node_id: integer
        @param root_node_id: graph's root's id.
        
        @rtype: list
        @return: LIFO path from graph's root to all other nodes in graph.
        """
        try: 
            status = dict.fromkeys(self._nodes.iterkeys(), 0)
            status[root_node_id] = 1            
            L = []        
            s = Stack()
            s.push(root_node_id)            
            while not s.is_empty():
                curr_node_id = s.pop()
                status[curr_node_id] = -1
                L.append(self._nodes[curr_node_id])
                arcs_set = self._inc[curr_node_id]
                for arc in arcs_set:
                    if status[arc._head] is 0:
                        status[arc._head] = 1
                        s.push(arc._head)
            return L
        except KeyError:
            return []       

    def bfs(self, root_node_id):
        """
        Returns the FIFO path-as-list from graph's root to all other nodes in graph.
        
        bfs(root_node_id) -> path
        
        @type root_node_id: integer
        @param root_node_id: graph's root's id.
        
        @rtype: list
        @return: FIFO path from graph's root to all other nodes in graph.
        """
        try:       
            status = dict.fromkeys(self._nodes.iterkeys(), 0)
            status[root_node_id] = 1                   
            L = []
            q = Queue()
            q.enqueue(root_node_id)        
            while not q.is_empty():
                curr_node_id = q.dequeue()
                status[curr_node_id] = -1
                L.append(self._nodes[curr_node_id])
                arcs_set = self._inc[curr_node_id]
                for arc in arcs_set:
                    if status[arc._head] is 0:
                        status[arc._head] = 1
                        q.enqueue(arc._head)        
            return L
        except KeyError:
            return []           
    
    def __repr__(self):
        s = "{"       
        for node in self._nodes.itervalues():
            arcs_set = self._inc[node._id]
            s += "{} : {}\n".format(str(node), str(arcs_set)) 
        s += "}"
        return s
    
    def __str__(self):
        return self.__repr__()    
    
def __test(graph): 
    """
    Graph Test.
    
    __test(graph) -> None
    
    @type graph: basegraph
    @param graph: graph instance.    
    """   
    
    if not isinstance(graph, basegraph):
        raise TypeError("Expected type was Graph.")
    
    print "### iPATH TEST DATA STRUCTURE"
    print "### Data Type: Graph ({})".format(str(graph.__class__.__bases__[0].__name__))
    print "### Implementation: {}".format(str(graph.__class__.__name__))
    
    print "\n*** ADD NODE ***\n"    
    for i in range(10):
        print "add_node({})".format(str(i))   
        graph.add_node(i) 
    
    print "\n*** ADD ARC ***\n"    
    for i in range(10):
        print "add_arc({}, {}, {})".format(str(i), str(i + 1), str(2 * (i + 1)))
        graph.add_arc(i, i + 1, 2 * (i + 1))
        print "add_arc({}, {}, {})".format(str(i), str(i + 2), str(2 * (i + 2)))
        graph.add_arc(i, i + 2, 2 * (i + 2))
        
    print "\n*** GRAPH ***\n"    
    print "\n{}\n".format(str(graph))
    
    print "\n*** REMOVE NODE ***\n"    
    print "remove_node(5)"
    graph.remove_node(5)
    
    print "\n*** GRAPH ***\n"    
    print "\n{}\n".format(str(graph))
    
    print "\n*** REMOVE ARC ***\n"       
    print "remove_arc(7, 8)"    
    graph.remove_arc(7, 8)
    
    print "\n*** GRAPH ***\n"    
    print "\n{}\n".format(str(graph))
    
    print "\n*** INCIDENT ARCS ***\n"    
    for node in graph.get_nodes():
        print "Incident Arcs of {}\t{}\n".format(str(node), str(graph.get_incident_arcs(node._id)))
        
    print "\n*** ADJACENCY ***\n"    
    for i in range(10):
        for j in range(10):
            if graph.are_adjacent(i, j) == True:
                print "Adjacency Between ({}, {}): True\n".format(str(i), str(j))
                    
    print "\n*** NODES ***\n"    
    print "numNodes: {}\n".format(str(graph.get_num_nodes())) 
    print "Nodes: {}\n".format(str(graph.get_nodes()))  
    
    print "\n*** ARCS ***\n" 
    print "numArcs: {}\n".format(str(graph.get_num_arcs()))      
    print "Arcs: {}\n".format(str(graph.get_arcs()))   
    
    print "\n*** SEARCH BFS ***\n"           
    for i in range(10):        
        print "bfs({})".format(str(i))
        Lbfs = graph.bfs(i)
        for n in Lbfs:
            print "{}\n".format(str(n))
        print "\n"
        
    print "\n*** SEARCH DFS ***\n"        
    for i in range(9):
        print "dfs({})".format(str(i))
        Ldfs = graph.dfs(i)
        for n in Ldfs:
            print "{}\n".format(str(n))
        print "\n"
        
    print "\n### END OF TEST ###\n"

if __name__ == "__main__":    
    graph = GraphIncidenceList()
    __test(graph)   
    graph = GraphIncidenceSet()
    __test(graph)   
