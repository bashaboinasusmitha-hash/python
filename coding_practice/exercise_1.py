#word formation by adding prefixes:
base_words=input("enter a base words separated by comma:").split(",")
print(base_words)
prefixes=input("enter a prefix:")
for words in base_words:
    new=prefixes+words
    print(f"the new word of {words} is '{new}'")
#using multiple prefixes :
base_words=input("enter a base words separated by comma:").split(",")
print(base_words)
prefixes=input("enter a prefixes:").split(",")
for words in base_words:
    for prefix in prefixes:
        print(prefix+words)
#word analysis by finding length of each word:
words=input("enter words:")
words=words.split(",")
for i in words:
    print(f"the length of word '{i}' is {len(i)}")