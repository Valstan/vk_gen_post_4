class ArgvCheck:

    def __init__(self):
        self.argument = None

    def get_argument(self):
        return self.argument

    def check(self, value):
        if len(value) > 1:
            self.argument = value

