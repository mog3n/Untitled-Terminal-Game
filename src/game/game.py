import pickle

def play(g):
    print(g)

    save = open("save.p", "wb+")
    pickle.dump(g, save)
    save.close()
