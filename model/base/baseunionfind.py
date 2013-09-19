class baseunionfind:
    """
    Union-Find interface.

    makeset(element)
    union(element_A, element_B)
    find(element)
    """
    
    def makeset(self):
        """
        Creates a new Union-Find with the specified element.
        
        makeset(element) -> new_root
        
        @type element: object
        @param element: element to be added to the new Union-Find.
        
        @rtype: node
        @return: the new Union-Find's root node.
        """
        raise NotImplementedError("makeset: You should have implemented this method!")
    
    def union(self, root_node_A, root_node_B):
        """
        Builds and returns the union between the Union-Find corresponding to the specified element_A
        with the Union-Find corresponding to the specified element_B.
        
        union(root_node_A, root_node_B) -> updated_root_node_A
        
        @type root_node_A: node
        @param root_node_A: first Union-Find's root node
        @type root_node_B: node
        @param root_node_B: second Union-Find's root node.
        
        @rtype: node
        @return: the updated first Union-Find's root node.
        """
        raise NotImplementedError("union: You should have implemented this method!")
    
    def find(self, element):
        """
        Returns the root node of the specified element.
        
        find(element) -> root_node
        
        @type element: object
        @param element: element whose root node will be returned.
        
        @rtype: node
        @return: root node.
        """
        raise NotImplementedError("find: You should have implemented this method!") 