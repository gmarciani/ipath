class UnsupportedParserError(Exception): 
    """
    Exception raised when unsupported parser is specified.
    """
    def __init__(self, message):
        self.message = message

class UnsupportedDataStructureError(Exception): 
    """
    Exception raised when unsupported data structure is specified.
    """
    def __init__(self, message):
        self.message = message

class UnsupportedAlgorithmError(Exception): 
    """
    Exception raised when unsupported algorithm is specified.
    """
    def __init__(self, message):
        self.message = message

class InvalidParameterError(Exception): 
    """
    Exception raised when invalid parameter is specified.
    """
    def __init__(self, message):
        self.message = message

class InvalidSourceError(Exception): 
    """
    Exception raised when invalid source is specified.
    """
    def __init__(self, message):
        self.message = message

class BinomialTreeRankError(Exception): 
    """
    Exception raised when invalid merge operation is executed.
    """
    def __init__(self, message):
        self.message = message

class PriorityQueueInvalidKeyError(Exception): 
    """
    Exception raised when invalid decrease/increase key operation is executed.
    """
    def __init__(self, message):
        self.message = message  