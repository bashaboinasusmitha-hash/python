#for else:
'''here the else part is executed only when the for loop is succsessfully executed.'''
#find the targeted element
numbers=[10,3,4,5,2,9]
target=5
for i in numbers:
    if i==target:
        print("target found")#target found
        break
else:
    print("found")#here the else block is not printed because we are termiinating the for loop without iterating the total list.
numbers=[10,3,4,5,2,9]
target=100
for i in numbers:
    if i==target:
        print("target found")
        break
else:
    print("found")#found, here the else block is executed because for loop checks each and every element in the list