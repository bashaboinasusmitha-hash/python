#swap all the uppercase letters to lowercase and vice versa.
def swap_case(s):
    s_1=''
    for i in s:
        if i==i.capitalize():
            i=i.lower()
            s_1+=i
        else:
            i=i.upper()
            s_1+=i
    return s_1
print(swap_case('HackerRank.com presents "Pythonist 2".'))
