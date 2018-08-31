import random
name = input("What is your name: ")

while True:
    userinput= input("Do you have a question(yes/no)")
    if userinput.strip() == "yes":
        quest =input("What is your question?")
        fortunes = ["Yes", "No", "Maybe", "Sooon"]
        print(random.choice(fortunes))
        print("Have a nice day " + str(name))
    else:
         break
print("Have a nice day " + str(name))       


