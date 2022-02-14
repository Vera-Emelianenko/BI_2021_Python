
class MySet(set):
    
    """a class that inherits from sets, contains only positive numbers when created and will not add non-positive values"""
    
    def __init__ (self, *args):
        # * args can contain several iterable items
        # first I create a list to contain alll the elements from those items
        self.modified_args = []
        # for every iterable item
        for arg in args:
            # for evety element
            for element in arg:
                # check that it is a number and if yes, that this number is positive
                if isinstance(element, (int, float)) and element > 0:
                    self.modified_args.append(element)
        # call _init_ of the parent, giving him the new list
        super().__init__(self.modified_args)
        
    # adds only positive elements
    def add(self, element):
        # again, checking that it is a number and if yes, that this number is positive
        if isinstance(element, (int, float)) and element > 0:
            # call add of the parent, giving him the new list
            super().add(element)