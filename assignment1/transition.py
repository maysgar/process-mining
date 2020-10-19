class Transition:

    def __init__(self):
        self.id = 0  # Each of the states
        self.value = ""  # connects two states
        self.pre = []
        self.post = []
