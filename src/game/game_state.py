class GameState:

    def __init__(self):
        self._rounds = 0
        self._state = {"Circles": 0,
                       "Wealth": 0,
                       "Mentality": 0}

    def __str__(self):
        str = "Rounds: {}\n".format(self._rounds)
        for k in list(self._state.keys()):
            str += "{}: {}\n".format(k, self._state[k])
        return str
