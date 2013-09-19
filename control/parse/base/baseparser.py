class baseparser:
    """
    Parser interface.
    """
    
    def parse_file(self, source):
        """
        Parses a Graph from an OSM file. 
        This is the preferred way for parsing when on execution mode.
        
        parse_file(source) -> graph
        
        @type source: string
        @param source: OSM file absolute path.
        
        @rtype: graph
        @return: parsed graph.
        """
        raise NotImplementedError("parse_file: You should have implemented this method!")
    
    def parse_string(self, source):
        """
        Parses a Graph from an OSM string. 
        This is the preferred way for parsing when on profiling mode.
        
        parse_string(source) -> graph
        
        @type source: string
        @param source: OSM string
        
        @rtype: graph
        @return: parsed graph.
        """
        raise NotImplementedError("parse_string: You should have implemented this method!")