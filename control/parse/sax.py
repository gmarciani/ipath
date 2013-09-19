#Parser Imports
from control.parse.base.baseparser import baseparser
import xml.sax.handler
from utils.singleton import singleton
#Graph Imports
from model.graph import GraphIncidenceSet as Graph
from utils.map_utils import geo_distance
#Source Management Imports
from os.path import isfile as isfile
import StringIO
#Exception Import
from exception.exceptions import InvalidSourceError

@singleton
class SaxParser(baseparser):
    """
    Sax Parser singleton, optimized for very huge OSM parsing.
    """    
    def __init__(self):
        self._source = None
        self._parser = xml.sax.make_parser()
        self._handler = None
        
    def _initialize_source_as_file(self, source):
        """
        Checks syntax and semantic of the specified source as file.
        
        _initialize_source_as_string(source) -> None
        
        @type source: string
        @param source: OSM file.        
        """
        if not isfile(source):
            raise InvalidSourceError()
        else:
            self._source = source
        
    def _initialize_source_as_string(self, source):
        """
        Checks syntax and semantic of the specified source as string.
        
        _initialize_source_as_string(source) -> None
        
        @type source: string
        @param source: OSM string.        
        """
        if not isinstance(source, basestring):
            raise InvalidSourceError()
        else:
            self._source = source    
        
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
        self._initialize_source_as_file(source)
        self._handler = SaxParserHandlerToGraph()
        self._parser.setContentHandler(self._handler)  
        self._parser.parse(self._source)
        return self._handler.get_graph()
        
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
        self._initialize_source_as_string(source)
        self._handler = SaxParserHandlerToGraph()
        self._parser.setContentHandler(self._handler)
        self._parser.parse(StringIO.StringIO(self._source))   
        return self._handler.get_graph()
        
class SaxParserHandlerToGraph(xml.sax.handler.ContentHandler):
    """
    Core Sax Handler for OSM parsing events.
    """    
    def __init__(self):
        self._way = False
        self._graph = Graph()
        self._adj_nodes = []
        self._node_id = None
        self._node_latitude = None
        self._node_longitude = None
        self._adj_node_id = None
        
    def startElement(self, name, attributes):
        if name == "node":
            self._node_id = int(attributes["id"])
            self._node_latitude = float(attributes["lat"])
            self._node_longitude = float(attributes["lon"])
        elif name == "way":
            self._way = True
        elif name == "nd" and self._way is True:
            self._adj_node_id = int(attributes["ref"])        
        
    def endElement(self, name):
        if name == "node":
            coords = [self._node_latitude, self._node_longitude]
            self._graph.add_node(coords, self._node_id)
        elif name == "way":
            self._way = False
            for i in range(len(self._adj_nodes) - 1):
                nodeAId = self._adj_nodes[i]
                nodeBId = self._adj_nodes[i + 1]
                coordA = self._graph.get_node_by_id(nodeAId).element
                coordB = self._graph.get_node_by_id(nodeBId).element
                info = geo_distance(coordA, coordB)
                self._graph.add_arc(nodeAId, nodeBId, info)
            self._adj_nodes = []
        elif name == "nd":
            self._adj_nodes.append(self._adj_node_id)
            
    def get_graph(self):
        return self._graph        
        
def __test(parser, source):
    """
    Sax Parser Test.
    
    __test(parser, source) -> None
    
    @type parser: parser
    @param parser: parser instance.
    @type source: string
    @param source: absolute file directory.
    """        
    if not isinstance(parser, baseparser):
        raise TypeError("Expected type was Parser.")
    
    print "### iPATH TEST PARSER"
    print "### Data Type: Parser ({})".format(str(parser.__class__.__bases__[0].__name__))
    print "### Implementation: {}".format(str(parser.__class__.__name__))
    
    print "\n*** PARSE FROM FILE ***\n"    
    print "Source (as file): {}".format(source) 
    print "Parsing from File to Graph . . . "
    graph = parser.parse_file(source)
    print "Parsed Graph Analysis"
    print "\tNodes: {}".format(str(graph.get_num_nodes()))
    print "\tArcs: {}".format(str(graph.get_num_arcs()))
    print "\tDeg: {} deg/node".format(str(average_node_deg(graph)))
    print "\tWeight: {} meters/arc".format(str(average_arc_weight(graph)))
    print "\tIsolation: {} %".format(str(isolation(graph))) 
    print "\tBlocking nodes: {} %".format(str(blocking_nodes(graph)))
    
    #print "\n*** GRAPH ***\n"      
    #print "\n{}\n".format(str(graph))
    
    print "\n*** PARSE FROM STRING ***\n"    
    print "Source (as string): {}".format(source)
    string = open(source).read()
    print "Parsing from String to Graph . . ."
    graph = parser.parse_string(string)
    print "Parsed Graph Analysis"
    print "\tNodes: {}".format(str(graph.get_num_nodes()))
    print "\tArcs: {}".format(str(graph.get_num_arcs()))
    print "\tDeg: {} deg/node".format(str(average_node_deg(graph)))
    print "\tWeight: {} meters/arc".format(str(average_arc_weight(graph)))
    print "\tIsolation: {} %".format(str(isolation(graph))) 
    print "\tBlocking nodes: {} %".format(str(blocking_nodes(graph)))
    
    #print "\n*** GRAPH ***\n"      
    #print "\n{}\n".format(str(graph)) 
    
    print "\n### END OF TEST ###\n"    
    
if __name__ == "__main__":
    #Test Imports
    from test.__init__ import TEST_SOURCE_REAL_ROME as TEST
    #Graph Analysis Imports
    from utils.map_utils import average_node_deg, average_arc_weight, isolation, blocking_nodes
    parser = SaxParser()
    __test(parser, TEST)