class basebinomialtree:
    """
    Binomial-Tree interface.
    
    def merge(other)    
    def get_sons()
    """
    
    def merge(self, other):
        """
        Merges two binomial trees.
        
        merge(other) -> binomial_tree
        
        @type other: basebinomialtree
        @param other: the binomial tree to be merged.
        """
        raise NotImplementedError("merge: You should have implemented this method!")
    
    def get_sons(self):
        """
        Returns sons list of binomial trees.
        
        get_sons() -> sons_list
        
        @rtype: list
        @return: sons list.
        """
        raise NotImplementedError("get_sons: You should have implemented this method!")