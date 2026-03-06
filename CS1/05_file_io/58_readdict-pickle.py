import pickle
with open('studbase.dat','rb') as f:
    D=pickle.load(f)
    print(D)
