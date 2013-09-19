def singleton(my_class):
    """
    Class Descriptor that realizes the Singleton Pattern.
    """
    instances = {}
    def get_instance():
        if my_class not in instances:
            instances[my_class] = my_class()
        return instances[my_class]
    return get_instance

def __test(descriptor):
    """
    Singleton Class Descripto Test.
    
    __test(descriptor) -> None
    
    @type descriptor: class descriptor
    @param descriptor: the class descriptor instance that realizes the singleton pattern.
    """
    @descriptor
    class Foo:
        def __init__(self, attribute = 2):
            self.attribute = attribute
    
    print "### iPATH TEST SINGLETON"
    print "### Type: Singleton Class Descriptor"
    print "### Implementation: {}".format(str(descriptor.__name__))
    
    print "\n*** SINGLETON FOO ***\n"
    
    print "@descriptor"
    print "class Foo:"
    print "\tdef __init__(self, attribute = 2):"
    print "\t\tself.attribute = attribute\n"
    
    print "my_class_1 = Foo()"
    my_class_1 = Foo()
    print "my_class_1.attribute: {}".format(str(my_class_1.attribute))
    print "my_class_1.attribute = 10".format(str(my_class_1.attribute))
    my_class_1.attribute = 10
    print "my_class_2 = Foo()"
    my_class_2 = Foo()
    print "my_class_2.attribute: {}".format(str(my_class_2.attribute))
    
    print "\n### END OF TEST ###\n"
    
if __name__ == "__main__":
    __test(singleton)