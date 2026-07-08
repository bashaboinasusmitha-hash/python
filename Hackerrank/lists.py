N = int(input())#NO.of commands.
li=[]
for i in range(N):
    commands,*line =input().split()
    if commands == "append":
        li.append(int(line[0]))
    elif commands=="insert":
        li.insert(int(line[0]),int(line[1]))
    elif commands=="pop":
        li.pop()
    elif commands=="remove":
        li.remove()
    elif commands=="sort":
        li.sort()
    elif commands=="reverse":
        li.reverse()
    elif commands=="print":
        print(li)