#operations:
#union():"U" or "|"
s1={1,2,6,"susmitha",True,3.2}
s2={"rama",False,0,4,2,1}
print(s1|s2)
s3={2,5,10,8,3.9}
print(s1|s2|s3)
#intersection():
s={1,2,6,"susmitha",True,3.2}
s2={"rama",False,0,4,2,1}
print(s1.intersection(s2))
s3={5,10,8,3.9}
print(s1.intersection(s2,s3))#set() because no common elements in three sets
#difference()
s={1,2,6,"susmitha",True,3.2}
s2={"rama",False,0,4,2,1}
print(s1-s2)#{3.2, 'susmitha', 6}
print(s2-s1)#{False,4,"rama"}
s3={5,10,8,3.9}
print(s1-s2-s3)#{3.2,"susmitha",6}
#converting tuple set and performing union:
s1={"sushma","ravinder","ramadevi",1,2}
s2={"susmitha","tharun","chinnanna",2,1}
print(s1.union(("akshaya","ajay")))
#if we print like print(s1|("akshaya","ajay")) it will give error
#upadting a set
s1.update(s2)
print(s1)
s1.update(["suma","raju"])
print(s1)
#intersection():.intersection()
s1={"sushma","ravinder","ramadevi",1,2}
s2={"susmitha","tharun","chinnanna",2,1}
print(s1.intersection(s2))
print(s1 & s2)
print(s1.intersection(["ravinder","raksha"]))
#intersection update:
s1.intersection_update(s2)
print(s1)
s2.intersection_update(s1)
print(s2)#prints only common elements from s1 to s2
s2.intersection_update(["mohana"])
print(s2)#set() because mohana is not in s2
#operationss()
#isdisjoint():it prints False or True .checks whether in two or more sets that there are common elements
s1={"sushma","ravinder","ramadevi",1,2}
s2={"susmitha","tharun","chinnanna",2,1}
print(s1.isdisjoint(s2))#false because there is a common elements in both
print(s1.isdisjoint(["ravi","reshma"]))#prints True becoz there is no common elements
#issubset()
s1={"akhilesh","promod","pavan","mallika","keerthi"}
s2={"promod","mallika"}
print(s2.issubset(s1))#true beacuse every element in s2 has in s1
print(s1.issubset(s2))#false because not every element of s1 in s2
print(s1.issubset(["ramesh","likitha"]))#false
print(s1<=s2)#false
print(s2<=s1)#true ("<=")
#issuperset():(">=")
s1={"akhilesh","promod","pavan","mallika","keerthi"}
s2={"promod","mallika"}
print(s1.issuperset(s2))#true because every element on s2 has s1
print(s2.issuperset(s1))#false
print(s1>=s2)
#del()
s1={"akhilesh","promod","pavan","mallika","keerthi"}
del s1
#print(s1)#name error