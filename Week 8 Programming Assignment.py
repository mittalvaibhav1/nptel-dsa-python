n,k=map(int,input().split())
marks=[]
for i in range(n):
  marks.append(int(input()))

best = [[0 for i in range(k+1)] for j in range(n)]

best[0]=[marks[0]]*(k+1) 

for i in range(1,n):
  best[i][0] = max (best[i-1][0]+marks[i], 0)
  for j in range(1,k+1):  
    best[i][j] = max(best[i-1][j]+marks[i],best[i-1][j-1])
max=0
for i in range(n):
  if(max<best[i][k]):
    max=best[i][k]   
print(max)