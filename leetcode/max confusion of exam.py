#maximize the confusion of exam:
''' A teacher is writing a test with n true/false questions, with 'T' denoting true and 'F' denoting false. 
He wants to confuse the students by maximizing the number of consecutive questions with the same answer (multiple trues or multiple falses in a row).
You are given a string answerKey, where answerKey[i] is the original answer to the ith question. 
In addition, you are given an integer k, the maximum number of times you may perform the following operation:
Change the answer key for any question to 'T' or 'F' (i.e., set answerKey[i] to 'T' or 'F').
Return the maximum number of consecutive 'T's or 'F's in the answer key after performing the operation at most k times.'''
answerkey="TTFTTFTT"
k=1
n=len(answerkey)
l=0
ans=0
temp=0
f=0
t=0
#print(n)
for r in range(n):
    if answerkey[r]=="F":
        f+=1
    else:
        t+=1
    while (min(t,f)>k):
        if answerkey[l]=="F":
            f-=1
        else:
            t-=1
        l+=1
    ans=max(ans,r-l+1)
print(ans)