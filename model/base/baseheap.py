class baseheap:
    """
    Heap interface.
    
    is_empty()
    find_min()
    delete_min()
    find_max()
    delete_max()
    """
    
    def is_empty(self):
        """
        Returns True if heap is empty, otherwise False.
        
        is_empty() -> True/False
        
        @rtype: boolean
        @return: True if the heap is empty, otherwise False.
        """
        raise NotImplementedError("is_empty: You should have implemented this method!")
    
    def find_min(self):
        """
        Returns the minimum element into the heap.
        
        find_min() -> min_element
        
        @rtype: object
        @return: minimum element into the heap.
        """
        raise NotImplementedError("find_min: You should have implemented this method!")
    
    def delete_min(self):
        """
        Returns and deletes the minimum element into the heap.
        
        delete_min() -> min_element
        
        @rtype: object
        @return: minimum element into the heap.
        """
        raise NotImplementedError("delete_min: You should have implemented this method!")
    
    def find_max(self):
        """
        Returns the maximum element into the heap.
        
        find_max() -> max_element
        
        @rtype: object
        @return: maximum element into the heap.
        """
        raise NotImplementedError("find_max: You should have implemented this method!")
    
    def delete_max(self):
        """
        Returns and deletes the maximum element into the heap.
        
        delete_max() -> max_element
        
        @rtype: object
        @return: maximum element into the heap.
        """
        raise NotImplementedError("delete_max: You should have implemented this method!")  