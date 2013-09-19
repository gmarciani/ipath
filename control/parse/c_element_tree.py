#Parser Imports
from control.parse.base.baseparser import baseparser
from xml.etree.cElementTree import iterparse
from utils.singleton import singleton
#Graph Imports
from model.graph import GraphIncidenceSet as Graph
from utils.map_utils import geo_distance
#Support Data-Structres Imports
from sets import Set
#Source Management Imports
from os.path import isfile
from StringIO import StringIO
#Exception Import
from exception.exceptions import InvalidSourceError

@singleton
class cElementTreeParser(baseparser):
    """
    cElementTree Parser singleton, optimized for very huge OSM parsing.
    """    
    def __init__(self):
        self._source = None
        
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
            
    def _inflate_graph(self, nodes, adj_list):
        """
        Generates a Graph from the parsed data.
        
        _inflate_graph(nodes, adj_list) -> graph
        
        @type nodes: dictionary
        @param nodes: node coordinates indexed by node_id.
        @type adj_list: list of list
        @param adj_list: listed node_id. Every list is an adjacency list of nodes.
        
        @rtype: graph
        @return: graph inflated from parsed data.
        """
        graph = Graph()
        for node in nodes.iteritems(): 
            graph.add_node(node[1], node[0])
        for adj_nodes in adj_list:
            for i in range(len(adj_nodes) - 1):
                nodeAId = adj_nodes[i]
                nodeBId = adj_nodes[i + 1]
                coordA = nodes[nodeAId]
                coordB = nodes[nodeBId]
                info = geo_distance(coordA, coordB)
                graph.add_arc(nodeAId, nodeBId, info)
        return graph
        
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
        
        nodes = {}
        adj_list = Set()
        adj_nodes = []
        way = False
        
        context = iterparse(self._source, events = ("start", "end"))
        context = iter(context)
        event, root = context.next()
        
        for event, element in context:
            if event == "start" and element.tag == "way":
                way = True
                adj_nodes = []
                root.clear()
            elif event == "end" and element.tag == "node":                
                node_id = int(element.attrib["id"])
                node_latitude = float(element.attrib["lat"])
                node_longitude = float(element.attrib["lon"])                
                coords = [node_latitude, node_longitude]
                nodes[node_id] = coords
                root.clear()
            elif event == "end" and element.tag == "way":
                adj_list.add(tuple(adj_nodes))
                way = False
                root.clear()
            elif event == "end" and element.tag == "nd":
                if way:
                    adj_node_id = int(element.attrib["ref"])
                    adj_nodes.append(adj_node_id)
                root.clear()
        return self._inflate_graph(nodes, adj_list)                  
        
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
        
        nodes = {}
        adj_list = Set()
        adj_nodes = []
        way = False
        
        #Iterative parsing for very huge OSM parsing.
        context = iterparse(StringIO(self._source), events = ("start", "end"))
        context = iter(context)
        event, root = context.next()
        
        for event, element in context:
            if event == "start" and element.tag == "way":
                way = True
                adj_nodes = []
                root.clear()
            elif event == "end" and element.tag == "node":                
                node_id = int(element.attrib["id"])
                node_latitude = float(element.attrib["lat"])
                node_longitude = float(element.attrib["lon"])                
                coords = [node_latitude, node_longitude]
                nodes[node_id] = coords 
                root.clear()           
            elif event == "end" and element.tag == "way":
                adj_list.add(tuple(adj_nodes))
                way = False
                root.clear()
            elif event == "end" and element.tag == "nd":
                if way:
                    adj_node_id = int(element.attrib["ref"])
                    adj_nodes.append(adj_node_id)
                root.clear()
        return self._inflate_graph(nodes, adj_list)  
        
def __test(parser, source):
    """
    cElementTree Parser Test.
    
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
    parser = cElementTreeParser()
    __test(parser, TEST)