#Panel Imports
from view.cli.base.basepanel import basepanel
from utils.singleton import singleton
#Core Functionalities Imports
from sys import exit
from control.parse.c_element_tree import cElementTreeParser as parser
from control.shortestpath.dijkstra_sc import dijkstra_sc_0, dijkstra_sc_1, dijkstra_sc_2, dijkstra_sc_3
from control.shortestpath.dijkstra_mc import dijkstra_mc_0, dijkstra_mc_1, dijkstra_mc_2, dijkstra_mc_3
#Test Imports
from utils.map_utils import isolation, blocking_nodes, average_node_deg, average_arc_weight
from test.__init__ import TEST_SOURCE_REAL_ROME
from output.__init__ import OUTPUT_DIR
from os.path import isdir, isfile
from time import clock

IPATH_DIJKSTRA_SC_0 = 0
IPATH_DIJKSTRA_SC_1 = 1
IPATH_DIJKSTRA_SC_2 = 2
IPATH_DIJKSTRA_SC_3 = 3
IPATH_DIJKSTRA_MC_0 = 4
IPATH_DIJKSTRA_MC_1 = 5
IPATH_DIJKSTRA_MC_2 = 6
IPATH_DIJKSTRA_MC_3 = 7

ALGORITHMS = [IPATH_DIJKSTRA_SC_0,
              IPATH_DIJKSTRA_SC_1,
              IPATH_DIJKSTRA_SC_2,
              IPATH_DIJKSTRA_SC_3,
              IPATH_DIJKSTRA_MC_0,
              IPATH_DIJKSTRA_MC_1,
              IPATH_DIJKSTRA_MC_2,
              IPATH_DIJKSTRA_MC_3]

ALGORITHMS_NAME = {IPATH_DIJKSTRA_SC_0: "Single-Coupling 0",
                   IPATH_DIJKSTRA_SC_1: "Single-Coupling 1",
                   IPATH_DIJKSTRA_SC_2: "Single-Coupling 2",
                   IPATH_DIJKSTRA_SC_3: "Single-Coupling 3",
                   IPATH_DIJKSTRA_MC_0: "Multiple-Coupling 0",
                   IPATH_DIJKSTRA_MC_1: "Multiple-Coupling 1",
                   IPATH_DIJKSTRA_MC_2: "Multiple-Coupling 2",
                   IPATH_DIJKSTRA_MC_3: "Multiple-Coupling 3"}

ALGORITHMS_FUNCTION = {IPATH_DIJKSTRA_SC_0: dijkstra_sc_0,
                       IPATH_DIJKSTRA_SC_1: dijkstra_sc_1,
                       IPATH_DIJKSTRA_SC_2: dijkstra_sc_2,
                       IPATH_DIJKSTRA_SC_3: dijkstra_sc_3,
                       IPATH_DIJKSTRA_MC_0: dijkstra_mc_0,
                       IPATH_DIJKSTRA_MC_1: dijkstra_mc_1,
                       IPATH_DIJKSTRA_MC_2: dijkstra_mc_2,
                       IPATH_DIJKSTRA_MC_3: dijkstra_mc_3}

DEFAULT_ALGORITHM = IPATH_DIJKSTRA_SC_2
    
def _quit():
    """
    Quits the whole program.
    
    _quit() -> None
    """
    exit()

def _compute_sp():
    algorithm = _get_algorithm()
    source = _get_source()
    num_nodes = _get_num_nodes()
    max_distance = _get_max_distance()
    output_dir = _get_output_dir()
    info = {"algorithm":algorithm, "source": source, "num_nodes": num_nodes, "max_distance": max_distance, "output_dir": output_dir}
    report = _get_report(info)
    print str(report)
    print "Parsing graph . . ."
    graph = parser().parse_file(source)
    print "Computig result . . ."
    start = clock()
    result = ALGORITHMS_FUNCTION[algorithm](graph, num_nodes, max_distance)
    end = clock()
    elapsed = end - start
    file_path = "{}/Result {} Nodes {} Distance {}.txt".format(str(output_dir), str(ALGORITHMS_NAME[algorithm]), str(num_nodes), str(max_distance))
    _store_result(graph, info, result, elapsed, file_path)
    try:
        from winsound import Beep
        Beep(2000, 700)
    except ImportError:
        pass
    PanelHome().show_menu()
    
def _get_algorithm():
    choices = []
    for algorithm in ALGORITHMS_NAME.iteritems():
        choices.append("{}) {}".format(str(algorithm[0]), str(algorithm[1])))
    choice = -1
    while not choice in ALGORITHMS:
        choice = str(raw_input("Algorithms:\n{}\nChoose your algorithm (blank for default): ".format("\n".join(choices))))
        if len(choice) == 0: choice = DEFAULT_ALGORITHM
        choice = int(choice)
        if choice not in ALGORITHMS: print "Oops! Invalid algorithm"
    return choice
        
def _get_source():
    choice = ""
    while not isfile(choice):
        choice = str(raw_input("Enter OSM source (blank for default): "))
        if len(choice) == 0: choice = TEST_SOURCE_REAL_ROME
        elif not isfile(choice): print "Oops! Invalid source"
    return choice
    
def _get_num_nodes():
    choice = None
    while True:
        try:
            choice = int(raw_input("Enter Number of Nodes: "))
        except ValueError:
            print "Oops! Invalid parameter"
            continue
        return choice    
    
def _get_max_distance():
    choice = None
    while True:
        try:
            choice = int(raw_input("Enter Max Distance: "))
        except ValueError:
            print "Oops! Invalid parameter"
            continue
        return choice
    
def _get_output_dir():
    choice = ""
    while not isdir(choice):
        choice = str(raw_input("Enter Output Directory (blank for default): "))
        if len(choice) == 0: choice = OUTPUT_DIR
        if not isdir(choice): print "Oops! Invalid directory"
    return choice

def _get_report(info):
    s = "\n### Report\n"
    s += "###\n"
    s += "### Algorithm: {}\n".format(str(ALGORITHMS_NAME[info["algorithm"]]))
    s += "### Source: {}\n".format(str(info["source"]))
    s += "### Num. Nodes: {}\n".format(str(info["num_nodes"]))
    s += "### Max. Distance: {}\n".format(str(info["max_distance"]))
    s += "### Output: {}\n".format(str(info["output_dir"]))
    return s
    
def _store_result(graph, info, result, elapsed, path):
    s = "### iPATH TEST RESULTS\n"
    s += "###\n"
    s += "### Algorithm: {}\n".format(str(ALGORITHMS_NAME[info["algorithm"]]))
    s += "###\n"
    s += "### Source: {}\n".format(str(info["source"]))
    s += "### Num. Nodes: {}\n".format(str(info["num_nodes"]))
    s += "### Max. Distance: {}\n".format(str(info["max_distance"]))
    s += "###\n"
    s += "### Nodes: {}\n".format(str(graph.get_num_nodes()))
    s += "### Arcs: {}\n".format(str(graph.get_num_arcs()))
    s += "### Av. Nodes Deg: {} deg/node\n".format(str(average_node_deg(graph)))
    s += "### Av. Arcs Weight: {} meters/arc\n".format(str(average_arc_weight(graph)))
    s += "### Isolation: {} %\n".format(str(isolation(graph)))
    s += "### Blocking Nodes: {}\n".format(str(blocking_nodes(graph)))
    s += "###\n"
    s += "###\n"
    s += "### Timing Result: {} seconds \n".format(str(elapsed))
        
    s += "\n\n*** RESULTS ***\n\n"
    s += str(result)
        
    s += "\n\n### END OF TEST ###\n"       
        
    file_stream = open(path, "w")
    file_stream.write(s)
    file_stream.close()

@singleton
class PanelHome(basepanel):
    """
    Builds a CLI panel for welcome message and main interactive menu.
    """
        
    def __init__(self):       
        splash_content = ["iPath",
                          "Giacomo Marciani",
                          "Python App for SP-Problem solving on real OSM Maps.",
                          "\'Remember to take the right path\'"]

        menu_content = [("1|Compute SP", _compute_sp), 
                        ("2|Quit", _quit)] 
        
        basepanel.__init__(self, splash_content, menu_content)      
        
def __test(panel):
    """
    Panel Test.
    """
    print "### iPATH TEST CLI COMPONENT"
    print "### Component: Panel"
    print "### Implementation: {}".format(str(panel.__class__.__name__))
    print "###"
    print "### Splash Content: {}".format(str(panel.splash.content))
    print "### Splash Template: {}".format(str(panel.splash.template))
    print "### Menu Content: {}".format(str(panel.menu.content))
    print "### Menu Content: {}".format(str(panel.menu.template))
    
    print "\n*** PANEL ***\n"
    panel.show()
    
    print "\n### END OF TEST ###\n"
    
if __name__ == "__main__":
    panel = PanelHome()
    __test(panel)            