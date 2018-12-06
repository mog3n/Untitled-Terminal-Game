class GameState:

    def __init__(self, c, w, m):
        self._running = True
        # May have user picked state before game some how
        self._state = {"Rounds": 0,
                       "Circles": c,
                       "Wealth": w,
                       "Material": m,
                       "Mentality": None}
        self._factors = ["Circles", "Wealth", "Material"]
        self._calc_mentality()

    def __str__(self):
        str = " -- "
        for k in list(self._state.keys()):
            str += "{}: {} -- ".format(k, self._state[k])
        return str

    def isRunning(self):
        return self._running

    def stop(self):
        self._running = False

    def round(self):
        self._state["Rounds"] += 1

    def _calc_mentality(self):
        mental = 0
        for f in self._factors:
            x = self._state[f]
            # Quadratic in intercept form
            mental += (-3.7 * x * (x - 6))
        self._state["Mentality"] = mental
