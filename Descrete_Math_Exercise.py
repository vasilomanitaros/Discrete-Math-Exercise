#Havel-Hakimi Theorem-Graph Realization Problem
print ("Enter the sequence of natural numbers\n(Use spacebar to seperate the entries and enter to finish the list): ")
lst= [int(x) for x in input().split()]

def func(listed):
    name=list(listed)
    k=False
    print("Sequence to check:"+ str(name))
    for x in range(len(name)):
        if (name[x]<0): 
            print("The sequence does not repsent a graph")
            return False
        if all([ k == 0 for k in name ]) :
            print("The sequence does represent a graph")
            return True
    name.sort(reverse=True)
    print("Sorted: "+ str(name))
    z=name.pop(0)
    if z>len(name):
        print("The sequence does not repsent a graph")
        return False
    for x in range(z):
        name[x]=name[x]-1
    return func(name)

if func(lst)==True:
    name=list(lst)
    neighborhood=[ [] for x in range(len(name)) ]
    adj=[[0]*len(name) for i in range(len(name))] #implementation of adjacency matrix
    for x in range(len(name)):
        while name[x]>0:
            k=0;it=0
            for y in range(x+1,len(name)):
                if name[y]>k and adj[x][y]==0:
                    k=name[y]
                    it=y
            adj[x][it]=1
            adj[it][x]=1
            name[it]=name[it]-1
            name[x]=name[x]-1
    arrnew=[] #list of neighborhood lists for each vertex
    for x in range(len(name)):
        neighborhood=[]
        for y in range(len(name)):
            if adj[x][y]==1:
                neighborhood.append(y+1)
        arrnew.append(neighborhood)
    for x in range(len(name)):
        print("N("+str(x+1)+")="+str(arrnew[x]))
