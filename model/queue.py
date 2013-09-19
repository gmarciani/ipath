#Interface Import
from model.base.basequeue import basequeue
#Support Data-Structures Imports
from model.linkedlist import SimpleLinkedList as LinkedList
from collections import deque        

class QueueLinkedList(LinkedList, basequeue):
    
    def enqueue(self, element):
        """
        Enqueues the element at the end of the queue.
        
        enqueue(element) -> None
        
        @type element: object
        @param element: element to be enqueued at the end of the queue.
        """
        self.add_as_last(element)
    
    def dequeue(self):
        """
        Dequeues and deletes the first element from the queue.
        
        dequeue() -> first_element
        
        @rtype: object
        @return: first element of the queue.
        """
        return self.pop_first()

class QueueDeque(basequeue):
    
    def __init__(self):
        self._q = deque()
        
    def is_empty(self):
        """
        Returns True if the queue is empty, otherwise False.
        
        is_empty() -> True/False
        
        @rtype: boolean
        @return: True is the stack is empty, otherwise False.
        """
        return len(self._q) == 0
        
    def enqueue(self, element):
        """
        Enqueues the element at the end of the queue.
        
        enqueue(element) -> None
        
        @type element: object
        @param element: element to be enqueued at the end of the queue.
        """
        self._q.append(element)
        
    def get_first(self):
        """
        Returns the first element of the queue.
        
        get_first() -> first_element
        
        @rtype: object
        @return: first element of the queue.
        """
        return None if len(self._q) == 0 else self._q[0]
        
    #Override
    def dequeue(self):
        """
        Dequeues and deletes the first element from the queue.
        
        dequeue() -> first_element
        
        @rtype: object
        @return: first element of the queue.
        """
        return None if len(self._q) == 0 else self._q.popleft()
    
    def __repr__(self):
        return str(self._q)[6 : -1]
    
    def __str__(self):
        return self.__repr__()         

def __test(queue):
    """
    Queue Test.
    
    __test(queue) -> None
    
    @type queue: basequeue
    @param queue: queue instance.
    """    
    if not isinstance(queue, basequeue):
        raise TypeError("Expected type was Queue.")
    
    print "### iPATH TEST DATA STRUCTURE"
    print "### Data Type: Queue ({})".format(str(queue.__class__.__bases__[0].__name__))
    print "### Implementation: {}".format(str(queue.__class__.__name__))
    
    print "\n*** ENQUEUE ***\n"    
    for i in range(10):
        print "enqueue({})".format(str(i))
        queue.enqueue(i)

    print "\n{}\n".format(str(queue))
    
    print "\n*** DEQUEUE ***\n"    
    for i in range(2):
        print "dequeue(): {}\n".format(str(queue.dequeue()))

    print "\n{}\n".format(str(queue))
    
    print "\n*** GET FIRST ***\n"    
    print "get_first(): {}\n".format(str(queue.get_first()))
    
    print "\n{}\n".format(str(queue))
    
    print "\n*** EMPTYING ***\n"    
    while not queue.is_empty():
        queue.dequeue()
        print "{}".format(str(queue))
        
    print "\n### END OF TEST ###\n"

if __name__ == "__main__":
    queue = QueueLinkedList()
    __test(queue)
    
    queue = QueueDeque()
    __test(queue)
