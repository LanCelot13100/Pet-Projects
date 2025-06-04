#  This program asks you to create a tuple and enter a fruit that you want to take form this tuple

real_fruits = ('apple','cherry','grapes','peach','orange','mango',"guava",'lime','apricot','grapefruit','kiwi','plum','pear','strawberry','blackberry','banana','watermelon')

#  The difference between the 'real_fruits' and 'fruits' variables is the fact that 'fruits' variable is only needed in the for loop down below
fruits = ('Apple','Cherry','Grapes','Peach','Orange','Mango',"Guava",'Lime','Apricot','Grapefruit','Kiwi','Plum','Pear','Strawberry','Blackberry','Banana','Watermelon')
print("Here are the fruits that you can pun inside your tuple:")
for row1 in fruits:
    print(row1)
print("")


def first_fruit():
    x = input("Enter the first fruit: ").lower()
    while not x in real_fruits:
        print("This fruit wasn't in the tuple!")
        x = input("Enter the first fruit again: ").lower()
    return x


#  In this function, the 'same_fruit1' parameter is needed not to have the already chosen fruit as the second one
def second_fruit(*,same_fruit1: str):
    y = input("Enter the second fruit: ").lower()
    while not y in real_fruits or y == same_fruit1:
        if y == same_fruit1:
            print("You have already chosen this fruit!")
            y = input("Enter the second fruit again: ").lower()
        elif not y in real_fruits:
            print("This fruit wasn't in the tuple!")
            y = input("Enter the second fruit again: ").lower()
    return y


#  In this function, the 'same_fruit1' and 'same_fruit2' parameters are needed not to have the already chosen fruits as the third one
def third_fruit(*,same_fruit1: str,same_fruit2: str):
    q = input("Enter the third fruit: ").lower()
    while not q in real_fruits or q == same_fruit1 or q == same_fruit2:
        if q == same_fruit1 or q == same_fruit2:
            print("You have already chosen this fruit!")
            q = input("Enter the third fruit again: ").lower()
        elif not q in real_fruits:
            print("This fruit wasn't in the tuple!")
            q = input("Enter the third fruit again: ").lower()
    return q


#  These are functions that return the entered fruits with the uppercase first letter no matter how it was entered:
#  Were created to make the fruits in the tuple look better with the uppercase letter as the first one


#  Here is the first function:
first_fruit_function = first_fruit()
fruit1 = list(first_fruit_function)
def fruit_function1():
    if fruit1[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        return "".join(fruit1)
    elif fruit1[0] in "abcdefghijklmnopqrstuvwxyz":
        fruit1[0] = fruit1[0].upper()
        string_fruit1 = "".join(fruit1)
        return string_fruit1


#  Here is the second function:
second_fruit_function = second_fruit(same_fruit1=first_fruit_function)
fruit2 = list(second_fruit_function)
def fruit_function2():
    if fruit2[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        return "".join(fruit2)
    elif fruit2[0] in "abcdefghigklmnopqrstuvwxyz":
        fruit2[0] = fruit2[0].upper()
        string_fruit2 = "".join(fruit2)
        return string_fruit2


#  Here is the third function:
third_fruit_function = third_fruit(same_fruit1=first_fruit_function,same_fruit2=second_fruit_function)
fruit3 = list(third_fruit_function)
def fruit_function3():
    if fruit3[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        return "".join(fruit3)
    elif fruit3[0] in "abcdefghigklmnopqrstuvwxyz":
        fruit3[0] = fruit3[0].upper()
        string_fruit3 = "".join(fruit3)
        return string_fruit3


fruit_tuple = (fruit_function1(),fruit_function2(),fruit_function3())
#  The program shows the user the created tuple
print(f"""Here is the tuple of those fruits that you have created:
{fruit_tuple}""")
#  And finally it prints all chosen fruits one by one using 'for' loop
print("And here are these fruits one by one: ")
for row2 in fruit_tuple:
    print(row2)

print("""
The program terminated
Thanks for using!""")
