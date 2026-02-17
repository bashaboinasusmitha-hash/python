'''membership operators are: "in","not in"
membership operators checks whether the value exists inside a sequence
it works with different datatypes list,tuple,string,dictionary,sets'''
#for list data types:
li=[2,4,1,7,3,9]
print(2 in li)
print(8 in li)
print(1 not in li)
#strings:
print("for string datatype:")
print("in strings "in"checks for continous substring,not just presence of letters.")
print("the length of  substring must be equal or lessthan the string and it is case sensitive.")
string="susmitha"
print("su" in string)
print("st" in string)
print("s" in string)
print("PY" in string)
#dictionaries
#in dictionaries only keys are searched
dic={"Name":"susmitha","age":20,"course":"btech"}
print("Name" in dic)
#for values:
print("susmitha" in dic.values())
print("for dictionaries and sets the search time is faster than other data types because sets uses hashing(O(1)) avg time")
li=[100,20,42]
set={20,4,1}
print(100 in li)#linear search (O(n))
print(20 in set)#faster O(1)