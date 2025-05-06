import pickle
D={123456:['bill leee','444 main st',{'math':92,'english':23,'french':88}],56789:['Ann So','999 bway',{'math':98,'spanish':33,'english':78}]}

with open('studbase.dat','wb') as f:
    pickle.dump(D,f)
