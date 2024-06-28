class Judge:
    def __init__(self, keeper):
        self.keeper = keeper
    def increase(self, teammate ,n):
        self.keeper.increase(n, teammate)