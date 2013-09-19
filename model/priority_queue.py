#Interface Import
from model.base.basepriorityqueue import basepriorityqueue
#Support Data-Structures Import
from model.binomial_tree import BinomialTree as BinomialTree    
#Exception Import
from exception.exceptions import PriorityQueueInvalidKeyError  
    
class DHeap(basepriorityqueue):
    
    class Node:
    
        def __init__(self, element, key, index):
            self.element = element
            self._key = key
            self._index = index
        
        def __repr__(self):
            return "*({}, {})".format(str(self.element), str(self._key)) 
    
        def __str_(self):
            return self.__repr__() 
    
    def __init__(self, deg = 4):
        self._heap = []
        self._deg = deg
        self._node_map = {}
    
    def is_empty(self):
        """
        Returns True if the Priority-Queue is empty, otherwise False.
        
        is_empty() -> True/False
        
        @rtype: boolean
        @return: True if the Priority-Queue is empty, otherwise False.
        """
        return (len(self._heap) is 0)

    def find_min(self):
        """
        Returns the node with the minimum priority.
        
        find_min() -> min_node
        
        @rtype: priority queue node
        @return: minimum priority node.
        """
        return None if self.is_empty() else self._heap[0]
    
    def insert(self, element, key): 
        """
        Inserts into the Priority-Queue a new node with the specified element and priority-key.
        
        insert(element, key) -> None
        
        @type element: object
        @param element: element to be added into the Priority-Queue.
        @type key: float
        @param key: priority-key of the new element.
        """       
        node = DHeap.Node(element, key, len(self._heap))
        self._update_node_map_index(node)        
        self._heap.append(node)  
        self._move_up(node) 

    def delete_min(self):
        """
        Deletes and returns the node with the minimum priority-key in the Priority-Queue.
        
        delete_min() -> min_node
        
        @rtype: priority queue node
        @return: node with the minimum priority-key
        """
        if self.is_empty(): return None
        min_node = self._heap[0]
        last_node = self._heap[-1]
        self._swap(min_node, last_node)
        del self._node_map[min_node.element]
        del self._heap[-1]
        self._move_down(last_node)   
        return min_node      
        
    def decrease_key(self, element, new_key):
        """
        Decreases the priority-key of the specified element to the specified new key.
        
        decrease_key(element, new_key) -> None
        
        @type element: object
        @param element: element whose priority-key is going to be decreased.
        @type new_key: float
        @param new_key: new smaller priority-key.
        """
        node = self._find_node_by_element(element)
        if new_key > node._key: raise PriorityQueueInvalidKeyError()
        self._decrease_key(node, new_key)
        
    def increase_key(self, element, new_key):
        """
        Increases the priority-key of the specified element to the specified new key.
        
        increase_key(element, new_key) -> None
        
        @type element: object
        @param element: element whose priority-key is going to be increased.
        @type new_key: float
        @param new_key: new bigger priority-key.
        """   
        node = self._find_node_by_element(element)
        if new_key < node._key: raise PriorityQueueInvalidKeyError()
        self._increase_key(node, new_key)
        
    def _increase_key(self, node, new_key):        
        node._key = new_key
        self._move_down(node)
    
    def _decrease_key(self, node, new_key):        
        node._key = new_key
        self._move_up(node)     

    def _move_up(self, node):
        if node._index <= 0: return 
        father_node = self._find_father(node)
        while father_node is not None and node._key < father_node._key:
            self._swap(node, father_node)
            father_node = self._find_father(node)
    
    def _move_down(self, node):
        sonNode = self._min_son(node)
        while sonNode is not None and node._key > sonNode._key:
            self._swap(node, sonNode)
            sonNode = self._min_son(node)
            
    def _min_son(self, node):
        firstSonIndex = (self._deg * (node._index) + 1)        
        if firstSonIndex >= len(self._heap): return None
        minSon = self._heap[firstSonIndex]
        i = firstSonIndex + 1
        for i in range(firstSonIndex + 1, min(firstSonIndex + self._deg, len(self._heap))):
            if self._heap[i]._key < minSon._key: minSon = self._heap[i]
        return minSon
            
    def _find_father(self, node):
        if node._index <= 0: return None
        father_index = (node._index - 1) / self._deg
        father_node = self._heap[father_index]
        return father_node
            
    def _swap(self, node1, node2):
        self._heap[node1._index] = node2
        self._heap[node2._index] = node1
        node1._index, node2._index = node2._index, node1._index
        self._update_node_map_index(node1)
        self._update_node_map_index(node2)
        
    def _update_node_map_index(self, node):
        self._node_map[node.element] = node._index
        
    def _find_node_by_element(self, element):
        try:
            index = self._node_map[element]
            node = self._heap[index]
        except KeyError:
            return None
        return node
        
    def __repr__(self):
        s = "["
        if not self.is_empty():
            for i in range(len(self._heap)):
                node = self._heap[i]
                s += str(node)
                if (i + 1) < len(self._heap): s += ", "      
        s += "]"
        return s
    
    def __str__(self):
        return self.__repr__()      
    
class BinomialHeap(basepriorityqueue):
    
    MAX_RANK = 32
    MIN_VALUE = - float("inf")
    
    def __init__(self):
        self._heap = self._initialize_heap()
        self._tree_map = {}
        
    def _initialize_heap(self):
        heap = []
        for rank in range(BinomialHeap.MAX_RANK): heap.append([None, None, None])
        return heap            
        
    def is_empty(self):
        """
        Returns True if the Priority-Queue is empty, otherwise False.
        
        is_empty() -> True/False
        
        @rtype: boolean
        @return: True if the Priority-Queue is empty, otherwise False.
        """
        for i in range(len(self._heap)):
            if self._heap[i][0] is not None: return False
        return True       

    def insert(self, element, key):
        """
        Inserts into the Priority-Queue a new node with the specified element and priority-key.
        
        insert(element, key) -> None
        
        @type element: object
        @param element: element to be added into the Priority-Queue.
        @type key: float
        @param key: priority-key of the new element.
        """
        new_btree = BinomialTree(element, key)
        self._tree_map[element] = 0 
        root = new_btree._root
        if self._heap[0][0] is None: self._heap[0][0] = new_btree                       
        else: self._heap[0][1] = new_btree, self._rebuild()
        return root
    
    def find_min(self):
        """
        Returns the node with the minimum priority.
        
        find_min() -> min_node
        
        @rtype: priority queue node
        @return: minimum priority node.
        """
        if self.is_empty(): return None
        return self._heap[self._find_min_rank()][0]._root

    def delete_min(self):
        """
        Deletes and returns the node with the minimum priority-key in the Priority-Queue.
        
        delete_min() -> min_node
        
        @rtype: priority queue node
        @return: node with the minimum priority-key
        """
        if self.is_empty(): return None
        min_rank = self._find_min_rank()
        min_btree = self._heap[min_rank][0]
        del self._node_map[min_btree._root.element]
        sons = min_btree.get_sons()
        self._heap[min_rank][0] = None
        rank = 0
        curr = sons.get_first_record()
        while curr is not None:
            if self._heap[rank][0] is None: self._heap[rank][0] = curr.element
            else: self._heap[rank][1] = curr.element
            rank += 1
            curr = curr._next
        self._rebuild()
        return min_btree._root
    
    def decrease_key(self, element, new_key):
        """
        Decreases the priority-key of the specified element to the specified new key.
        
        decrease_key(element, new_key) -> None
        
        @type element: object
        @param element: element whose priority-key is going to be decreased.
        @type new_key: float
        @param new_key: new smaller priority-key.
        """
        node = self._find_node_by_element(element)
        if new_key > node._key: raise PriorityQueueInvalidKeyError()
        self._decrease_key(node, new_key)
    
    def increase_key(self, element, new_key):
        """
        Increases the priority-key of the specified element to the specified new key.
        
        increase_key(element, new_key) -> None
        
        @type element: object
        @param element: element whose priority-key is going to be increased.
        @type new_key: float
        @param new_key: new bigger priority-key.
        """
        node = self._find_node_by_element(element)
        if new_key > node._key: raise PriorityQueueInvalidKeyError()
        self._increase_key(node, new_key)
    
    def _decrease_key(self, node, new_key):
        node._key = new_key
        while node._father is not None and node._key < node._father._key: node._swap(node._father)
    
    def _increase_key(self, node, new_key):
        self._delete(node)    
        self.insert(node.element, new_key)
    
    def _delete(self, node):
        self._decrease_key(node, BinomialHeap.MIN_VALUE)
        self.delete_min()
        
    def _find_min_rank(self):
        if self.is_empty(): return -1
        for rank in range(BinomialHeap.MAX_RANK):
            if self._heap[rank][0] is not None: break
        for i in range(rank + 1, BinomialHeap.MAX_RANK):
            if self._heap[i][0] is not None and self._heap[i][0]._root._key < self._heap[rank][0]._root._key: rank = i                
        return rank
    
    def _rebuild(self):
        for rank in range(BinomialHeap.MAX_RANK):
            if self._heap[rank][1] is None and self._heap[rank][2] is None: continue            
            if self._heap[rank][1] is not None and self._heap[rank][2] is not None:
                merged = self._heap[rank][1].merge(self._heap[rank][2])
                self._heap[rank][1] = self._heap[rank][2] = None
            else:
                merged = self._heap[rank][0].merge(self._heap[rank][1])
                self._heap[rank][0] = self._heap[rank][1] = None    
            if self._heap[rank + 1][0] is None: self._heap[rank + 1][0] = merged
            elif self._heap[rank + 1][1] is None: self._heap[rank + 1][1] = merged
            else: self._heap[rank + 1][2] = merged    
                
    def _find_node_by_element(self, element):
        rank = self._tree_map[element]
        bTree = self._heap[rank][0]
        node = bTree.get_node_by_element(element)
        return node
                
    def __repr__(self):
        s = "{"
        for rank in range(BinomialHeap.MAX_RANK):
            if self._heap[rank][0] is None: continue
            s += str(self._heap[rank][0])            
        s += "}"
        return s
    
    def __str__(self):
        return self.__repr__()    

def __test(priority_queue):
    """
    Priority-Queue Test.
    
    __test(priority_queue) -> None
    
    @type priority_queue: basepriorityqueue
    @param priority_queue: priority-queue instance.    
    """    
    if not isinstance(priority_queue, basepriorityqueue):
        raise TypeError("Expected type was PriorityQueue.") 
    
    print "### iPATH TEST DATA STRUCTURE"
    print "### Data Type: Priority Queue ({})".format(str(priority_queue.__class__.__bases__[0].__name__))
    print "### Implementation: {}".format(priority_queue.__class__.__name__)   
    
    print "\n*** INSERT ***\n"    
    for i in range(0, 10, 2):
        print "insert({}, {})".format(str(i), str(float(i)))
        priority_queue.insert(i, float(i))
        
    for i in range(1, 10, 2):
        print "insert({}, {})".format(str(i), str(float(i)))
        priority_queue.insert(i, float(i))
    
    print "\n{}\n".format(str(priority_queue))
    
    print "\n*** FIND/DELETE MIN ***\n"    
    for i in range(2):
        print "find_min: {}".format(str(priority_queue.find_min()))
        print "delete_min: {}\n".format(str(priority_queue.delete_min()))
        
    print "\n{}\n".format(str(priority_queue))
    
    print "\n*** DECREASE KEY ***\n"        
    for i in range(5, 10):
        print "decrease_key({}, {})".format(str(i), str(float(i / 2)))
        priority_queue.decrease_key(i, float(i / 2))
        
    print "\n{}\n".format(str(priority_queue))
    
    print "\n*** INCREASE KEY ***\n"        
    for i in range(2, 5):
        print "increase_key({}, {})".format(str(i), str(float(i * 2)))
        priority_queue.increase_key(i, float(i * 2))
        
    print "\n{}\n".format(str(priority_queue)) 
    
    for i in range(2):
        print "find_min: {}".format(str(priority_queue.find_min()))
        print "delete_min: {}\n".format(str(priority_queue.delete_min()))    
    
    print "\n{}\n".format(str(priority_queue))   
    
    print "\n*** EMPTYING ***\n"        
    while priority_queue.is_empty() is False:
        print "find_min: {}".format(str(priority_queue.find_min()))    
        print "delete_min: {}".format(str(priority_queue.delete_min()))       
        
    print "\n{}\n".format(str(priority_queue))
    
    print "\n### END OF TEST ###\n"
    
if __name__ == "__main__":
    priorityQueue = DHeap(4)
    __test(priorityQueue)
    
    #priorityQueue = BinomialHeap()
    #__test(priorityQueue)