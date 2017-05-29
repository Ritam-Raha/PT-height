from math import inf
H={}
I={}

def alph(w):
    return set(w)

def nocc(x,i,w):
    n = len(w)
    if x in alph(w):
        if i==n:
            return inf
        elif i<n and x == w[i]:
            return(i+1)
        elif i<n and x != w[i]:
            return nocc(x,i+1,w)

def noccrow(x,w):
    n=len(w)
    t={}
    if x in alph(w):
        t[x]=[]
        for i in range(0,n+1):
            t[x].append(nocc(x,i,w))
        return t[x]
def nocctable(w):
    d={}
    for x in alph(w):
        d[x]=noccrow(x,w)
    for i in d.keys():
        print(i,d[i])

def sld(x,i,w):
    j= H[x][i]
    m=[]
    if j==inf:
        return 1
    if j!= inf:
        for y in alph(w):
            if H[y][i]<= j:
                m.append(sld(y,j,w))
        return 1+min(m)
def sldrow(x,w):
    for p in alph(w):
        H[p]=noccrow(p,w)
    n=len(w)
    t={}
    if x in alph(w):
        t[x]=[]
        for i in range(0,n+1):
            t[x].append(sld(x,i,w))
        return t[x]
def sldtable(w):
    d={}
    for x in alph(w):
        d[x]=sldrow(x,w)
    for i in d.keys():
        print(i,d[i])
                
def locc(x,i,w):
    n = len(w)
    if x in alph(w):
        if i==1:
            return -(inf)
        elif i>0 and x == w[i-2]:
             return(i-1)
        elif i>0 and x != w[i-2]:
            return locc(x,i-1,w)

def loccrow(x,w):
    n=len(w)
    t={}
    if x in alph(w):
        t[x]=[]
        for i in range(1,n+2):
            t[x].append(locc(x,i,w))
        return t[x]
def locctable(w):
    d={}
    for x in alph(w):
        d[x]=loccrow(x,w)
    for i in d.keys():
        print(i,d[i])

def srd(x,i,w):
    j= I[x][i-1]
    l=[]
    if j== -(inf):
        return 1
    if j!= -(inf):
        for y in alph(w):
            if I[y][i-1]>= j:
                l.append(srd(y,j,w))
        return 1 + min(l)

def srdrow(x,w):
    for p in alph(w):
        I[p]=loccrow(p,w)
    n=len(w)
    t={}
    if x in alph(w):
        t[x]=[]
        for i in range(1,n+2):
            t[x].append(srd(x,i,w))
        return t[x]
def srdtable(w):
    d={}
    for x in alph(w):
        d[x]=srdrow(x,w)
    for i in d.keys():
        print(i,d[i])

def h(w):
    p=0
    m=(0,0,0)
    sldt={}
    for x in alph(w):
        sldt[x]=sldrow(x,w)
    srdt={}
    for x in alph(w):
        srdt[x]=srdrow(x,w)
    n=len(w)
    for i in range(0,n+1):
        if (srdt[x][i]+sldt[x][i]-1)>p:
            p=(srdt[x][i]+sldt[x][i]-1)
    return (p)
    
'''if __name__ == "__main__":
        while True:
            print(h(input()))'''

                
                


