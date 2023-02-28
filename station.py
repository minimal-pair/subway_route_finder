class Station:
    def __init__(self, name, lines):
        self.name = name
        self.neighbors = []
        self.lines = lines
        self.parent = ""
