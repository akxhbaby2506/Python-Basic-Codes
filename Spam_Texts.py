text = input("Enter the text: ")

if ("Make a lot of money" in text):
    spam = True
elif ("Click this" in text):
    spam = True
elif ("Subscribe now" in text):
    spam = True
elif ("Buy now" in text):
    spam = True
else:
    spam = False
    
if(spam):
    print("This is a spam")
else:
    print("It's not a spam")
    