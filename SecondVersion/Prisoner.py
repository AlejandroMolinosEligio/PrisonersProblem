## CLASS Prisoner

class Prisoner():

    def __init__(self, name: str, func):
        self.estrategy = func
        self.name = name