import sys

DEFAULT_CONTENT = [("1 | MenuItem1", sys.exit),
                   ("2 | MenuItem2", sys.exit)]

DEFAULT_TEMPLATE = {"sym": "#", 
                    "margins": [1, 1, 3, 3]}

class basemenu:
    """
    Builds a framed customizable menu, which adapts its functions, dimensions and its symbols respectively to the content and template specified. 
    It can be used to build up any interactive CLI menu.
    """    
    def __init__(self, content = DEFAULT_CONTENT, template = DEFAULT_TEMPLATE):
        self.content = content
        self.template = template      
    
    def __str__(self):
        sym = self.template["sym"]
        
        marginTop = self.template["margins"][0]
        marginBottom = self.template["margins"][1]
        marginLeft = self.template["margins"][2]
        marginRight = self.template["margins"][3]
        
        numItems = len(self.content)
        maxContentSize = max([len(c[0]) for c in self.content]) 
        if maxContentSize % 2 != 0:
            maxContentSize = maxContentSize + 1   
        borderSize = 1 + (marginLeft + maxContentSize + marginRight + 1) * numItems
        
        ext = sym * borderSize
        latL = sym
        latR = sym
        empty = " "
        emptyLine = latL + (empty * (marginLeft + maxContentSize + marginRight) + latR) * numItems
        
        s = "\n"
        s += ext + "\n"
        
        for i in range(marginTop):
            s += emptyLine + "\n"
            
        s += latL
            
        for item in self.content:
            size = len(item[0])
            emptySizeLeft = marginLeft + ((maxContentSize - size) / 2)
            emptySizeRight = marginRight + ((maxContentSize - size) / 2)
            if size % 2 == 0:            
                s += (empty * emptySizeLeft) + item[0] + (empty * emptySizeRight) + latR
            else:
                s += (empty * emptySizeLeft) + item[0] + (empty * (emptySizeRight + 1)) + latR
                
        s += "\n"                         
            
        for i in range(marginBottom):
            s += emptyLine + "\n"
            
        s += ext + "\n"
        s += "\n"       
        
        return s           
        
    def listen(self):
        """
        Intercepts the menu item selection, and performs the associated function.
        """
        choice = None
        
        while choice == None or choice > len(self.content):
            choice = int(raw_input("Enter a choice: "))        
            if choice <= len(self.content):
                self.content[choice - 1][1]()
            else:
                print "Oops! Invalid choice"

def __test(menu):
    """
    Menu Test.
    """
    def f1():
        print "f1"
        
    def f2():
        print "f2"
        
    def f3():
        print "f3" 
        
    def f4():
        print "f4"
        
    def f5():
        print "f5" 
    
    content = [("1| File", f1),                
               ("2| Edit", f2), 
               ("3| Source", f3),
               ("4| Project", f4), 
               ("5| Run", f5)]
    
    menu.content = content
    
    print "### TEST CLI COMPONENT"
    print "### Component: Menu"
    print "### Implementation: {}".format(str(menu.__class__.__name__))
    print "###"
    print "### Content: {}".format(menu.content)
    print "### Template: {}".format(menu.template)
    
    print "\n*** MENU ***\n"
    print menu
    menu.listen()
    
    print "\n### END OF TEST ###\n"

if __name__ == "__main__":
    menu = basemenu()
    __test(menu)