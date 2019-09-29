class Interface:
    """
    Interface Contract class
    """
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.validate()
        self.apply()
        
    def validate(self):
        """
        Validates data types
        """
        assert len(self.kwargs), "Atleast 1 parameter required, recieved 0"
        try:
            for key in self.kwargs:
                required_type = self.__class__.__dict__[key]
                value = self.kwargs[key]

                if not isinstance(value, required_type):
                    if value.__class__.__base__ != required_type.__base__:
                        self.kwargs[key] = required_type(**value)
                    else:
                        raise ValueError('Value of {} is {} where required type is {}' \
                                                 .format(key, type(value), required_type))
        except KeyError as err:
            raise ValueError('{} not present in {}'.format(err, type(self)))
    
    def apply(self):
        """
        Applies ops to data
        """
        class_variables = [key for key in self.__class__.__dict__.keys() if not key.startswith('_')]
        class_functions = {key.strip('_'): key for key in self.__class__.__dict__.keys() if key.startswith('_') 
                                                   and key.strip('_') in class_variables}
        
        # print (class_variables, class_functions, self.__class__.__dict__.keys())
        for key in class_functions:
            self.kwargs[key] = self.__class__.__dict__[class_functions[key]](self.kwargs[key])
        
        
    def serialize(self):
        """
        Serializes to JSON/dict format
        """
        for key in self.kwargs:
            if self.kwargs[key].__class__.__base__ == self.__class__.__base__:
                self.kwargs[key] = self.kwargs[key].serialize()
        return self.kwargs
