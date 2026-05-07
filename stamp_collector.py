"""
Stamp Collector
A stamp collector is attempting to collect 4 different stamp types. 
If she is equally likely to find each type of stamp, 
what is the expected number of stamps that she would have to find 
in order to find three different unique stamp types?
"""

import numpy as np

class Collection:
    def __init__(self):
        self.owned = []
        self.total = [1, 2, 3, 4]

    def collect_one(self):
        found = np.random.choice(self.total, size=1, replace=True)[0]
        if found not in self.owned:
            self.owned.append(found)
        
    def evaluate_collection(self):
        if len(self.owned) == 3: 
            return True
        else:
            return False
        

N = 1000
n = 0

for _ in range(N):
    d = Collection()
    collection_complete = False
    while collection_complete == False:
        d.collect_one()
        n +=1
        collection_complete = d.evaluate_collection()

print(f"Collecting 3 out of 4 took E[N] = {n/N}")
