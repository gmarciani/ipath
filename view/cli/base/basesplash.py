DEFAULT_CONTENT = ["iPath",
                   "Giacomo Marciani",
                   "Python App for SP-Problem solving on real OSM Maps.",
                   "\'Remember to take the right path\'"]

DEFAULT_TEMPLATE = {"sym": ["#", "*"],
                    "margins": [3, 3, 15, 15]}

class basesplash:
    """
    Builds a frame splash customizable, adapting its size and its symbols respectively to the content and template specified. 
    It can be used for welcome messages or to highlight any information within a CLI.
    """      
    def __init__(self, content = DEFAULT_CONTENT, template = DEFAULT_TEMPLATE):
        self.content = content
        self.template = template 
    
    def __str__(self):              
        sym1 = self.template["sym"][0]
        sym2 = self.template["sym"][1]
        
        marginTop = self.template["margins"][0]
        marginBottom = self.template["margins"][1]
        marginLeft = self.template["margins"][2]
        marginRight = self.template["margins"][3]
        
        maxContentSize = max([len(c) for c in self.content]) 
        if maxContentSize % 2 != 0:
            maxContentSize = maxContentSize + 1        
        borderSize = 2 + marginLeft + maxContentSize + marginRight + 2
        
        ext = sym1 * borderSize
        ins = sym1 + (sym2 * (borderSize - 2)) + sym1
        latL = sym1 + sym2
        latR = sym2 + sym1
        empty = " "
        emptyLine = latL + (empty * (borderSize - 4)) + latR
        
        s = "\n"
        s += ext + "\n"
        s += ins + "\n"
        
        for i in range(marginTop):
            s += emptyLine + "\n"            
            
        for item in self.content:
            size = len(item)
            emptySizeLeft = marginLeft + ((maxContentSize - size) / 2)
            emptySizeRight = marginRight + ((maxContentSize - size) / 2)
            if size % 2 == 0:            
                s += latL + (empty * emptySizeLeft) + item + (empty * emptySizeRight) + latR + "\n" + emptyLine + "\n"
            else:
                s += latL + (empty * emptySizeLeft) + item + (empty * (emptySizeRight + 1)) + latR + "\n" + emptyLine + "\n"              
            
        for i in range(marginBottom - 1):
            s += emptyLine + "\n"
            
        s += ins + "\n"
        s += ext + "\n"
        s += "\n"       
        
        return s

def __test(splash):
    """
    Splash Test.
    """
    print "### iPATH TEST CLI COMPONENT"
    print "### Component: Splash"
    print "### Implementation: {}".format(str(splash.__class__.__name__))
    print "###"
    print "### Content: {}".format(splash.content)
    print "### Template: {}".format(splash.template)
    
    print "\n*** SPLASH ***\n"
    print splash
    
    print "\n### END OF TEST ###\n"

if __name__ == "__main__":
    splash = basesplash()
    __test(splash)