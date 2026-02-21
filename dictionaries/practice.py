'''Dictionaries is a collection of key value pairs.values can be mutable
keys must be immutable,unique,keys cannot be sets,lists,dictionary.'''
#creating a dictionary:
dic={"name":"susmitha","roll no":238316624,"age":20}
print(dic)
#method 2:
d=dict(a=1,b=2)
print(d)
#empty dictionary
dic={}
print(dic)
#method : from keys:
d=dict.fromkeys(["a","b","c"],0)
print(d)#{'a':0,'b':0,'c':0}
#Accessing values:
d={"a":10,"b":20,"c":10}
print(d)
print(d["a"])#10 it gives error if key not in dictionary
print(d.get("b"))#20 safe method it doesn't give error but show as none so safe access method
#Adding and updating :
d={"a":10,"b":20,"c":10}
d["c"]=30 # updating 
d["e"]=40#adding a key valuee pair
d["f"]=60#adding 
d["b"]=50
print(d)#{"a":10,"b":50,"c":30,"e":40,"f":60}
#removing elements:
#pop():removes specific key
dic={"a":10,"b":50,"c":30,"e":40,"f":60}
dic.pop("a")
print(dic)#{"b":50,"c":30,"e":40,"f":60}
#popitem(): removes last inserted item
dic={"a":10,"b":50,"c":30,"e":40,"f":60}
dic.popitem()
print(dic)#{"a":10,"b":50,"c":30,"e":40}
#del:
dic={"a":10,"b":50,"c":30,"e":40,"f":60}
del dic["b"]
print(dic)#{"a":10,"c":30,"e":40,"f":60}
#clear(): remove all items:
dic={"a":10,"b":50,"c":30,"e":40,"f":60}
dic.clear()
print(dic)#{}
#dictionary methods:
#keys():prints only keys in form of list 
dic={"a":10,"b":50,"c":30,"e":40,"f":60}
a=dic.keys()
print(a)#dict_keys(['a', 'b', 'c', 'e', 'f'])
#values():prints only values in lis
dic={"a":10,"b":50,"c":30,"e":40,"f":60}
b=dic.values()
print(b)#dict_values([10, 50, 30, 40, 60])
#items():
dic={"a":10,"b":50,"c":30,"e":40,"f":60}
a=dic.items()
print(a)#dict_items([('a', 10), ('b', 50), ('c', 30), ('e', 40), ('f', 60)])
#update()
dic={"a":10,"b":50,"c":30,"e":40,"f":60}
dic_1={"name":"susmitha","age":20,"course":"B-tech"}
dic.update({"a":35})
print(dic)
dic.update(dic_1)
print(dic)#{'a': 10, 'b': 50, 'c': 30, 'e': 40, 'f': 60, 'name': 'susmitha', 'age': 20, 'course': 'B-tech'}
#copy()
dic={"a":10,"b":50,"c":30,"e":40,"f":60}
new_dic=dic.copy()
print(new_dic)#{'a': 10, 'b': 50, 'c': 30, 'e': 40, 'f': 60}
#default()
dic={"a":10,"b":50,"c":30,"e":40,"f":60}
a=dic.setdefault("g",0)
print(a)#0
a=dic.setdefault("a",0)
print(a)#10 beacause it is already present if not i print as 0
#duplicte data:
dic={"a":10,"b":50,"c":30,"e":40,"a":60}
print(dic)#dic={"a":60,"b":50,"c":30,"e":40}
#if we enter any duplicate key then it print tha value of last inserted duplicate key value