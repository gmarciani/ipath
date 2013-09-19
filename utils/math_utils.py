def average(data_list):
    """
    Computes average value for a list of values.
    
    average(data_list) -> average
    
    @type data_list: list
    @param data_list: list of values to compute the average.
    @rtype: float
    @return: the floating-point average.
    """
    if data_list is None:
        return None    
    average = 0.0
    numItems = len(data_list)    
    for item in data_list:
        average += item 
    return float(average / numItems)

def __test(func, L):
    """
    Average Test.
    
    __test(func, L) -> None
    
    @type func: module function
    @param func: the average computation function.
    @type L: list
    @param L: list of values to compute the average.
    """
    print "### iPATH TEST MATH UTILS"
    print "### Type: Average Computation"
    print "### Implementation: {}".format(str(func.__name__))
    print "###"
    print "### Input: {}".format(L)
    
    print "\n*** RESULT ***\n"
    print "{}".format(str(func(L)))
    
    print "\n### END OF TEST ###\n"
    
if __name__ == "__main__":
    L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    __test(average, L)