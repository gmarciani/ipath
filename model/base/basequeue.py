class basequeue:
    """
    Queue interface.
    
    is_empty()
    enqueue(element)
    get_first()
    dequeue()
    """
    
    def is_empty(self):
        """
        Returns True if the queue is empty, otherwise False.
        
        is_empty() -> True/False
        
        @rtype: boolean
        @return: True is the stack is empty, otherwise False.
        """
        raise NotImplementedError("is_empty: You should have implemented this method!")    
    
    def enqueue(self, element):
        """
        Enqueues the element at the end of the queue.
        
        enqueue(element) -> None
        
        @type element: object
        @param element: element to be enqueued at the end of the queue.
        """
        raise NotImplementedError("enqueue: You should have implemented this method!")
    
    def get_first(self):
        """
        Returns the first element of the queue.
        
        get_first() -> first_element
        
        @rtype: object
        @return: first element of the queue.
        """
        raise NotImplementedError("get_first: You should have implemented this method!")
        
    def dequeue(self):
        """
        Dequeues and deletes the first element from the queue.
        
        dequeue() -> first_element
        
        @rtype: object
        @return: first element of the queue.
        """
        raise NotImplementedError("dequeue: You should have implemented this method!") 