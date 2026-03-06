#Find Longest Word
sentence=input("enter a sentence: ")
sentence=sentence.split()
longest=(sentence[0])
#print(longest)
for i in sentence:
    if len(i)>len(longest):
        longest=i
print("the longest word is :",longest)
#Matrix Addition
matrx=[[2,4],[1,3]]
matrix=[[2,4],[3,5]]
r=len(matrx)
c=len(matrx[0])
print("matrix1")
for i in range(r):
    for j in range(c):
        print(matrx[i][j],end=" ")
    print()
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j],end=" ")
    print()
for i in range(r):
    for j in range(c):
        print(matrx[i][j]+matrix[i][j],end=" ")
    print()
#prime range:
num1=int(input("enter a number :"))
num2=int(input("enter a number 2:"))
for i in range(num1,num2+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print("the number is prime:",i,end=" ")