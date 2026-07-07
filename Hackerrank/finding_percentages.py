n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
print(student_marks)
query_name = input()
res=0
print(len(student_marks))
for i in student_marks:
    if i==query_name:
        for i in student_marks[i]:
            print(i)
            res+=i
        res=res/len(student_marks)
print(f"{res:.2f}")