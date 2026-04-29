#Buy and sell stocks:
'''You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.'''
prices=[7,1,5,3,6,4]
n=len(prices)
res=0
for i in range(n-1):
    for j in range(i+1,n):
        #print(i,j)
        if prices[i]<prices[j]:
            ans=prices[j]-prices[i]
            res=max(res,ans)
print(res)
#optimal way:
prices=[7,1,5,3,6,4]
n=len(prices)
minval=prices[0]
ans=0
for i in range(n):
    ans=max(ans,prices[i]-minval)
    minval=min(prices[i],minval)
print(ans)