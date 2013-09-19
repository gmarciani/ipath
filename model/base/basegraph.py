class basegraph:
    """
    Graph interface.
    
    add_node(element)
    remove_node(node_id)
    add_arc(nodeA_id, nodeB_id, info)
    remove_arc(nodeA_id, nodeB_id)
    set_arc_status(nodeA_id, nodeB_id, status)
    get_nodes()
    get_arcs()
    get_num_nodes()
    get_num_arcs()
    get_node_by_id(node_id)
    get_incident_arcs(node_id)
    are_adjacent(nodeA_id, nodeB_id)
    bfs(root_node_id)
    dfs(root_node_id)
    """
    
    def add_node(self, element):
        """
        Adds a new node in graph, with the specified element.
        
        add_node(element) -> None
        
        @type element: object
        @param element: element to be assigned to the new node.    
        """
        raise NotImplementedError("add_node: You should have implemented this method!")
    
    def remove_node(self, node_id):
        """
        Removes from graph the node with the specified id.
        
        remove_node(node_id) -> None
        
        @type node_id: integer
        @param node_id: id of the node to be removed from graph.
        """
        raise NotImplementedError("remove_node: You should have implemented this method!")
    
    def add_arc(self, nodeA_id, nodeB_id, info):
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
        raise NotImplementedError("add_arc: You should have implemented this method!")    
    
    def remove_arc(self, nodeA_id, nodeB_id):
        """
        Removed from graph the undirected arc between nodeA and nodeB.
        
        remove_arc(nodeA_id, nodeB_id) -> None
        
        @type nodeA_id: integer
        @param nodeA_id: id of tail node.
        @type nodeB_id: integer
        @param nodeB_id: id of head node.    
        """
        raise NotImplementedError("remove_arc: You should have implemented this method!") 
    
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
        raise NotImplementedError("set_arc_status: You should have implemented this method!")
    
    def get_nodes(self):
        """
        Returns all nodes in graph        
        get_nodes() -> nodes_list
        
        @rtype: list
        @return: list of nodes in graph.    
        """
        raise NotImplementedError("get_nodes: You should have implemented this method!")
    
    def get_arcs(self):
        """
        Returns all undirected arcs in graph.
        
        get_arcs() -> arcs_list
        
        @rtype: list
        @return: list of undirected arcs in graph.    
        """
        raise NotImplementedError("get_arcs: You should have implemented this method!")
    
    def get_num_nodes(self):
        """
        Returns the number of nodes in graph.
        
        get_num_nodes() -> number_of_nodes
        
        @rtype: integer
        @return: number of nodes in graph.    
        """
        raise NotImplementedError("get_num_nodes: You should have implemented this method!")
    
    def get_num_arcs(self):
        """
        Returns the number of undirected arcs in graph.
        
        get_num_arcs() -> number_of_arcs
        
        @rtype: integer
        @return: number of undirected arcs in graph.    
        """
        raise NotImplementedError("get_num_arcs: You should have implemented this method!") 
    
    def get_node_by_id(self, node_id):
        """
        Returns node in graph by id.
        
        get_node_by_id(node_id) -> node
        
        @type node_id: integer
        @param node_id: id of the requested node in graph. 
        
        @rtype: node
        @return: node corresponding to the given id.
        """
        raise NotImplementedError("get_node_by_id: You should have implemented this method!")
    
    def get_incident_arcs(self, node_id):
        """
        Returns all incident arcs to the specified node.
        
        get_incident_arcs(node_id) -> list/set
        
        @type node_id: integer
        @param node_id: id of node whos incident arcs have been requested.  
        
        @rtype: list/set
        @return: all arcs that are incident to the node whose id has been specified.  
        """
        raise NotImplementedError("get_incident_arcs: You should have implemented this method!")
    
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
        raise NotImplementedError("are_adjacent: You should have implemented this method!") 
    
    def dfs(self, root_node_id):
        """
        Returns the LIFO path-as-list from graph's root to all other nodes in graph.
        
        dfs(root_node_id) -> path
        
        @type root_node_id: integer
        @param root_node_id: graph's root's id.
        
        @rtype: list
        @return: LIFO path from graph's root to all other nodes in graph.
        """
        raise NotImplementedError("dfs: You should have implemented this method!")          
    
    def bfs(self, root_node_id):
        """
        Returns the FIFO path-as-list from graph's root to all other nodes in graph.
        
        bfs(root_node_id) -> path
        
        @type root_node_id: integer
        @param root_node_id: graph's root's id.
        
        @rtype: list
        @return: FIFO path from graph's root to all other nodes in graph.
        """
        raise NotImplementedError("bfs: You should have implemented this method!")  
    
    