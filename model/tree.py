#Interface Imports
from model.base.basetree import basetree
#Support Data-Structure Imports
from model.stack import StackLinkedList as Stack
from model.queue import QueueDeque as Queue

class RelationTree(basetree):
    
    def __init__(self, root_id):
        self._root_id = root_id
        self._relations = {root_id: None}
        
    def get_root(self):
        """
        Returns the root's id.
        
        get_root() -> root_id
        
        @rtype: integer
        @return: root's id.
        """
        return self._root_id
    
    def get_father(self, node_id):
        return self._relations[node_id]
        
    def insert(self, father_id, node_id):
        """
        Inserts the specified new node as son of the specified existent father inside the tree.
        
        insert(father_id, node_id) -> None
        
        @type father_id: integer
        @param father_id: already existent node's id inside tree.
        @type node_id: integer
        @param node_id: new node's id.
        """
        self._relations[node_id] = father_id
        
    def make_son(self, father_id, node_id):
        """
        Makes the specified node as son of the specified father inside the tree.
        
        make_son(father_id, node_id) -> None
        
        @type father_id: integer
        @param father_id: already existent node's id inside tree.
        @type node_id: integer
        @param node_id: already existent node's id.
        """
        self._relations[node_id] = father_id
            
    def get_path_to(self, node_id):
        """
        Returns the path-as-list from the specified node to the root inside the tree.
        
        get_path_to(node_id) -> path_list
        
        @type node_id: integer
        @param node_id: already existent node's id.
        @rtype: list
        @return: path from the specified node to the root inside the tree.
        """
        path = [node_id]
        father_id = self._relations[node_id]
        while father_id is not None:
            path.append(father_id)
            father_id = self._relations[father_id]
        return tuple(path[::-1])
    
    def delete(self, node_id):
        """
        Deletes the specified node from the tree.
        
        delete(node_id) -> None
        
        @type node_id: integer
        @param node_id: existent node's id to be deleted from the tree.
        """
        try:
            del self._relations[node_id]
        except KeyError:
            return
        for relation in self._relations.iteritems():
            if relation[1] == node_id:
                self.delete(relation[1])
    
    def dfs(self):
        """
        Returns the LIFO path-as-list from the root to all other nodes inside tree. 
        
        dfs() -> reasearch_path
        
        @rtype: list
        @return: LIFO path-as-list from the root to all other nodes inside tree.
        """
        res = []
        stack = Stack()
        if self._root_id is not None:
            stack.push(self._root_id)
        while not stack.is_empty():
            current_id = stack.pop()
            res.append(current_id)
            sons = self._get_sons(current_id)
            for son_id in sons:
                stack.push(son_id)
        return res
    
    def bfs(self):
        """
        Returns the FIFO path-as-list from the root to all other nodes inside tree. 
        
        bfs() -> reasearch_path
        
        @rtype: list
        @return: FIFO path-as-list from the root to all other nodes inside tree.
        """
        res = []
        queue = Queue()
        if self._root_id is not None:
            queue.enqueue(self._root_id)
        while not queue.is_empty():
            current_id = queue.dequeue()
            res.append(current_id)
            sons = self._get_sons(current_id)
            for son_id in sons:
                queue.enqueue(son_id)
        return res
    
    def _get_sons(self, node_id):
        sons = []
        for relation in self._relations.iteritems():
            if relation[1] == node_id: sons.append(relation[0])
        return sons
    
    def __repr__(self):
        s = ""
        bfs = self.bfs()
        for node_id in bfs:
            s += "{}: {} | {}\n".format(str(node_id), str(self._relations[node_id]), str(self._get_sons(node_id))) 
        return s
    
    def __str__(self):
        return self.__repr__()  

class DictTree(basetree):
    
    def __init__(self, root_id):
        self._root_id = root_id
        self._tree = {root_id: [None, []]}
        
    def get_root(self):
        """
        Returns the root's id.
        
        get_root() -> root_id
        
        @rtype: integer
        @return: root's id.
        """
        return self._root_id
    
    def get_father(self, node_id):
        return self._tree[node_id][0]
        
    def insert(self, father_id, node_id):
        """
        Inserts the specified new node as son of the specified existent father inside the tree.
        
        insert(father_id, node_id) -> None
        
        @type father_id: integer
        @param father_id: already existent node's id inside tree.
        @type node_id: integer
        @param node_id: new node's id.
        """
        self._tree[node_id] = [father_id, []]
        self._tree[father_id][1].append(node_id)        
        
    def make_son(self, father_id, node_id):
        """
        Makes the specified node as son of the specified father inside the tree.
        
        make_son(father_id, node_id) -> None
        
        @type father_id: integer
        @param father_id: already existent node's id inside tree.
        @type node_id: integer
        @param node_id: already existent node's id.
        """
        try:     
            if self._tree[node_id][0] is not None:
                self._cut(node_id)       
            self._tree[node_id][0] = father_id    
        except KeyError:
            return        
        self._tree[father_id][1].append(node_id)    
        
    def get_path_to(self, node_id):
        """
        Returns the path-as-list from the specified node to the root inside the tree.
        
        get_path_to(node_id) -> path_list
        
        @type node_id: integer
        @param node_id: already existent node's id.
        @rtype: list
        @return: path from the specified node to the root inside the tree.
        """
        path = [node_id]
        father_id = self._tree[node_id][0]
        while father_id is not None:
            path.append(father_id)
            father_id = self._tree[father_id][0]
        return tuple(path[::-1])
        
    def delete(self, node_id):
        """
        Deletes the specified node from the tree.
        
        delete(node_id) -> None
        
        @type node_id: integer
        @param node_id: existent node's id to be deleted from the tree.
        """
        father_id = self._tree[node_id][0]
        self._tree[father_id][1].remove(node_id)
        for son_id in self._tree[node_id][1]:
            del self._tree[son_id]
        del self._tree[node_id]    
        
    def dfs(self):
        """
        Returns the LIFO path-as-list from the root to all other nodes inside tree. 
        
        dfs() -> reasearch_path
        
        @rtype: list
        @return: LIFO path-as-list from the root to all other nodes inside tree.
        """
        res = []
        stack = Stack()
        if self._root_id is not None:
            stack.push(self._root_id)
        while not stack.is_empty():
            current_id = stack.pop()
            res.append(current_id)
            sons = sorted(self._tree[current_id][1])
            for son_id in sons:
                stack.push(son_id)
        return res
    
    def bfs(self):
        """
        Returns the FIFO path-as-list from the root to all other nodes inside tree. 
        
        bfs() -> reasearch_path
        
        @rtype: list
        @return: FIFO path-as-list from the root to all other nodes inside tree.
        """
        res = []
        queue = Queue()
        if self._root_id is not None:
            queue.enqueue(self._root_id)
        while not queue.is_empty():
            current_id = queue.dequeue()
            res.append(current_id)
            sons = sorted(self._tree[current_id][1])
            for son_id in sons:
                queue.enqueue(son_id)
        return res
    
    def _cut(self, node_id):
        father_id = self._tree[node_id][0]
        self._tree[father_id][1].remove(node_id)
        self._tree[node_id][0] = None
        
    def __repr__(self):
        s = ""        
        for item in self._tree.iteritems():
            s += "{}: {} | {}\n".format(str(item[0]), str(item[1][0]), str(item[1][1]))            
        return s
    
    def __str__(self):
        return self.__repr__()   
    
class TreeArrayList(basetree):
    
    class Node:
        
        def __init__(self, node_id, father_id = None):
            self._id = node_id
            self._father_id = father_id
            self._sons = []
            
        def __repr__(self):
            return "{}: {} | {}\n".format(str(self._id), str(self._father_id), str(self._sons))
        
        def __str__(self):
            return self.__repr__()
        
    def __init__(self, root_id):
        self._root_id = root_id
        self._nodes = {root_id: TreeArrayList.Node(root_id)}   
        
    def get_root(self):
        """
        Returns the root's id.
        
        get_root() -> root_id
        
        @rtype: integer
        @return: root's id.
        """
        return self._root_id     
        
    def insert(self, father_id, node_id):
        """
        Inserts the specified new node as son of the specified existent father inside the tree.
        
        insert(father_id, node_id) -> None
        
        @type father_id: integer
        @param father_id: already existent node's id inside tree.
        @type node_id: integer
        @param node_id: new node's id.
        """
        self._nodes[father_id]._sons.append(node_id)
        self._nodes[node_id] = TreeArrayList.Node(node_id, father_id)
        
    def make_son(self, father_id, node_id):
        """
        Makes the specified node as son of the specified father inside the tree.
        
        make_son(father_id, node_id) -> None
        
        @type father_id: integer
        @param father_id: already existent node's id inside tree.
        @type node_id: integer
        @param node_id: already existent node's id.
        """
        try:
            prev_father_id = self._nodes[node_id]._father_id
            self._nodes[prev_father_id]._sons.remove(node_id)
            self._nodes[father_id]._sons.append(node_id)
            self._nodes[node_id]._father_id = father_id
        except ValueError, KeyError:
            return
        
    def get_path_to(self, node_id):
        """
        Returns the path-as-list from the specified node to the root inside the tree.
        
        get_path_to(node_id) -> path_list
        
        @type node_id: integer
        @param node_id: already existent node's id.
        @rtype: list
        @return: path from the specified node to the root inside the tree.
        """
        path = [node_id]
        father_id = self._nodes[node_id]._father_id
        while father_id is not None:
            path.append(father_id)
            father_id = self._nodes[father_id]._father_id
        return tuple(path[::-1])
        
    def delete(self, node_id):
        """
        Deletes the specified node from the tree.
        
        delete(node_id) -> None
        
        @type node_id: integer
        @param node_id: existent node's id to be deleted from the tree.
        """
        node = self._nodes[node_id]        
        father_id = self._nodes[node_id]._father_id
        self._nodes[father_id]._sons.remove(node_id)
        for son_id in node._sons:
            self.delete(son_id)
        del self._nodes[node_id]
            
    def dfs(self):
        """
        Returns the LIFO path-as-list from the root to all other nodes inside tree. 
        
        dfs() -> reasearch_path
        
        @rtype: list
        @return: LIFO path-as-list from the root to all other nodes inside tree.
        """
        res = []
        stack = Stack()
        if self._root_id is not None:
            stack.push(self._root_id)
        while not stack.is_empty():
            current_id = stack.pop()
            res.append(current_id)
            sons = self._nodes[current_id]._sons
            for son_id in sons:
                stack.push(son_id)
        return res
    
    def bfs(self):
        """
        Returns the FIFO path-as-list from the root to all other nodes inside tree. 
        
        bfs() -> reasearch_path
        
        @rtype: list
        @return: FIFO path-as-list from the root to all other nodes inside tree.
        """
        res = []
        queue = Queue()
        if self._root_id is not None:
            queue.enqueue(self._root_id)
        while not queue.is_empty():
            current_id = queue.dequeue()
            res.append(current_id)
            sons = self._nodes[current_id]._sons
            for son_id in sons:
                queue.enqueue(son_id)
        return res
    
    def __repr__(self):
        s = ""
        for node in self._nodes.itervalues():
            s += str(node)
        return s
        
    def __str__(self):
        return self.__repr__()           
    
def __test(tree):
    """
    Tree Test.
    
    __test(tree) -> None
    
    @type tree: basetree
    @param tree: tree instance.
    """    
    if not isinstance(tree, basetree):
        raise TypeError("Expected type was Tree.")
    
    print "### iPATH TEST DATA STRUCTURE"
    print "### Data Type: Tree ({})".format(str(tree.__class__.__bases__[0].__name__))
    print "### Implementation: {}".format(str(tree.__class__.__name__))
    
    print "\n*** INSERT ***\n"    
    for i in range(1, 5):
        print "insert(0, {})".format(i)
        tree.insert(0, i)
        
    for i in range(5, 10):
        print "insert({}, {})".format(i - 4, i)
        tree.insert(i - 4, i)
    
    print "\n{}\n".format(str(tree)) 
    
    print "\n*** MAKE SON ***\n"    
    for i in range(8, 10):
        print "make_son({}, {})".format(1, i)
        tree.make_son(1, i)
        
    print "\n*** PATH TO ***\n"
    
    for i in range(10):
        print "get_path_to({}): {}\n".format(str(i), str(tree.get_path_to(i)))
    
    print "\n{}\n".format(str(tree)) 
    
    print "\n*** RESEARCH: DFS ***\n"
    print tree.dfs()
    
    print "\n*** RESEARCH: BFS ***\n"
    print tree.bfs()

    print "\n{}\n".format(str(tree))  
    
    print "\n*** DELETE ***\n"    
    print "delete(3)"
    tree.delete(3)
    
    print "\n{}\n".format(str(tree))  
    
    print "\n### END OF TEST ###\n"  

if __name__ == "__main__":    
    tree = RelationTree(0)
    __test(tree)
    tree = DictTree(0)
    __test(tree)
    tree = TreeArrayList(0)
    __test(tree)
