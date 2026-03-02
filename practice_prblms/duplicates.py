#removing duplicates from sentences:
sentence=input("enter a sentence :")
words=sentence.split()
unique=[]
for i in words:
    if i not in unique:
        unique.append(i)
print(unique)
print(" ".join(unique))
#counting vowels and consonants
sentence = input("Enter a sentence: ").lower()
vowels = "aeiou"
vowel_count = 0
consonant_count = 0
for char in sentence:
    if char.isalpha():   # check only letters
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)