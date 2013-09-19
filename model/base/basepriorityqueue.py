class basepriorityqueue:
    """
    Priority-Queue interface.
    
    is_empty()
    find_min()
    insert(element, key)
    delete_min()
    decrease_key(element, new_key)
    increase_key(element, new_key)
    """
    
    def is_empty(self):
        """
        Returns True if the Priority-Queue is empty, otherwise False.
        
        is_empty() -> True/False
        
        @rtype: boolean
        @return: True if the Priority-Queue is empty, otherwise False.
        """
        raise NotImplementedError("is_empty: You should have implemented this method!")
    
    def insert(self, element, key):
        """
        Inserts into the Priority-Queue a new node with the specified element and priority-key.
        
        insert(element, key) -> None
        
        @type element: object
        @param element: element to be added into the Priority-Queue.
        @type key: float
        @param key: priority-key of the new element.
        """
        raise NotImplementedError("insert: You should have implemented this method!")
    
    def find_min(self):
        """
        Returns the node with the minimum priority.
        
        find_min() -> min_node
        
        @rtype: priority queue node
        @return: minimum priority node.
        """
        raise NotImplementedError("find_min: You should have implemented this method!")       
    
    def delete_min(self):
        """
        Deletes and returns the node with the minimum priority-key in the Priority-Queue.
        
        delete_min() -> min_node
        
        @rtype: priority queue node
        @return: node with the minimum priority-key
        """
        raise NotImplementedError("delete_min: You should have implemented this method!")   
    
    def decrease_key(self, element, new_key):
        """
        Decreases the priority-key of the specified element to the specified new key.
        
        decrease_key(element, new_key) -> None
        
        @type element: object
        @param element: element whose priority-key is going to be decreased.
        @type new_key: float
        @param new_key: new smaller priority-key.
        """
        raise NotImplementedError("decrease_key: You should have implemented this method!")
    
    def increase_key(self, element, new_key):
        """
        Increases the priority-key of the specified element to the specified new key.
        
        increase_key(element, new_key) -> None
        
        @type element: object
        @param element: element whose priority-key is going to be increased.
        @type new_key: float
        @param new_key: new bigger priority-key.
        """
        raise NotImplementedError("increase_key: You should have implemented this method!")