#Interface Import
from model.base.baseheap import baseheap    

class HeapMin(baseheap):
    
    def __init__(self, L):
        self._heap = L
        self._length = len(L)
        self._heapify()
    
    def is_empty(self):
        """
        Returns True if heap is empty, otherwise False.
        
        is_empty() -> True/False
        
        @rtype: boolean
        @return: True if the heap is empty, otherwise False.
        """
        return self._length == 0    
      
    def find_min(self):
        """
        Returns the minimum element into the heap.
        
        find_min() -> min_element
        
        @rtype: object
        @return: minimum element into the heap.
        """
        return None if self._length == 0 else self._heap[0]
        
    def delete_min(self):
        """
        Returns and deletes the minimum element into the heap.
        
        delete_min() -> min_element
        
        @rtype: object
        @return: minimum element into the heap.
        """
        if self._length == 0:
            return None
        min = self._heap[0]
        self._heap[0], self._heap[self._length - 1] = self._heap[self._length - 1], self._heap[0]
        self._length -= 1
        self._move_down(0) 
        return min
    
    def _heapify(self):
        self._recursive_heapify(0, self._length - 1)
        
    def _recursive_heapify(self, first, last):            
        if first > last:
            return
        self._recursive_heapify((2 * first) + 1, last) 
        self._recursive_heapify((2 * first) + 2, last) 
            
        self._move_down(first)
        
    def _move_down(self, father_index):
        son_index = self._min_son(father_index)
        while son_index != -1 and self._heap[son_index] < self._heap[father_index]:
            self._heap[son_index], self._heap[father_index] = self._heap[father_index], self._heap[son_index]
            father_index = son_index
            son_index = self._min_son(father_index)
            
    def _min_son(self, father_index):
        if (father_index * 2) + 1 > (self._length - 1):
            return -1
        
        if (father_index * 2) + 2 > (self._length - 1):
            return (father_index * 2) + 1
        
        if self._heap[(father_index * 2) + 1] < self._heap[(father_index * 2) + 2]:
            return (father_index * 2) + 1
        else:
            return (father_index * 2) + 2
        
    def __repr__(self):
        return str(self._heap[:self._length])
    
    def __str__(self):
        return self.__repr__()

class HeapMax(baseheap):
    
    def __init__(self, L):
        self._heap = L
        self._length = len(L)
        self._heapify()
    
    def is_empty(self):
        """
        Returns True if heap is empty, otherwise False.
        
        is_empty() -> True/False
        
        @rtype: boolean
        @return: True if the heap is empty, otherwise False.
        """
        return self._length == 0
      
    def find_max(self):
        """
        Returns the maximum element into the heap.
        
        find_max() -> max_element
        
        @rtype: object
        @return: maximum element into the heap.
        """
        return None if self._length == 0 else self._heap[0]
        
    def delete_max(self):
        """
        Returns and deletes the maximum element into the heap.
        
        delete_max() -> max_element
        
        @rtype: object
        @return: maximum element into the heap.
        """
        if self._length == 0:
            return None
        max = self._heap[0]
        self._heap[0], self._heap[self._length - 1] = self._heap[self._length - 1], self._heap[0]
        self._length -= 1
        self._move_down(0) 
        return max
    
    def _heapify(self):
        self._recursive_heapify(0, self._length - 1)
        
    def _recursive_heapify(self, first, last):            
        if first > last:
            return
        self._recursive_heapify((2 * first) + 1, last) 
        self._recursive_heapify((2 * first) + 2, last) 
            
        self._move_down(first)
        
    def _move_down(self, father_index):
        son_index = self._max_son(father_index)
        while son_index != -1 and self._heap[son_index] > self._heap[father_index]:
            self._heap[son_index], self._heap[father_index] = self._heap[father_index], self._heap[son_index]
            father_index = son_index
            son_index = self._max_son(father_index)
            
    def _max_son(self, father_index):
        if (father_index * 2) + 1 > (self._length - 1):
            return -1
        
        if (father_index * 2) + 2 > (self._length - 1):
            return (father_index * 2) + 1
        
        if self._heap[(father_index * 2) + 1] > self._heap[(father_index * 2) + 2]:
            return (father_index * 2) + 1
        else:
            return (father_index * 2) + 2
        
    def __repr__(self):
        return str(self._heap[:self._length]) 
    
    def __str__(self):
        return self.__repr__()          
        
def __test(heap):
    """
    Heap Test.
    
    __test(heap) -> None
    
    @type heap: baseheap
    @param heap: heap instance.
    """    
    if not isinstance(heap, baseheap):
        raise TypeError("Expected type was Heap.")
    
    print "### iPATH TEST DATA STRUCTURE"
    print "### Data Type: Heap ({})".format(str(heap.__class__.__bases__[0].__name__))
    print "### Implementation: {}".format(str(heap.__class__.__name__))
    
    print "\n*** FIND/DELETE MIN/MAX ***\n"    
    if isinstance(heap, HeapMin):       
        print "delete_min: {}".format(str(heap.delete_min()))        
        print "find_min: {}".format(str(heap.find_min()))
        print "delete_min: {}".format(str(heap.delete_min()))       
        print "find_min: {}".format(str(heap.find_min()))
    elif isinstance(heap, HeapMax):      
        print "delete_max: {}".format(str(heap.delete_max()))        
        print "find_max: {}".format(str(heap.find_max()))
        print "delete_max: {}".format(str(heap.delete_max()))        
        print "find_max: {}".format(str(heap.find_max()))
        
    print "\n{}\n".format(str(heap))
    
    print "\n*** EMPTYING ***\n"    
    while not heap.is_empty():
        if isinstance(heap, HeapMin):
            heap.delete_min()
            print heap
        elif isinstance(heap, HeapMax):
            heap.delete_max()
            print heap
        
    print "\n### END OF TEST ###\n"

if __name__ == "__main__":
    L = [3, 2, 1, 7, 6, 5, 4, 10, 9, 8]
    heap = HeapMin(L)
    __test(heap)
    
    L = [3, 2, 1, 7, 6, 5, 4, 10, 9, 8]
    heap = HeapMax(L)
    __test(heap)