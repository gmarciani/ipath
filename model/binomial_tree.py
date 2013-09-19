#Interface Import
from model.base.basebinomialtree import basebinomialtree
#Support Data-Structures Imports
from model.linkedlist import SimpleLinkedList as LinkedList
from model.queue import QueueDeque as Queue
#Exception Import
from exception.exceptions import BinomialTreeRankError

class BinomialTree(basebinomialtree):
    
    class Node:
    
        def __init__(self, element, key):
            self.element = element
            self._key = key
            self._rank = 0
            self._father = None
            self._sons = LinkedList()       

        def _swap(self, other):
            self.element, other.element = other.element, self.element
            self._key, other._key = other._key, self._key

        def _add_son(self, son):
            son._father = self
            self._sons.add_as_last(son)
        
        def __repr__(self):
            return "*B{}({}, {})".format(str(self._rank), str(self.element), str(self._key))
    
        def __str__(self):
            return self.__repr__()
    
    def __init__(self, element, key):
        self._root = BinomialTree.Node(element, key)

    def merge(self, other):
        """
        Merges two binomial trees.
        
        merge(other) -> binomial_tree
        
        @type other: basebinomialtree
        @param other: the binomial tree to be merged.
        """
        if self._root._rank != other._root._rank:
            raise BinomialTreeRankError()
        
        this_root = self._root
        other_root = other._root
        
        if this_root._key <= other_root._key:
            other_root._father = this_root
            this_root._add_son(other_root)
            self._root._rank += 1
            return self
        else:
            this_root._father = other_root
            other_root._add_son(this_root)
            other._root._rank += 1
            return other        

    def get_sons(self):
        """
        Returns sons list of binomial trees.
        
        get_sons() -> sons_list
        
        @rtype: list
        @return: sons list.
        """
        res = LinkedList()
        curr = self._root._sons.get_first_record()
        while curr is not None:
            nTree = BinomialTree(None, None)
            nTree._root = curr.element
            nTree._root._father = None
            res.add_as_last(nTree)
            curr = curr._next
        return res
    
    def __repr__(self):
        queue = Queue()
        queue.enqueue(self._root)
        queue.enqueue(None)
        s = "{"
        while not queue.is_empty():
            currNode = queue.dequeue()
            if currNode is not None:
                s += str(currNode)
                if not currNode._sons.is_empty():
                    recordSon = currNode._sons.get_first_record()
                    while recordSon is not None:
                        queue.enqueue(recordSon.element)
                        recordSon = recordSon._next
                    queue.enqueue(None)
            else:
                s += "\n"
        s += "}"
        return s       
        
    def __str__(self):
        return self.__repr__()    

def __test(binomial_tree):
    """
    Binomial-Tree Test.
    
    __test(binomial_tree) -> None
    
    @type binomial_tree: basebinomialtree
    @param binomial_tree: binomial-tree istance.
    """
    print "### iPATH TEST DATA STRUCTURE"
    print "### Data Type: Binomial Tree ({})".format(str(binomial_tree.__class__.__bases__[0].__name__))
    print "### Implementation: {}".format(str(binomial_tree.__class__.__name__))
    
    bTreeList = [binomial_tree]
    
    for i in range(3):
        print "BinomialTree({}, {})".format(str(i), str(float(i)))
        bTree = BinomialTree(i, float(i))
        bTreeList.append(bTree)
        
    for bTree in bTreeList:
        print "#{}:\t\n{}\n".format(str(bTreeList.index(bTree)), str(bTree))
        
    print "\n*** MERGE ***\n"       
    for i in range(0, 4, 2):
        print "{}.merge({})".format(str(i), str(i + 1), str())
        bTreeList[i].merge(bTreeList[i + 1])
        
    for bTree in bTreeList:
        print "#{}:\t\n{}\n".format(str(bTreeList.index(bTree)), str(bTree))
        
    print "\n*** MERGE ***\n"        
    for i in range(0, 2, 1):
        print "{}.merge({})".format(str(i), str(i + 2), str())
        bTreeList[i].merge(bTreeList[i + 2])
        
    for bTree in bTreeList:
        print "#{}:\t\n{}\n".format(str(bTreeList.index(bTree)), str(bTree))
        
    print "\n### END OF TEST ###\n"    
    
if __name__ == "__main__":
    binomial_tree = BinomialTree(0, 0.0)
    __test(binomial_tree)