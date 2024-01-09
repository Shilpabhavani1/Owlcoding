def factorial(self, N):
        #code here
        fact=1
        p=[]
        for i in range(N,1,-1):
            fact=fact*i
        p.append(fact)
        return p
