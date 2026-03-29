#Minimum cost of buying candies :
cost=[1,2,3]
cost.sort()
purchase=0
ans=0
n=len(cost)
for i in range(n-1,-1,-1):
    if purchase==2:
        purchase=0
    else:
        ans+=cost[i]
        purchase+=1
print(ans)
