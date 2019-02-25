import numpy as np
from matplotlib import pyplot as plt

if __name__ == '__main__':
    p1 = np.array([-1,1])
    p2 = np.array([1,-1])
    pat = [p1,p2]

    # generate J
    n = len(pat[0])
    J = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            if j == i:
                J[i,j] = 0
            else:
                J[i,j] = np.sum([p[i]*p[j]/float(n) for p in pat])
    print(J)
    
    # check if the patterns are fixed points
    print('Input: saved patterns')
    for p in pat:
        print(p,'=>',np.matmul(J,p.T)) 

    # use random patterns
    print('Input: random patterns')
    for _ in range(len(pat)):
        r = np.array([np.random.choice([-1,1]) for _ in range(n)])
        print(r,'=>',np.matmul(J,r.T))
        
    # retrieve pattern from random inputs -- won't do so, will oscillate
    print('Retrieving pattern')
    for _ in range(len(pat)):
        r = np.array([np.random.choice([-1,1]) for _ in range(n)])
        f = np.array(r)
        for _ in range(11):
            f = np.matmul(J,f.T)
            print(f)
        print(r,'=>',f)
