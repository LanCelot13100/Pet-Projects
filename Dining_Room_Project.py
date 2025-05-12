# This program allows you to enter a dining room and choose the food that you'll be eaten.
# There are lots of food to choose, so enjoy your meal
# There is the 'plate' variable, it's a list that will contain as many types of food as you want to place in there.
# When you want to see what you've put 'on your plate', you have to enter the 'plate'
# if enter some type of food after entering the same one, the program will tell you that 'You've already put this food on your plate!'


plate = []
# This is the list of fruits for entering that again:
another_apple = False
another_grapes = False
another_orange = False
another_cherry = False
another_kiwi = False
# This is the list of vegetables for entering that again:
another_carrot = False
another_tomato = False
another_potato = False
another_pumpkin = False
another_eggplant = False
# This is the list of fish for entering that again:
another_salmon = False
another_trout = False
another_mackerel = False
# This is the list of meat for entering that again:
another_beef = False
another_pork = False
another_duck = False
# This is the list of marshmello for entering that again:
another_marshmello = False
print("""Here is the list of food that you can put on your plate down below:
Fruits
Vegetables
Fish
Meat
Marshmello""")
question1 = input("Which one do you want to put on your plate? (>plate to see the put food on the plate) ").lower()
while question1 == "fruits" or question1 == "vegetables" or question1 == "fish" or question1 == 'meat' or question1 == 'marshmello' or question1 == 'plate' or len(question1) > 0 or question1.strip() == "":
    if question1 == "fruits":
        print("""The list of fruits:
Apple
Grapes
Orange
Cherry
Kiwi""")
        question1 = input("Which one do you want to put on your plate? (>plate to see the put food on the plate) ").lower()
        while not (question1 == 'vegetables' or question1 == 'fish' or question1 == 'meat' or question1 == 'marshmello' or question1 == 'plate'):
            if question1 == 'apple':
                if another_apple:
                    print("You've already put this fruit on your plate!")
                    question1 = input("Anything else? (>plate to see the put food on the plate) ").lower()
                else:
                    another_apple = True
                    plate.append("Apple")
                    print(f"Apple was put on your plate.")
                    question1 = input("Anything else? (>plate to see the put food on the plate) ").lower()
            elif question1 == 'grapes':
                if another_grapes:
                    print("You've already put this fruit on your plate!")
                    question1 = input("Anything else? (>plate to see the put food on the plate) ").lower()
                else:
                    another_grapes = True
                    plate.append("Grapes")
                    print(f"Grapes was put on your plate.")
                    question1 = input("Anything else? (>plate to see the put food on the plate) ").lower()
            elif question1 == 'orange':
                if another_orange:
                    print("You've already put this fruit on your plate!")
                    question1 = input("Anything else? (>plate to see the put food on the plate) ").lower()
                else:
                    another_apple = True
                    plate.append("Orange")
                    print(f"Orange was put on your plate.")
                    question1 = input("Anything else? (>plate to see the put food on the plate) ").lower()
            elif question1 == 'cherry':
                if another_cherry:
                    print("You've already put this fruit on your plate!")
                    question1 = input("Anything else? (>plate to see the put food on the plate) ").lower()
                else:
                    another_cherry = True
                    plate.append("Cherry")
                    print(f"Cherry was put on your plate.")
                    question1 = input("Anything else? (>plate to see the put food on the plate) ").lower()
            elif question1 == 'kiwi':
                if another_kiwi:
                    print("You've already put this fruit on your plate!")
                    question1 = input("Anything else? (>plate to see the put food on the plate) ").lower()
                else:
                    another_kiwi = True
                    plate.append("Kiwi")
                    print(f"Kiwi was put on your plate.")
                    question1 = input("Anything else? (>plate to see the put food on the plate) ").lower()
            elif len(question1) > 0:
                print("The entered food wasn't understood clearly.")
                question1 = input("Enter it again! (>plate to see the put food on the plate) ").lower()

    elif question1 == 'vegetables':
        print("""The list of vegetables:
Carrot
Tomato
Potato
Pumpkin
Eggplant""")
        question1 = input("Which one do you want to put on your plate? (>plate to see the put food on the plate) ").lower()
        while not (question1 == 'fruits' or question1 == 'fish' or question1 == 'meat' or question1 == 'marshmello' or question1 == 'plate'):
            if question1 == 'carrot':
                if another_carrot:
                    print("You've already put this vegetable on your plate!")
                    question1 = input("Anything else? (>plate to see the put food on the plate) ").lower()
                else:
                    another_carrot = True
                    plate.append("Carrot")
                    print(f"Carrot was put on your plate.")
                    question1 = input("Anything else? (>plate to see the put food on the plate) ").lower()
            elif question1 == 'tomato':
                if another_tomato:
                    print("You've already put this vegetable on your plate!")
                    question1 = input("Anything else? (>plate to see the put food on the plate) ").lower()
                else:
                    another_tomato = True
                    plate.append("Tomato")
                    print(f"Tomato was put on your plate.")
                    question1 = input("Anything else? (>plate to see the put food on the plate) ").lower()
            elif question1 == 'potato':
                if another_potato:
                    print("You've already put this vegetable on your plate!")
                    question1 = input("Anything else? (>plate to see the put food on the plate) ").lower()
                else:
                    another_potato = True
                    plate.append("Potato")
                    print(f"Potato was put on your plate.")
                    question1 = input("Anything else? (>plate to see the put food on the plate) ").lower()
            elif question1 == 'pumpkin':
                if another_pumpkin:
                    print("You've already put this vegetable on your plate!")
                    question1 = input("Anything else? (>plate to see the put food on the plate) ").lower()
                else:
                    another_pumpkin = True
                    plate.append("Pumpkin")
                    print(f"Pumpkin was put on your plate.")
                    question1 = input("Anything else? (>plate to see the put food on the plate) ").lower()
            elif question1 == 'eggplant':
                if another_eggplant:
                    print("You've already put this vegetable on your plate!")
                    question1 = input("Anything else? (>plate to see the put food on the plate) ").lower()
                else:
                    another_eggplant = True
                    plate.append("Eggplant")
                    print(f"Eggplant was put on your plate.")
                    question1 = input("Anything else? (>plate to see the put food on the plate) ").lower()
            elif len(question1) > 0:
                print("The entered food wasn't understood clearly.")
                question1 = input("Enter it again! (>plate to see the put food on the plate) ").lower()

    elif question1 == "fish":
        print("""The list of fish:
Salmon
Trout
Mackerel""")
        question1 = input("Which one do you want to put on your plate? (>plate to see the put food on the plate) ").lower()
        while not (question1 == 'vegetables' or question1 == 'fruits' or question1 == 'meat' or question1 == 'marshmello' or question1 == 'plate'):
            if question1 == 'salmon':
                if another_salmon:
                    print("You've already put this fish on your plate!")
                    question1 = input("Anything else? (>plate to see the put food on the plate) ").lower()
                else:
                    another_salmon = True
                    plate.append("Salmon")
                    print(f"Salmon was put on your plate.")
                    question1 = input("Anything else? (>plate to see the put food on the plate) ").lower()
            elif question1 == 'trout':
                if another_trout:
                    print("You've already put this fish on your plate!")
                    question1 = input("Anything else? (>plate to see the put food on the plate) ").lower()
                else:
                    another_trout = True
                    plate.append("Trout")
                    print(f"Trout was put on your plate.")
                    question1 = input("Anything else? (>plate to see the put food on the plate) ").lower()
            elif question1 == 'mackerel':
                if another_mackerel:
                    print("You've already put this fish on your plate!")
                    question1 = input("Anything else? (>plate to see the put food on the plate) ").lower()
                else:
                    another_mackerel = True
                    plate.append("Mackerel")
                    print(f"Mackerel was put on your plate.")
                    question1 = input("Anything else? (>plate to see the put food on the plate) ").lower()
            elif len(question1) > 0:
                print("The entered food wasn't understood clearly.")
                question1 = input("Enter it again! (>plate to see the put food on the plate) ").lower()


    elif question1 == "meat":
        print("""The list of meat:
Beef
Pork
Duck""")
        question1 = input("Which one do you want to put on your plate? (>plate to see the put food on the plate) ").lower()
        while not (question1 == 'vegetables' or question1 == 'fish' or question1 == 'fruits' or question1 == 'marshmello' or question1 == 'plate'):
            if question1 == 'beef':
                if another_beef:
                    print("You've already put this meat on your plate!")
                    question1 = input("Anything else? (>plate to see the put food on the plate) ").lower()
                else:
                    another_beef = True
                    plate.append("Beef")
                    print(f"Beef was put on your plate.")
                    question1 = input("Anything else? (>plate to see the put food on the plate) ").lower()
            elif question1 == 'pork':
                if another_pork:
                    print("You've already put this meat on your plate!")
                    question1 = input("Anything else? (>plate to see the put food on the plate) ").lower()
                else:
                    another_pork = True
                    plate.append("Pork")
                    print(f"Pork was put on your plate.")
                    question1 = input("Anything else? (>plate to see the put food on the plate) ").lower()
            elif question1 == 'duck':
                if another_duck:
                    print("You've already put this meat on your plate!")
                    question1 = input("Anything else? (>plate to see the put food on the plate) ").lower()
                else:
                    another_duck = True
                    plate.append("Duck")
                    print(f"Duck was put on your plate.")
                    question1 = input("Anything else? (>plate to see the put food on the plate) ").lower()
            elif len(question1) > 0:
                print("The entered food wasn't understood clearly.")
                question1 = input("Enter it again! (>plate to see the put food on the plate) ").lower()

    elif question1 == 'marshmello':
        if another_marshmello:
            print("You've already put marshmello on your plate!")
            question1 = input("Anything else? (>plate to see the put food on the plate) ").lower()
        else:
            another_marshmello = True
            plate.append("Marshmello")
            print(f"Marshmello was put on your plate.")
            question1 = input("Anything else? (>plate to see the put food on the plate) ").lower()
    elif question1 == "plate":
        if len(plate) == 0:
            print("""Ooops!
Looks like you haven't put anything on you plate yet...""")
        else:
            print("Here is the list of the food that you've put on your plate down below:")
            for row in plate:
                print(row)
        question3 = input("""Do you want to add something else?
>Yes
>No (finish)
>""").lower()
        while not (question3 == 'yes' or question3 == 'no'):
            print("I don't understand that.")
            question3 = input("""Do you want to add something else?
>Yes
>No (finish)
>""").lower()
        if question3 == 'yes':
            question1 = input("""What else do you want to add? (>plate to see the put food on the plate) 
Fruits
Vegetables
Fish
Meat
Marshmello
""").lower()
        elif question3 == 'no':
            print("""The program terminated
Thanks for using!""")
            break

    elif len(question1) > 0 or question1.strip() == "":
        print("The entered food wasn't understood clearly.")
        question1 = input("Enter it again! (>plate to see the put food on the plate) ").lower()

