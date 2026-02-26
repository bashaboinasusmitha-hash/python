#checking whether a number is prime or not:
def prime(n):
    if n<=1:
        return "Not a prime"
    for i in range(2,n):
        if n%i==0:
            return "not prime"
    return prime
num=int(input("enter a number:"))
print(prime(num))
#reverse a string:
def reverse_string(string):
    return string[::-1]
word=input("enter a word:")
print(reverse_string(word))
#counting vowels:
def count_vowels_consonants(text):
    vowels = "aeiouAEIOU"
    v_count = 0
    c_count = 0
    for ch in text:
        if ch.isalpha():   # check only letters
            if ch in vowels:
                v_count += 1
            else:
                c_count += 1
    return v_count,c_count
word = input("Enter a word or sentence: ")
vowels, consonants = count_vowels_consonants(word)
print("Number of vowels:", vowels)
print("Number of consonants:", consonants)