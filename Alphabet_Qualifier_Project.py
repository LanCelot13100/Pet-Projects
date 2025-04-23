
# Here is the description of this program down below
print("""Welcome to the program that finds the number of the letter of the entered word in English alphabet or...
This program can also find the number of the letter of the entered word!
But if you want to enter some number and find out the letter that's equal to this number, you can do that too!
This is the English alphabet:
abcdefghijklmnopqrstuvwxyz
'a' is the first letter,so the number of this is 1, 'b' = 2 and etc.

Do you want to play with it or maybe you want to get to the core of this program?
>play - play with that
>start - start the program itself""")
question_1 = input(">").lower()

# Here the 'game' starts down below if you don't want to start the main program first
while not question_1 == "start":
    if question_1 == "play":
        print("Do you want to enter a number or letter? ")
        question_1 = input(">").lower()
        while not question_1 == "start":
            if question_1 == "number":
                question_1 = input("Enter a number: ")
                while not question_1 == "start":
                    if int(question_1) > 26:
                        print("""The English alphabet contains only 26 letters
The entered number can't be more than 26""")
                        question_1 = input("Enter a number: ")
                    elif int(question_1) < 1 :
                        print("""The English alphabet contains only 26 letters
The entered number can't be negative or equal to 0""")
                        question_1 = input("Enter a number: ")
                    alphabet = " abcdefghijklmnopqrstuvwxyz"
                    number = alphabet.find(alphabet[int(question_1)])
                    letter = alphabet[number]
                    print(f"""The letter that's equal to '{question_1}' is '{letter}'
                
You can enter a number or letter again to continue playing or you can start a program itself
>letter - choose to enter a letter,enter a letter,receive the number of this letter
>number - choose to enter a number,enter a number,receive the letter of this number
>start - start the program itself""")
                    break
                question_1 = input(">").lower()

            elif question_1 == "letter":
                question_1 = input("Enter a letter: ").lower()
                while not question_1 == "start":
                    alphabet = " abcdefghijklmnopqrstuvwxyz"
                    number = alphabet.find(question_1)
                    print(f"""The number that's equal to '{question_1}' is '{number}'
                    
You can enter a number or letter again to continue playing or you can start a program itself
>letter - choose to enter a letter,enter a letter,receive the number of this letter
>number - choose to enter a number,enter a number,receive the letter of this number
>start - start the program itself""")
                    break
                question_1 = input(">").lower()
            else:
                print("I don't understand that...")
                question_1 = input("Do you want to enter a letter or number? ").lower()
    elif question_1:
        print("""I don't understand that...
        
Do you want to >start the program or >play with the technology of determination letters and numbers through each other?
>play - play with that
>start - start the program itself""")
        question_1 = input(">").lower()

# Here the main program starts down below after 'playing' with that
question_2 = input("""After entering any word you will be able get the number of any letter in this word in English alphabet by:
Entering any letter in the entered word (>letter)
Entering any number that's equal to the letter in the entered word (>number)
If you didn't understand that then you can open a technical documentation (>help)
Which way do you choose?
>""").lower()
while question_2 == "letter" or question_2 == "number" or question_2 == "help" or len(question_2) > 0:
    if question_2 == "letter":
        word = input("Enter any word: ")
        letter = input("Enter any letter in this word: ")
        while not (letter in word or letter.upper() in word):
            if letter.lower() in word:
                print("The uppercase form of this letter never was in this word")
                letter = input("Enter any letter in this word again: ")
            else:
                print("Looks like you've entered the wrong letter...")
                letter = input("Enter any letter in this word again: ")
        alphabet = " abcdefghijklmnopqrstuvwxyz"
        x = alphabet.find(letter.lower())
        print(f"""The number of this letter is equal to {x} in the English alphabet
The program has been terminated
Thanks for using!""")
        break


    elif question_2 == "number":
        word_question = input("Enter any word: ").lower()
        word = f" {word_question}"
        alphabet = " abcdefghijklmnopqrstuvwxyz"
        number = input("Enter any NUMBER of the letter in this word: ")
        number = int(number)
        x = alphabet.find(word[int(number)])
        letter = alphabet[x]
        print(f"""The number that was entered is '{letter}' or '{letter.upper()}'
This letter is equal to '{x}' in the English alphabet
The program has been terminated
Thanks for using!""")
        break
    elif question_2 == "help":
        print("""Look:
Firstly,you enter a word;
Secondly,you enter a LETTER in the word or a NUMBER of the letter in the word to choose the number of the letter in the English alphabet;
You can choose to find the number or the letter by entering this letter or entering the number of this letter in the word
""")
        question_2 = input("""Do you want to find a number of the chosen letter in the English alphabet by:
Entering a letter: (>letter) 
Entering a number: (>number)
>""").lower()
    else:
        print("I don't understand that...")
        question_2 = input("""Do you want to find a number of the chosen letter in the word by:
Entering a letter? (>letter) 
Entering a number? (>number)
>""").lower()
