#Interface Import
from model.base.baseunionfind import baseunionfind
#Support Data-Structures Import
from model.linkedlist import SimpleLinkedList as LinkedList    
    
class UnionFindNode:
    
    def __init__(self, element):
        self.element = element
        self._father = None
        self._sons = LinkedList()
        
    def __repr__(self):
        return "({})".format(str(self.element))
    
    def __str__(self):
        return self.__repr__()        

class QuickFind(baseunionfind):
    
    def makeset(self, element):
        """
        Creates a new Union-Find with the specified element.
        
        makeset(element) -> new_root
        
        @type element: object
        @param element: element to be added to the new Union-Find.
        
        @rtype: node
        @return: the new Union-Find's root node.
        """        
        rootNode = UnionFindNode(element)
        sonNode = UnionFindNode(element)
        rootNode._sons.add_as_last(sonNode)
        sonNode._father = rootNode
        return rootNode
    
    def union(self, rootNode1, rootNode2):
        """
        Builds and returns the union between the Union-Find corresponding to the specified element_A
        with the Union-Find corresponding to the specified element_B.
        
        union(root_node_A, root_node_B) -> updated_root_node_A
        
        @type root_node_A: node
        @param root_node_A: first Union-Find's root node
        @type root_node_B: node
        @param root_node_B: second Union-Find's root node.
        
        @rtype: node
        @return: the updated first Union-Find's root node.
        """
        curr2 = rootNode2._sons.get_first_record()
        while curr2 is not None:
            curr2.element._father = rootNode1
            curr2 = curr2._next
               
        last1 = rootNode1._sons.get_last_record()
        first2 = rootNode2._sons.get_first_record()
        last2 = rootNode2._sons.get_last_record()
        last1._next = first2
        rootNode1._sons._last = last2
        
        return rootNode1
    
    def find(self, node):
        """
        Returns the root node of the specified element.
        
        find(element) -> root_node
        
        @type element: object
        @param element: element whose root node will be returned.
        
        @rtype: node
        @return: root node.
        """
        return node._father.element

    def findRoot(self, node):
        """
        Returns the root node of the specified element.
        
        find(element) -> root_node
        
        @type element: object
        @param element: element whose root node will be returned.
        
        @rtype: node
        @return: root node.
        """
        return node._father    

class UnionFindBalancedNode(UnionFindNode):
    
    def __init__(self, element):
        UnionFindNode.__init__(self, element)
        self._size = 1         
        
class QuickFindBalanced(QuickFind, baseunionfind):
    
    def makeset(self, element):
        """
        Creates a new Union-Find with the specified element.
        
        makeset(element) -> new_root
        
        @type element: object
        @param element: element to be added to the new Union-Find.
        
        @rtype: node
        @return: the new Union-Find's root node.
        """
        rootNode = UnionFindBalancedNode(element)
        sonNode = UnionFindBalancedNode(element)
        rootNode._sons.add_as_last(sonNode)
        sonNode._father = rootNode
        return rootNode
    
    def union(self, rootNode1, rootNode2):  
        """
        Builds and returns the union between the Union-Find corresponding to the specified element_A
        with the Union-Find corresponding to the specified element_B.
        
        union(root_node_A, root_node_B) -> updated_root_node_A
        
        @type root_node_A: node
        @param root_node_A: first Union-Find's root node
        @type root_node_B: node
        @param root_node_B: second Union-Find's root node.
        
        @rtype: node
        @return: the updated first Union-Find's root node.
        """      
        if rootNode1._size >= rootNode2._size:
            curr2 = rootNode2._sons.get_first_record()
            while curr2 is not None:
                curr2.element._father = rootNode1
                curr2 = curr2._next
            last1 = rootNode1._sons.get_last_record()
            first2 = rootNode2._sons.get_first_record()
            last2 = rootNode2._sons.get_last_record()
            last1._next = first2
            rootNode1._sons._last = last2
            rootNode1._size += rootNode2._size            
            return rootNode1
        else:
            curr1 = rootNode1._sons.get_first_record()
            while curr1 != None:
                curr1.element._father = rootNode2
                curr1 = curr1._next
            last2 = rootNode2._sons.get_last_record()
            first1 = rootNode1._sons.get_first_record();
            last1 = rootNode1._sons.get_last_record();
            last2._next = first1
            rootNode2._sons._last = last1
            rootNode2._size += rootNode1._size            
            return rootNode2

class QuickUnion(baseunionfind):
    
    def makeset(self, element): 
        """
        Creates a new Union-Find with the specified element.
        
        makeset(element) -> new_root
        
        @type element: object
        @param element: element to be added to the new Union-Find.
        
        @rtype: node
        @return: the new Union-Find's root node.
        """
        node = UnionFindNode(element) 
        return node
    
    def union(self, rootNode1, rootNode2): 
        """
        Builds and returns the union between the Union-Find corresponding to the specified element_A
        with the Union-Find corresponding to the specified element_B.
        
        union(root_node_A, root_node_B) -> updated_root_node_A
        
        @type root_node_A: node
        @param root_node_A: first Union-Find's root node
        @type root_node_B: node
        @param root_node_B: second Union-Find's root node.
        
        @rtype: node
        @return: the updated first Union-Find's root node.
        """       
        rootNode2._father = rootNode1
        return rootNode1
    
    def find(self, node):
        """
        Returns the root node of the specified element.
        
        find(element) -> root_node
        
        @type element: object
        @param element: element whose root node will be returned.
        
        @rtype: node
        @return: root node.
        """
        rootNode = self.findRoot(node)
        return rootNode.element

    def findRoot(self, node):
        """
        Returns the root node of the specified element.
        
        find(element) -> root_node
        
        @type element: object
        @param element: element whose root node will be returned.
        
        @rtype: node
        @return: root node.
        """
        curr = node
        while curr._father is not None:
            curr = curr._father
        return curr   

class QuickUnionBalanced(QuickUnion, baseunionfind):
    
    def makeset(self, e):
        """
        Creates a new Union-Find with the specified element.
        
        makeset(element) -> new_root
        
        @type element: object
        @param element: element to be added to the new Union-Find.
        
        @rtype: node
        @return: the new Union-Find's root node.
        """
        return UnionFindBalancedNode(e)

    def union(self, rootNode1, rootNode2):
        """
        Builds and returns the union between the Union-Find corresponding to the specified element_A
        with the Union-Find corresponding to the specified element_B.
        
        union(root_node_A, root_node_B) -> updated_root_node_A
        
        @type root_node_A: node
        @param root_node_A: first Union-Find's root node
        @type root_node_B: node
        @param root_node_B: second Union-Find's root node.
        
        @rtype: node
        @return: the updated first Union-Find's root node.
        """
        r1 = rootNode1
        r2 = rootNode2
        if r1._size >= r2._size:
            r2._father = r1
            r1._size += r2._size
            return r1
        else:
            r1._father = r2
            r2._size += r1._size
            return r2

class QuickUnionCompressed(QuickUnionBalanced, baseunionfind):
    
    def findRoot(self, node):
        """
        Returns the root node of the specified element.
        
        find(element) -> root_node
        
        @type element: object
        @param element: element whose root node will be returned.
        
        @rtype: node
        @return: root node.
        """
        l = []
        curr = node
        
        while curr._father is not None:
            l.append(curr)
            curr = curr._father
        
        if l is not []:
            for n in l:
                n._father = curr
        
        return curr        

def __test(union_find):
    """
    Union-Find Test.
    
    __test(union_find) -> None
    
    @type union_find: baseunionfind
    @param union_find: union-find instance.    
    """     
    if not isinstance(union_find, baseunionfind):
        raise TypeError("Expected type was UnionFind.")
    
    print "### TEST DATA STRUCTURE"
    print "### Data Type: Union-Find ({})".format(str(union_find.__class__.__bases__[0].__name__))
    print "### Implementation: {}".format(union_find.__class__.__name__)
    
    nodes = []
    
    print "\n*** MAKESET ***\n"    
    if isinstance(union_find, (QuickFind, QuickFindBalanced)):
        for i in range(10):
            print "makeset({})".format(str(i))
            root = union_find.makeset(i)
            nodes.append(root._sons.get_first_record().element)
    elif isinstance(union_find, (QuickUnion, QuickUnionBalanced, QuickUnionCompressed)):
        for i in range(10):
            print "makeset({})".format(str(i))
            nodes.append(union_find.makeset(i))
            
    print "\n*** FIND ***\n"            
    if isinstance(union_find, QuickFind):
        for i in range(10):
            print "find({}) = {}\n".format(str(i), str(union_find.find(nodes[i])))        
    elif isinstance(union_find, QuickFindBalanced):
        for i in range(10):
            print "find({}) = {}\t father({}) = {}\n".format(i, union_find.find(nodes[i]), i, nodes[i]._father.element if nodes[i]._father is not None else "None")
    elif isinstance(union_find, (QuickUnion, QuickUnionBalanced, QuickUnionCompressed)):
        for i in range(10):
            print "find({}) = {}\t father({}) = {}\n".format(i, union_find.find(nodes[i]), i, nodes[i]._father.element if nodes[i]._father is not None else "None")
    
    print "\n*** UNION ***\n"    
    print "union(root(0), root(2))"
    union_find.union(union_find.findRoot(nodes[0]), union_find.findRoot(nodes[2]))
    print("union(root(8), root(4))")
    union_find.union(union_find.findRoot(nodes[8]), union_find.findRoot(nodes[4]))
    
    print "\n*** FIND ***\n"
    if isinstance(union_find, QuickFind):
        for i in range(10):
            print "find({}) = {}\n".format(str(i), str(union_find.find(nodes[i])))       
    elif isinstance(union_find, QuickFindBalanced):
        for i in range(10):
            print "find({}) = {}\t father({}) = {}\n".format(i, union_find.find(nodes[i]), i, nodes[i]._father.element if nodes[i]._father is not None else "None")
    elif isinstance(union_find, (QuickUnion, QuickUnionBalanced, QuickUnionCompressed)):
        for i in range(10):
            print "find({}) = {}\t father({}) = {}\n".format(i, union_find.find(nodes[i]), i, nodes[i]._father.element if nodes[i]._father is not None else "None")
       
    print "\n*** UNION ***\n"       
    print "union(root(0), root(8))"
    union_find.union(union_find.findRoot(nodes[0]), union_find.findRoot(nodes[8]))
    print("union(root(5), root(8))")
    union_find.union(union_find.findRoot(nodes[5]), union_find.findRoot(nodes[8]))
    
    print "\n*** FIND ***\n"    
    if isinstance(union_find, QuickFind):
        for i in range(10):
            print "find({}) = {}\n".format(str(i), str(union_find.find(nodes[i])))        
    elif isinstance(union_find, QuickFindBalanced):
        for i in range(10):
            print "find({}) = {}\t father({}) = {}\n".format(i, union_find.find(nodes[i]), i, nodes[i]._father.element if nodes[i]._father is not None else "None")
    elif isinstance(union_find, (QuickUnion, QuickUnionBalanced, QuickUnionCompressed)):
        for i in range(10):
            print "find({}) = {}\t father({}) = {}\n".format(i, union_find.find(nodes[i]), i, nodes[i]._father.element if nodes[i]._father is not None else "None")

    print "\n### END OF TEST ###\n"

if __name__ == "__main__":
    
    unionFind = QuickFind()
    __test(unionFind)
    
    unionFind = QuickFindBalanced()
    __test(unionFind)
    
    unionFind = QuickUnion()
    __test(unionFind)    
    
    unionFind = QuickUnionBalanced()
    __test(unionFind)
    
    unionFind = QuickUnionCompressed()
    __test(unionFind)