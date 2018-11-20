class Factor:

    def __init__(self):
        self._total = 0
        self._good = 0
        self._bad = 0

    def __str__(self):
        return "Exp: {} Pos: {} Neg: {}".format(self._total, self._good, self._bad)
