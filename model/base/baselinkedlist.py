class baselinkedlist:
    """
    Linked-List interface.
    
    is_empty()        
    add_as_first(element)    
    add_as_last(element)    
    get_first()    
    get_last()
    get_first_record()
    get_last_record()
    pop_first()
    pop_last()
    delete_record(record)
    """
        
    def is_empty(self):
        """
        Returns True if linked-list is empty, otherwise False.
        
        is_empty() -> True/False
        
        @rtype: boolean
        @return: True if empty, False otherwise.
        """
        raise NotImplementedError("is_empty: You should have implemented this method!")

    def add_as_first(self, element):
        """
        Adds element as first into the linked-list.
        
        add_as_first(element) -> None
        
        @type element: object
        @param element: element to be added as first into the linked-list.
        """
        raise NotImplementedError("add_as_first: You should have implemented this method!")
    
    def add_as_last(self, element):
        """
        Adds element as last into the linked-list.
        
        add_as_last(element) -> None
        
        @type element: object
        @param element: element to be added as last into the linked-list.
        """
        raise NotImplementedError("add_as_last: You should have implemented this method!")
    
    def get_first(self):
        """
        Returns the first element into the linked-list.
        
        get_first() -> first_element
        
        @rtype: object
        @return: first element into the linked-list.
        """
        raise NotImplementedError("get_first: You should have implemented this method!")

    def get_last(self):
        """
        Returns the last element into the linked-list.
        
        get_last() -> last_element
        
        @rtype: object
        @return: last element into the linked-list.
        """
        raise NotImplementedError("get_last: You should have implemented this method!")
              
    def get_first_record(self):
        """
        Returns the first record into the linked-list.
        
        get_first_record() -> first_record
        
        @rtype: Record
        @return: first record into the linked-list.
        """
        raise NotImplementedError("get_first_record: You should have implemented this method!")       

    def get_last_record(self):
        """
        Returns the last record into the linked-list.
        
        get_last_record() -> last_record
        
        @rtype: Record
        @return: last record into the linked-list.
        """
        raise NotImplementedError("get_last_record: You should have implemented this method!")  
    
    def pop_first(self):
        """
        Deletes the first record from the linked-list, and return the correspondent element.
        
        pop_first() -> first_element
        
        @rtype: object
        @return: first element into the linked-list.
        """
        raise NotImplementedError("pop_first: You should have implemented this method!")
      
    def pop_last(self):
        """
        Deletes the last record from the linked-list, and return the correspondent element.
        
        pop_last() -> last_element
        
        @rtype: object
        @return: last element into the linked-list.
        """
        raise NotImplementedError("pop_last: You should have implemented this method!")
    
    def delete_record(self, record):
        """
        Deletes the specified record from the linked-list.
        
        delete_record(record) -> None
        
        @type record: Record
        @param record: record to be deleted from the linked-list.
        """
        raise NotImplementedError("delete_record: You should have implemented this method!")