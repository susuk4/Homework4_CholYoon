def numb_theory(a,b):
    I = IntegerRange(1,Infinity,1)
    N = []
    PrimeList = []
    for i in iter(I):
        N.append(i^2+a*i+b)
    P = Prime()
    for pr in P:
        if pr in N:
            PrimeList.append(pr)
    len(PrimeList)
