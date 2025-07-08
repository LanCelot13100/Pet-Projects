#Rock, Paper, Scissors Game
import random
import time


#  This function checks if the entered element is valid or not
def element_valid(*,elem: str,elem_list: list) -> str:
    while not elem.capitalize() in elem_list:
        print("There is no such element!")
        elem = input("Enter the element again: ")

    return elem.capitalize()
#  'elem' is the string from the 'user_guess' input
#  'elem_list' is the 'variants' list


#  This function generates a random element that will be used against you in the game
def element_generator(*,elem_list: list) -> str:
    elem = random.choice(elem_list)

    return elem
#  'elem_list' is the 'variants' list


def clash(*,your_elem: str,their_elem: str):
    if your_elem == their_elem:
        return "No one won..."
    else:
        if your_elem == "Rock" and their_elem == "Paper" or  your_elem == "Paper" and their_elem == "Scissors" or your_elem == "Scissors" and their_elem == "Rock":
            return "You lost!"
        elif your_elem == "Rock" and their_elem == "Scissors" or your_elem == "Paper" and their_elem == "Rock" or your_elem == "Scissors" and their_elem == "Paper":
            return "You won!"


variants = ["Rock","Paper","Scissors"]  #  <- Here is the list of elements

while True:  #  <- Here is the while loop that executes all written functions 
    user_guess = input("Enter the element: ")


    your_element = element_valid(elem=user_guess, elem_list=variants)  #  <- The 'element_valid' function belongs to the 'your_element' variable now
    their_element = element_generator(elem_list=variants)  #  <- The 'element_generator' function belongs to the 'their_element' variable now
    battle = clash(your_elem=your_element, their_elem=their_element)  #  <- The 'clash' function belongs to the 'battle' variable now

    print(f"Your element is {your_element}!")
    time.sleep(1)

    print(f"Your opponent's element is {their_element}!")
    time.sleep(1)

    print(battle)

    quit_button = input("Continue? (Q to Quit) ").lower()  #  After executing the game, you can terminate the program by pressing 'Q'
    if quit_button == "q":
        break

print("""The program terminated!
Thanks for using!""")
