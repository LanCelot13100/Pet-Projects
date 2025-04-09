list_of_names = ["John", "Freddy", "Sam"]
list_0 = list_of_names[0]
list_1 = list_of_names[1]
list_2 = list_of_names[2]
list_of_surnames = ["Leo","Mercury","Smith"]
surname_1 = list_of_surnames[0]
surname_2 = list_of_surnames[1]
surname_3 = list_of_surnames[2]
print("#Your full name can be John Leo, Freddy Mercury, Sam Smith")
question = input("Enter your name: ")
entered = False
while not question == list_0 or question == list_1 or question == list_2 or len(question) > 0:
    if question == list_0 or question == list_1 or question == list_2:
        print("Your name was excepted!")
        break
    elif len(question) > 0:
        print("It's not your real name and you know that!")
        question = input("Enter you name again: ")
question_2 = input("Enter your surname: ")
while question_2 == surname_1 and question == list_0 or question_2 == surname_2 and question == list_1 or question_2 == surname_3 and question == list_2 or question_2 == surname_1 and question != list_0 or question_2 == surname_2 and question != list_1 or question_2 == surname_3 and question != list_2 or len(question_2) > 0:
    if question_2 == surname_1 and question == list_0:
        print(f"""Your surname has been excepted!
The full '{list_0} {surname_1}' name has been confirmed!
Welcome!""")
        break
    elif question_2 == surname_2 and question == list_1:
        print(f"""Your surname has been excepted!
The full '{list_1} {surname_2}' name has been confirmed!
Welcome!""")
        break
    elif question_2 == surname_3 and question == list_2:
        print(f"""Your surname has been excepted!
The full '{list_2} {surname_3}' name has been confirmed!
Welcome!""")
        break
    elif question_2 == surname_1 and question != list_0 or question_2 == surname_2 and question != list_1 or question_2 == surname_3 and question != list_2:
        print("It doesn't have to be your surname")
        question_2 = input("Enter your surname again: ")
    else:
        print("I don't understand that...")
        question_2 = input("Enter your surname again: ")

