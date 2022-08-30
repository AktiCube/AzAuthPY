class Role(object):
    def __init__(self, id, name, color):
        self._id = id
        self._name = name
        self._color = color
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f"Role(id={self.id}, name={self.name}, color={self.color})"
    
    def __eq__(self, __o):
        if isinstance(__o, Role):
            return self.id == __o.id
        return False

    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    @property
    def color(self):
        return self._color
