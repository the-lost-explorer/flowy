
class FlowContext:
    """
    A class to manage the context of a flow, including the current step and its parameters.
    """

    def __init__(self):
        self.vars = {}

    def set_var(self, key: str, value: any):
        """
        Set a variable in the context.
        """
        self.vars[key] = value
    
    def get_var(self, key: str):
        """
        Get a variable from the context.
        """
        return self.vars.get(key, None)
    
    def clear(self):
        """
        Clear the context.
        """
        self.vars = {}
