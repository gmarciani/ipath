#Splash Imports
from view.cli.base.basesplash import basesplash
from view.cli.base.basesplash import DEFAULT_CONTENT as DEFAULT_SPLASH_CONTENT
#Menu Imports
from view.cli.base.basemenu import basemenu
from view.cli.base.basemenu import DEFAULT_CONTENT as DEFAULT_MENU_CONTENT

class basepanel:
    """
    Builds a CLI panel, with its splash and / or its interactive menu.
    Every CLI panel should extends this class.
    """    
    def __init__(self, splash_content = DEFAULT_SPLASH_CONTENT, menu_content = DEFAULT_MENU_CONTENT):
        self.splash = basesplash(splash_content)
        self.menu = basemenu(menu_content)
        
    def show(self):
        """
        Shows splash, menu and listens for menu item selection.
        
        show() -> None
        """
        self.show_splash()
        self.show_menu()
        
    def show_splash(self):
        """
        Shows splash.
        
        show_splash() -> None
        """
        if self.splash is not None: print self.splash        
        
    def show_menu(self):
        """
        Shows menu and listen for menu item selection.
        
        show_menu -> None
        """
        if self.menu is not None: 
            print self.menu
            self.menu.listen()
        
def __test(panel):
    """
    Panel Test.
    """
    print "### TEST CLI COMPONENT"
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
    panel = basepanel()
    __test(panel)