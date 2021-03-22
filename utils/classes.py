class ArgvCheck:
    def __init__(self, argument):
        self.argument = argument

    def check(self):
        if len(self) > 1:
            return self
        else:
            return
