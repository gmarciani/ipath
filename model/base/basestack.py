class basestack:
    """
    Stack interface.
    
    is_empty()
    push(element)
    top()
    pop()
    """
    
    def is_empty(self):
        """
        Returns True if the stack is empty, otherwise returns False.
        
        is_empty() -> True/False
        
        @rtype: boolean
        @return: True if the stack is empty, otherwise False.        
        """
        raise NotImplementedError("is_empty: You should have implemented this method!")
        
    def push(self, element):
        """
        Pushes element into the stack.
        
        push(element) -> None
        
        @type element: object
        @param element: element to be pushed into the stack.
        """
        raise NotImplementedError("push: You should have implemented this method!")
        
    def top(self):
        """
        Returns the element at the top of the stack.
        
        top() -> top_element
        
        @rtype: object
        @return: element at the top of the stack.
        """
        raise NotImplementedError("top: You should have implemented this method!")
    
    def pop(self):
        """
        Returns and deletes the element at the top of the stack.
        
        pop() -> top_element
        
        @rtype: object
        @return: element at the top of the stack.
        """
        raise NotImplementedError("pop: You should have implemented this method!") 