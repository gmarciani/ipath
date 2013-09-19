#Interface Import
from model.base.baselinkedlist import baselinkedlist            

class SimpleLinkedList(baselinkedlist):
    
    class Record:
    
        def __init__(self, element):
            self.element = element
            self._next = None   
        
        def __repr__(self):
            return str(self.element)
    
        def __str__(self):
            return self.__repr__()
    
    def __init__(self):
        self._first = None
        self._last = None
        self._num_elements = 0
        
    def is_empty(self):
        """
        Returns True if linked-list is empty, otherwise False.
        
        is_empty() -> True/False
        
        @rtype: bool
        @return: True if empty, False otherwise.
        """
        return (self._first is None)

    def add_as_first(self, element):
        """
        Adds element as first into the linked-list.
        
        add_as_first(element) -> None
        
        @type element: object
        @param element: element to be added as first into the linked-list.
        """
        record = SimpleLinkedList.Record(element)
        if self._first is None:
            self._first = self._last = record
        else:
            record._next = self._first
            self._first = record
        self._num_elements += 1
            
    def add_as_last(self, element):
        """
        Adds element as last into the linked-list.
        
        add_as_last(element) -> None
        
        @type element: object
        @param element: element to be added as last into the linked-list.
        """
        record = SimpleLinkedList.Record(element)
        if self._first is None:
            self._first = self._last = record
        else:
            self._last._next  = record
            self._last = record
        self._num_elements += 1
            
    def get_first(self):
        """
        Returns the first element into the linked-list.
        
        get_first() -> first_element
        
        @rtype: object
        @return: first element into the linked-list.
        """
        return None if self._first is None else self._first.element            

    def get_last(self):
        """
        Returns the last element into the linked-list.
        
        get_last() -> last_element
        
        @rtype: object
        @return: last element into the linked-list.
        """
        return None if self._last is None else self._last.element
              
    def get_first_record(self):
        """
        Returns the first record into the linked-list.
        
        get_first_record() -> first_record
        
        @rtype: Record
        @return: first record into the linked-list.
        """
        return None if self._first is None else self._first

    def get_last_record(self):
        """
        Returns the last record into the linked-list.
        
        get_last_record() -> last_record
        
        @rtype: Record
        @return: last record into the linked-list.
        """
        return None if self._first is None else self._last
        
    def pop_first(self):
        """
        Deletes the first record from the linked-list, and return the correspondent element.
        
        pop_first() -> first_element
        
        @rtype: object
        @return: first element into the linked-list.
        """
        if self._first is None:
            return None
        else:
            first_element = self._first.element
            self._first = self._first._next
            if self._first is None:
                self._last = None 
            self._num_elements -= 1
            return first_element
        
    def pop_last(self):
        """
        Deletes the last record from the linked-list, and return the correspondent element.
        
        pop_last() -> last_element
        
        @rtype: object
        @return: last element into the linked-list.
        """
        if self._first is None:
            return None
        else:
            last_element = self._last.element
            curr = self.get_first_record()
            prev = None
            while curr is not self._last:
                prev = curr
                curr = curr._next
            if prev is None:
                self._first = None
                self._last = None
            else:
                self._last = prev
                prev._next = None
                
            self._num_elements -= 1
            return last_element
        
    def delete_record(self, record):
        """
        Deletes the specified record from the linked-list.
        
        delete_record(record) -> None
        
        @type record: Record
        @param record: record to be deleted from the linked-list.
        """
        if self._first is None or record is None:
            return
        self._num_elements -= 1
        curr = self.get_first_record()
        prev = None
        while curr is not None:
            if curr is record:
                if prev is None:
                    self._first = curr._next
                elif curr._next is None:
                    self._last = prev
                    prev._next = None
                else:
                    prev._next = curr._next
                break
            
            prev = curr
            curr = curr._next        
  
    def __repr__(self):
        s = "["
        if self._first is not None:
            curr = self._first
            while curr is not None:
                if len(s) > 1:
                    s += ", "
                s += str(curr)
                curr = curr._next
        s += "]"
        return s  
    
    def __str__(self):
        return self.__repr__()   

class DoubleLinkedList(SimpleLinkedList, baselinkedlist):
    
    class Record(SimpleLinkedList.Record):
    
        def __init__(self, element):
            SimpleLinkedList.Record.__init__(self, element)
            self._prev = None
        
        def __repr__(self):
            return str(self.element)
    
        def __str__(self):
            return self.__repr__() 
    
    def add_as_first(self, element):
        """
        Adds element as first into the linked-list.
        
        add_as_first(element) -> None
        
        @type element: object
        @param element: element to be added as first into the linked-list.
        """
        record = DoubleLinkedList.Record(element)
        if self._first is None:
            self._first = self._last = record
        else:
            self._first._prev = record
            record._next = self._first
            self._first = record
        self._num_elements += 1
    
    def add_as_last(self, element):
        """
        Adds element as last into the linked-list.
        
        add_as_last(element) -> None
        
        @type element: object
        @param element: element to be added as last into the linked-list.
        """
        record = DoubleLinkedList.Record(element)
        if self._first is None:
            self._first = self._last = record
        else:
            record._prev = self._last
            self._last._next = record
            self._last = record
        self._num_elements += 1
    
    def pop_first(self):
        """
        Deletes the first record from the linked-list, and return the correspondent element.
        
        pop_first() -> first_element
        
        @rtype: object
        @return: first element into the linked-list.
        """
        if self._first is None:
            return None
        else:
            res = self._first.element
            self._first = self._first._next
            if self._first != None:
                self._first._prev = None  
            else:
                self._last = None
            self._num_elements -= 1
            return res            
    
    def pop_last(self):
        """
        Deletes the last record from the linked-list, and return the correspondent element.
        
        pop_last() -> last_element
        
        @rtype: object
        @return: last element into the linked-list.
        """
        if self._first is None:
            return None
        else:
            res = self._last.element
            self._last = self._last._prev
            if self._last is not None:
                self._last._next = None
            else:
                self._first = None
            self._num_elements -= 1
            return res

    def delete_record(self, record):
        """
        Deletes the specified record from the linked-list.
        
        delete_record(record) -> None
        
        @type record: Record
        @param record: record to be deleted from the linked-list.
        """
        if record is None:
            return
        self._num_elements -= 1
        if record._prev is not None:
            record._prev._next = record._next
        else:
            self._first = record._next
        if record._next is not None:
            record._next._prev = record._prev
        else:
            self._last = record._prev            

def __test(linked_list):
    """
    Linked-List Test.
    
    __test(linked_list) -> None
    
    @type linked_list: baselinkedlist
    @param linked_list: linked_list instance.    
    """    
    if not isinstance(linked_list, baselinkedlist):
        raise TypeError("Expected type was LinkedList.")
    
    print "### iPATH TEST DATA STRUCTURE"
    print "### Data Type: Linked List ({})".format(str(linked_list.__class__.__bases__[0].__name__))
    print "### Implementation: {}".format(str(linked_list.__class__.__name__))
    
    print "\n*** INSERT AS FIRST ***\n"    
    for i in range(5):
        print "add_as_first({})".format(str(i))
        linked_list.add_as_first(i)
        
    print "\n*** INSERT AS LAST ***\n"        
    for i in range(5, 10):
        print "add_as_last({})".format(str(i))
        linked_list.add_as_last(i)  
        
    print "\n{}\n".format(str(linked_list))
    
    print "\n*** GET FIRST/LAST ELEMENT ***\n"    
    print "get_first(): {}\n".format(str(linked_list.get_first()))
    print "get_last(): {}\n".format(str(linked_list.get_last()))
    
    print "\n*** GET FIRST/LAST RECORD ***\n"    
    print("record1 = get_first_record(): {}").format(str(linked_list.get_first_record()))
    record1 = linked_list.get_first_record()
    print("record2 = get_last_record(): {}").format(str(linked_list.get_last_record()))
    record2 = linked_list.get_last_record()
    
    print "\n*** DELETE RECORD ***\n"    
    print("delete_record(record1)")
    linked_list.delete_record(record1)
    print("delete_record(record2)")
    linked_list.delete_record(record2)
    
    print "\n*** POP FIRST/LAST ***\n"    
    print "pop_first(): {}".format(str(linked_list.pop_first()))
    print "pop_last(): {}".format(str(linked_list.pop_last()))
    
    print "\n{}\n".format(linked_list)
    
    print "\n*** EMPTYING ***\n"    
    while not linked_list.is_empty():
        linked_list.pop_last()
        print "{}".format(str(linked_list)) 
        
    print "\n### END OF TEST ###\n"      

if __name__ == "__main__":    
    linkedlist = SimpleLinkedList()
    __test(linkedlist) 
    
    linkedlist = DoubleLinkedList()
    __test(linkedlist)