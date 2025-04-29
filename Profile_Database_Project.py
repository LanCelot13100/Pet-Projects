# This program contains three classes:
# Dogs, cats and humans
# if you enter dogs', then this program will give you the access to every dog's profile
# if you enter cats', then this program will give you the access to every cat's profile
# if you enter humans', then this program will give you the access to every human's profile
# Was created using 'class' technology :D
class Dog:
    def __init__(self,name,color,age,weight):
        self.name = name
        self.color = color
        self.age = age
        self.weight = weight
Mike = Dog("Mike","black",2,20)
Henry = Dog("Henry","white",4,50)
Alex = Dog("Alex","orange",7,40)
class Cat:
    def __init__(self,name,color,age,weight):
        self.name = name
        self.color = color
        self.age = age
        self.weight = weight
Richard = Cat("Richard","white",1,8)
Johnny = Cat("Johnny","grey",3,15)
Ray = Cat("Ray","black",6,20)
class Human:
    def __init__(self,name,age,height,weight,):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
Jake = Human("Jake",23,175,65)
Bob = Human("Bob",41,170, 120)
Steve = Human("Steve",30, 181,80)
question1 = input("Do you want to see humans' profiles or cats' profiles or dogs' ones? ").lower()
while not question1 == "q":
    if question1 == "dogs'" or question1 == "dogs" or question1 == "dog":
        question2 = input("""Here is a list of dogs' names which profiles you can see:
Mike
Henry
Alex
Which profile do you want to see? """).lower()
        if question2 == "mike":
            print(f"""Name: {Mike.name}
Color: {Mike.color}
Age: {Mike.age} 
Weight: {Mike.weight} kg""")
            question1 = input("What a profile do you want to see next? (Q to quit the program) ").lower()
        elif question2 == "henry":
            print(f"""Name: {Henry.name}
Color: {Henry.color}
Age: {Henry.age} 
Weight: {Henry.weight} kg""")
            question1 = input("What a profile do you want to see next? (Q to quit the program) ").lower()
        elif question2 == "alex":
            print(f"""Name: {Mike.name}
Color: {Alex.color}
Age: {Alex.age} 
Weight: {Alex.weight} kg""")
            question1 = input("What a profile do you want to see next? (Q to quit the program) ").lower()
        elif len(question2) > 0:
            print("I don't understand that.")
            question2 = input("Which profile do you want to see? ").lower()
    elif question1 == "cats'" or question1 == "cats" or question1 == "cat":
        question2 = input("""Here is a list of cats' names which profiles you can see:
Richard
Johnny
Ray
Which profile do you want to see? """).lower()
        if question2 == "richard":
            print(f"""Name: {Richard.name}
Color: {Richard.color}
Age: {Richard.age} 
Weight: {Richard.weight} kg""")
            question1 = input("What a profile do you want to see next? (Q to quit the program) ").lower()
        elif question2 == "johnny":
            print(f"""Name: {Johnny.name}
Color: {Johnny.color}
Age: {Johnny.age} 
Weight: {Johnny.weight} kg""")
            question1 = input("What a profile do you want to see next? (Q to quit the program) ").lower()
        elif question2 == "ray":
            print(f"""Name: {Ray.name}
Color: {Ray.color}
Age: {Ray.age} 
Weight: {Ray.weight} kg""")
            question1 = input("What a profile do you want to see next? (Q to quit the program) ").lower()
        elif len(question2) > 0:
            print("I don't understand that.")
            question2 = input("Which profile do you want to see? ").lower()
    elif question1 == "humans'" or question1 == "humans" or question1 == "human":
        question2 = input("""Here is a list of humans' names which profiles you can see:
Jake
Bob
Steve
Which profile do you want to see? """).lower()
        if question2 == "jake":
            print(f"""Name: {Jake.name}
Age: {Jake.age} 
Height: {Jake.height} cm
Weight: {Jake.weight} kg""")
            question1 = input("What a profile do you want to see next? (Q to quit the program) ").lower()
        elif question2 == "bob":
            print(f"""Name: {Bob.name}
Age: {Bob.age} 
Height: {Bob.height} cm
Weight: {Bob.weight} kg""")
            question1 = input("What a profile do you want to see next? (Q to quit the program) ").lower()
        elif question2 == "steve":
            print(f"""Name: {Steve.name}
Age: {Steve.age} 
Height: {Steve.height} cm
Weight: {Steve.weight} kg""")
            question1 = input("What a profile do you want to see next? (Q to quit the program) ").lower()
        elif len(question2) > 0:
            print("I don't understand that.")
            question2 = input("Which profile do you want to see? ")
    else:
        print("I don't understand that.")
        question1 = input("Do you want to see humans' profiles or cats' profiles or dogs' ones? ").lower()

print("""The program terminated.
Thanks for using!""")

