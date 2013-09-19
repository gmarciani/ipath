#Interface Import
from model.base.basestack import basestack
#Support Data-Structures Imports
from model.linkedlist import SimpleLinkedList as LinkedList
from collections import deque

class StackLinkedList(LinkedList, basestack):

    def push(self, element):
        """
        Pushes element into the stack.
        
        push(element) -> None
        
        @type element: object
        @param element: element to be pushed into the stack.
        """
        self.add_as_first(element)

    def top(self):
        """
        Returns the element at the top of the stack.
        
        top() -> top_element
        
        @rtype: object
        @return: element at the top of the stack.
        """
        return self.get_first()

    def pop(self):
        """
        Returns and deletes the element at the top of the stack.
        
        pop() -> top_element
        
        @rtype: object
        @return: element at the top of the stack.
        """
        return self.pop_first()    
    
class StackArrayList(basestack):
    
    def __init__(self):
        self._s = []
        
    def is_empty(self):
        """
        Returns True if the stack is empty, otherwise returns False.
        
        is_empty() -> True/False
        
        @rtype: boolean
        @return: True if the stack is empty, otherwise False.        
        """
        return len(self._s) == 0
        
    def push(self, element):
        """
        Pushes element into the stack.
        
        push(element) -> None
        
        @type element: object
        @param element: element to be pushed into the stack.
        """
        self._s.append(element)
        
    def top(self):
        """
        Returns the element at the top of the stack.
        
        top() -> top_element
        
        @rtype: object
        @return: element at the top of the stack.
        """
        return None if len(self._s) == 0 else self._s[-1]
        
    def pop(self):
        """
        Returns and deletes the element at the top of the stack.
        
        pop() -> top_element
        
        @rtype: object
        @return: element at the top of the stack.
        """
        return None if len(self._s) == 0 else self._s.pop()
        
    def __repr__(self):
        return str(self._s) 
    
    def __str__(self):
        return self.__repr__()    
    
class StackDeque(basestack):
    
    def __init__(self):
        self._q = deque()
        
    def is_empty(self):
        """
        Returns True if the stack is empty, otherwise returns False.
        
        is_empty() -> True/False
        
        @rtype: boolean
        @return: True if the stack is empty, otherwise False.        
        """
        return len(self._q) == 0
    
    def push(self, element):
        """
        Pushes element into the stack.
        
        push(element) -> None
        
        @type element: object
        @param element: element to be pushed into the stack.
        """
        self._q.appendleft(element)
        
    def top(self):
        """
        Returns the element at the top of the stack.
        
        top() -> top_element
        
        @rtype: object
        @return: element at the top of the stack.
        """
        return None if len(self._q) == 0 else self._q[0]
        
    def pop(self):
        """
        Returns and deletes the element at the top of the stack.
        
        pop() -> top_element
        
        @rtype: object
        @return: element at the top of the stack.
        """
        return None if len(self._q) == 0 else self._q.popleft()
        
    def __repr__(self):
        return str(self._q)[6:-1]
    
    def __str__(self):
        return self.__repr__()

def __test(stack):
    """
    Stack Test.
    
    __test(stack) -> None
    
    @type stack: basestack
    @param stack: stack instance.
    """    
    if not isinstance(stack, basestack):
        raise TypeError("Expected type was Stack.")
    
    print "### iPATH TEST DATA STRUCTURE"
    print "### Data Type: Stack ({})".format(str(stack.__class__.__bases__[0].__name__))
    print "### Implementation: {}".format(str(stack.__class__.__name__))
    
    print "\n*** PUSH ***\n"    
    for i in range(10):
        print "push({})".format(str(i))
        stack.push(i)
        
    print "\n{}\n".format(str(stack))
    
    print "\n*** POP ***\n"    
    for i in range(2):
        print "top(): {}".format(str(stack.top())) 
        print "pop(): {}".format(str(stack.pop()))
        
    print "\n{}\n".format(str(stack))
    
    print "\n*** EMPTYING ***\n"    
    while not stack.is_empty():
        stack.pop()
        print "{}".format(str(stack))
        
    print "\n### END OF TEST ###\n"      

if __name__ == "__main__":
    stack = StackLinkedList()
    __test(stack)
    
    stack = StackArrayList()
    __test(stack)
    
    stack = StackDeque()
    __test(stack)