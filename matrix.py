n11,m1=map(int,input().split())
l1=[]
ui1=0
for i1 in range(n11):
    l1.append(list(map(int,input().split())))   
for i1 in range(n11):
    for j1 in range(m1-1):
        for k1 in range(j1+1,m1+1):
            if l1[i1][j1:k1]==[1]*len(l1[i1][j1:k1]):
                 if all(l1[p+i1][j1:k1]==[1]*len(l1[p+i1][j1:k1]) for p in range(len(l1[i1][j1:k1])-1)):
                     if len(l1[i1][j1:k1])>ui1:
                        ui1=len(l1[i1][j1:k1])
if len(l1)==1 and len(l1[0])==1 and l1[0][0]==1:
    print(1)
for i in range(ui1):
    print(*[1]*ui1) 
