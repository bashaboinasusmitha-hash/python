#nested dictionaris:
dic={"a":10,"b":50,"c":30,"e":40,"f":60}
dic["b"]={"b1":20,"b2":35}
dic["c"]={"c1":20,"c2":10}
print(dic)#{'a': 10, 'b': {'b1': 20, 'b2': 35}, 'c': {'c1': 20, 'c2': 10}, 'e': 40, 'f': 60}
print(dic["b"])#{'b1': 20, 'b2': 35}
print(dic["c"])
dic["e"]={12,35,12}
print(dic)#{'a': 10, 'b': {'b1': 20, 'b2': 35}, 'c': {'c1': 20, 'c2': 10}, 'e': {35, 12}, 'f': 60}
print(len(dic))#5
print(len(dic["b"]))#2
d={"name":"susmitha","marks":{"maths":30,"physics":34}}
print(d["marks"]["maths"])#30
#print(len(dic["a"])) error
#loops:
dic={"a":10,"b":50,"c":30,"e":40,"f":60}
n=len(dic)
for i in dic:
    print(i)#a b c e f
    print(dic[i])#10 50 30 40 60
    #print(dic.keys())
for i in dic.values():
    print(i)#10 50 30 40 60
for i in dic.items():
    print(i)
'''('a', 10)
('b', 50)
('c', 30)
('e', 40)
('f', 60)'''
for i ,j in dic.items():
    print(i,j)
'''a 10
b 50
c 30
e 40
f 60'''
for i in dic.keys():
    print(i)#a b c e f
#dictionary comprehsion:
squares={x:x*x for x in range(5)}
print(squares)#{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
#membership operators:
dic={"name":"rajesh","age":35,"status":"married"}
if "field" in dic:
    print(dic["field"])
else:
    print("key not found")