word=""
while word!="bye":
    word=input("Enter the word u want to talk with chatbot:").lower()
    if word=="hello":
        print("bot: hii")
    elif word=="how are you" or word=="how r u?" or word=="how are you?":
        print("bot: i'm fine,thank you")
    elif word=="bye":
        print("bot: goodbye")
        exit()
    else:
        print("bot: i didn't understand!")