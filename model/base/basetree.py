class basetree:
    """
    Tree interface.
    
    get_root()
    insert(father_id, node_id)
    make_son(father_id, node_id)
    get_path_to(node_id)
    delete(node_id)
    dfs()
    bfs()
    """
        
    def get_root(self):
        """
        Returns the root's id.
        
        get_root() -> root_id
        
        @rtype: integer
        @return: root's id.
        """
        raise NotImplementedError("get_root: You should have implemented this method!")
    
    def insert(self, father_id, node_id):
        """
        Inserts the specified new node as son of the specified existent father inside the tree.
        
        insert(father_id, node_id) -> None
        
        @type father_id: integer
        @param father_id: already existent node's id inside tree.
        @type node_id: integer
        @param node_id: new node's id.
        """
        raise NotImplementedError("insert: You should have implemented this method!")
    
    def make_son(self, father_id, node_id):
        """
        Makes the specified node as son of the specified father inside the tree.
        
        make_son(father_id, node_id) -> None
        
        @type father_id: integer
        @param father_id: already existent node's id inside tree.
        @type node_id: integer
        @param node_id: already existent node's id.
        """
        raise NotImplementedError("make_son: You should have implemented this method!")
    
    def get_path_to(self, node_id):
        """
        Returns the path-as-list from the specified node to the root inside the tree.
        
        get_path_to(node_id) -> path_list
        
        @type node_id: integer
        @param node_id: already existent node's id.
        @rtype: list
        @return: path from the specified node to the root inside the tree.
        """
        raise NotImplementedError("get_path_to: You should have implemented this method!")
    
    def delete(self, node_id):
        """
        Deletes the specified node from the tree.
        
        delete(node_id) -> None
        
        @type node_id: integer
        @param node_id: existent node's id to be deleted from the tree.
        """
        raise NotImplementedError("_cut: You should have implemented this method!")
    
    def dfs(self):
        """
        Returns the LIFO path-as-list from the root to all other nodes inside tree. 
        
        dfs() -> reasearch_path
        
        @rtype: list
        @return: LIFO path-as-list from the root to all other nodes inside tree.
        """
        raise NotImplementedError("dfs: You should have implemented this method!")
    
    def bfs(self):
        """
        Returns the FIFO path-as-list from the root to all other nodes inside tree. 
        
        bfs() -> reasearch_path
        
        @rtype: list
        @return: FIFO path-as-list from the root to all other nodes inside tree.
        """
        raise NotImplementedError("bfs: You should have implemented this method!")