class GameState:

    def __init__(self):
        self._state = {"Rounds": 0,
                       "Circles": 0,
                       "Wealth": 0,
                       "Material": 0,
                       "Mentality": 0}

    def __str__(self):
        str = " -- "
        for k in list(self._state.keys()):
            str += "{}: {} -- ".format(k, self._state[k])
        return str
