class Role(object):
    """
    An object to represent a role
    """
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

    """
    :class:`int`: Returns the id of the role
    """
    @property
    def id(self) -> int:
        return self._id

    """
    :class:`str`: Returns the name of the role
    """
    @property
    def name(self) -> str:
        return self._name

    """
    :class:`str`: Returns the hexadecimal color of the role
    """
    @property
    def color(self) -> str:
        return self._color
