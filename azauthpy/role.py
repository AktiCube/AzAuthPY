class Role:
    def __init__(self, id, name, color):
        self.id = id
        self.name = name
        self.color = color
    
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
        return self.id
    
    @property
    def name(self):
        return self.name
    
    @property
    def color(self):
        return self.color
