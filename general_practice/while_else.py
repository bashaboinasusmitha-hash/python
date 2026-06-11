#while else:
'''here the else block is executed when the while loop is false,
and not executed if the while loop iss terminated by using break'''
count=1
while count<=5:
    print(count)
    count+=1
else:
    print("Else Block")
print("out of loop")
'''here the else block is executed because when count=6  the while loop becomes false'''
count=1
while count<=5:
    print(count)
    count+=1
    if count==4:
        break
else:
    print("else block")
print("out of loop")#1 2 3 out of loop
'''here the else block is not executed because we are forcefully terminating the while loop.'''