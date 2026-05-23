#dictionary programs:
'''Create a dictionary for a student:
Name
Roll number
Marks'''
dic={
    "Name":"Susmitha",
    "Age":23,
    "Marks":95
}
print(dic)
#Access dictionary values using keys.
for i in dic.keys():
    print(i)
a=dic.keys()
print(a)
b=dic.values()
print(b)
#adding new key value pair:
dic["Branch"]="CSE-AIML"
print(dic)
#Update dictionary values.
dic["Age"]=26
print(dic)
#Delete an item from dictionary.
del dic["Branch"]
print(dic)
#Find highest value in dictionary.
dic_1={"priya_m":95,"sushuuy_m":96,"tharun_m":93}
print(max(dic_1.values()))
maximum=float("-inf")
for i in dic_1.values():
    if i>maximum:
        maximum=i
print(maximum)
#Count frequency of characters in a string using dictionary.
s="susmithaasui"
dic={}
for i in s:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
print(dic)