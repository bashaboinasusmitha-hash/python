'''sets are the collection of distinct elements which means no duplicates are allowed
 and they are unordered and mutable.sets are represented with {}
 sets are based on hashing so the searching is very fast compare to lists,tuples.no indexing becauseorder is not maintained'''
s={1,2,3}
print(s)
#TC=add (O(1)),remove(O(1)),search(O(1)),union(O(1))
'''sets can contain "int","float","string","tuple" 
but not contain "list",dictionary",and another set because they are mutable'''
#types of sets:
#normal sets
s={1,4,2,"susmitha"}
print(s)
#Frozen sets:immutable version of set it is used when we need fixed set data
fs=frozenset([1,2,3])#cannot remove,add,update
#methods:
#add():add elements in set
s={1,2,6,"susmitha",True,3.2}
s.add(20)
s.add(3.2)
s.add(False)
print(s)
#remove():remove values it gives error if the value not in set
s={1,2,6,"susmitha",True,3.2}
s.remove(2)
s.remove("susmitha")#{1,6,3.2}
s.remove(True)#{6,3.2} here 1 is equal to True so 1 will removed and 0 treated as False
print(s)
#in sets True == 1 so at a time it will store two values 
#discard():remove elements but not give any error even if the element we want to remove is not in set
s={1,2,6,"susmitha",True,3.2}
s.discard(10)#{1,2,3,"susmitha",3.2}
s.discard(6)#{1,2,"susmitha",3.2}
print(s)
#clear(): clear the total set prints(set()) empty set
s={1,2,6,"susmitha",True,3.2}
s.clear()
print(s)
#pop():removes the random element
s={1,2,6,"susmitha",True,3.2}
s.pop()
print(s.pop())
print(s)
print(s.pop())
#adding tuples:
s={1,2,6,"susmitha",True,3.2}
s.add((4,8,3))
print(s)