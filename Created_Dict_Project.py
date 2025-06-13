#  This program creates a random dictionary from strings in lists and asks you to enter all created values of the keys of the dict to create the 100% copy of the first dict


import random

#  Here is the list of names
names = ["Dario", "Vivian", "Annabella", "Leyla"]
surnames = ["Correa", "Huang", "Simpson", "Thompson"]
cities = ["New York", "Paris", "London", "Tokio", ]
jobs = ["Doctor", "Engineer","Teacher","Sales Assistant"]

#  Here is the possibility for names that returns a random number from 0 to 3 (3 included)
name_possibility = random.randrange(0,4)


#  This function returns a random name. It depends on the number that was chosen by random
def random_name(*, chance: int, first_name: str, second_name: str, third_name: str, forth_name: str) -> str:
        if chance == 0:
            name = first_name
            return name
        elif chance == 1:
            name = second_name
            return name
        elif chance == 2:
            name = third_name
            return name
        elif chance == 3:
            name = forth_name
            return name
#  'chance' parameter is the 'possibility' variable
#  'first_name' parameter is the 'Dario' name
#  'second_name' parameter is the 'Vivian' name
#  'third_name' parameter is the 'Annabella' name
#  'forth_name' parameter is the 'Leyla' name


#  Here is the possibility for surnames that returns a random number from 0 to 3 (3 included)
surname_possibility =  random.randrange(0,4)


#  This function returns a random surname. It depends on the number that was chosen by random
def random_surname(*, chance: int, first_surname: str, second_surname: str, third_surname: str, forth_surname: str) -> str:
        if chance == 0:
            surname = first_surname
            return surname
        elif chance == 1:
            surname = second_surname
            return surname
        elif chance == 2:
            surname = third_surname
            return surname
        elif chance == 3:
            surname = forth_surname
            return surname
#  'chance' parameter is the 'possibility' variable
#  'first_surname' parameter is the 'Correa' name
#  'second_name' parameter is the 'Huang' name
#  'third_name' parameter is the 'Simpson' name
#  'forth_name' parameter is the 'Thompson' name


#  Here is the possibility for ages that returns the random age from 17 to 62 (62 included)
age_possibility = random.randrange(17,63)


#  This function returns a random age. It depends on the number that was chosen by random
def random_age() -> int:
    return age_possibility


#  Here is the possibility for jobs that returns a random number from 0 to 3 (3 included)
job_possibility = random.randrange(0,4)


#
def random_job(*,chance: int, first_job: str, second_job: str, third_job: str, forth_job: str) -> str:
    if chance == 0:
        job = first_job
        return job
    elif chance == 1:
        job = second_job
        return job
    elif chance == 2:
        job = third_job
        return job
    elif chance == 3:
        job = forth_job
        return job
#  'chance' parameter is the 'possibility' variable
#  'first_job' parameter is the doctor profession
#  'second_job' parameter is the engineer profession
#  'third_job' parameter is the teacher profession
#  'forth_job' parameter is the sales assistant profession


#  Here is the possibility for cities that returns a random number from 0 to 3 (3 included)
city_possibility = random.randrange(0,4)


#  This function returns a random city. It depends on the number that was chosen by random
def random_city(*, chance: int, first_city: str, second_city: str, third_city: str, forth_city: str) -> str:
    if chance == 0:
        city = first_city
        return city
    elif chance == 1:
        city = second_city
        return city
    elif chance == 2:
        city = third_city
        return city
    elif chance == 3:
        city = forth_city
        return city
#  'chance' parameter is the 'possibility' variable
#  'first_city' parameter is New York
#  'second_city' parameter is Paris
#  'third_city' parameter is London
#  'forth_city' parameter is Tokio


dict_name = random_name(chance = name_possibility, first_name = names[0], second_name = names[1],third_name = names[2],forth_name = names[3])
dict_surname = random_surname(chance = surname_possibility, first_surname = surnames[0], second_surname = surnames[1],third_surname = surnames[2],forth_surname = surnames[3])
dict_age = random_age()
dict_job = random_job(chance = job_possibility, first_job = jobs[0], second_job = jobs[1], third_job = jobs[2], forth_job = jobs[3])
dict_city = random_city(chance = city_possibility, first_city = cities[0], second_city = cities[1], third_city = cities[2], forth_city = cities[3])

# Here is the main profile which values you will have to copy to your dict
main_profile = {
        "name": {dict_name},
        "surname": {dict_surname},
        "age": {dict_age},
        "job": {dict_job},
        "current location": {dict_city}
}

#  The program shows the user a random dict
print(f"""Here is a dict: {main_profile}
Let's create the same one!""")
#  The program makes all values in lowercase to enter them with lowercase letters later
main_profile.update(name=dict_name.lower())
main_profile.update(surname=dict_surname.lower())
main_profile.update(age=dict_age)
main_profile.update(job=dict_job.lower())
main_profile.update(city=dict_city.lower())


#  This program checks if the 'real_name' parameter is equal to the value of the 'name' key in the main dict
def incorrect_name(*,real_name: str):
    while real_name != main_profile.get("name") or real_name == main_profile.get("name"):
        if real_name != main_profile.get("name"):
            print("The entered name is not correct.")
            real_name = input("Enter the name again: ").lower()
        else:
            #  Now we need to replace the first letter in the entered name on the uppercase one
            list_real_name = list(real_name)
            if list_real_name[0] in "abcdefghijklmnopqrstuvwxyz":
                list_real_name[0] = list_real_name[0].upper()
                new_name_in_function = "".join(list_real_name)
                return new_name_in_function
#  The 'real_name' parameter is the 'entered_name' variable


#  This program checks if the 'real_surname' parameter is equal to the value of the 'surname' key in the main dict
def incorrect_surname(*,real_surname: str):
    while real_surname != main_profile.get("surname") or real_surname == main_profile.get("surname"):
        if real_surname != main_profile.get("surname"):
            print("The entered surname is not correct.")
            real_surname = input("Enter the surname again: ").lower()
        else:
            #  Now we need to replace the first letter in the entered name on the uppercase one
            list_real_surname = list(real_surname)
            if list_real_surname[0] in "abcdefghijklmnopqrstuvwxyz":
                list_real_surname[0] = list_real_surname[0].upper()
                new_surname_in_function = "".join(list_real_surname)
                return new_surname_in_function
#  The 'real_surname' parameter is the 'entered_surname' variable


#  This program checks if the 'real_age' parameter is equal to the value of the 'age' key in the main dict
def incorrect_age(*,real_age: int):
    while real_age != main_profile.get("age") or real_age == main_profile.get("age"):
        if real_age != main_profile.get("age"):
            print("The entered age is not correct.")
            real_age = int(input("Enter the age again: "))
        else:
            return real_age
#  The 'real_age' parameter is the 'entered_age' variable


#  This program checks if the 'real_job' parameter is equal to the value of the 'job' key in the main dict
def incorrect_job(*,real_job: str):
    while real_job != main_profile.get("job") or real_job == main_profile.get("job"):
        if real_job != main_profile.get("job"):
            print("The entered job is not correct.")
            real_job = input("Enter the job again: ").lower()
        else:
            #  Now we need to replace the first letter in the entered name on the uppercase one
            list_real_job = list(real_job)
            if list_real_job[0] in "abcdefghijklmnopqrstuvwxyz":
                list_real_job[0] = list_real_job[0].upper()
                new_job_in_function = "".join(list_real_job)
                first_word = new_job_in_function
                new_first_word = []
                for i in first_word:
                    if i == " ":
                        break
                    new_first_word.append(i)
                #  If there is more than one single word, the program makes the first letter of the second word the uppercase one
                if " " in list_real_job:

                    list_real_job.reverse()
                    new_list_real_job = []

                    for i in list_real_job:
                        if i == " ":
                            break
                        new_list_real_job.append(i)
                    new_list_real_job.reverse()
                    new_list_real_job[0] = new_list_real_job[0].upper()

                    first_word = "".join(new_first_word)
                    second_word = "".join(new_list_real_job)
                    return f"{first_word} {second_word}"
                return first_word
#  The 'real_job' parameter is the 'entered_job' variable


#  This program checks if the 'real_city' parameter is equal to the value of the 'city' key in the main dict
def incorrect_city(*,real_city: str):
    while real_city != main_profile.get("city") or real_city == main_profile.get("city"):
        if real_city != main_profile.get("city"):
            print("The entered surname is not correct.")
            real_city = input("Enter the surname again: ").lower()
        else:
            #  Now we need to replace the first letter in the entered name on the uppercase one
            list_real_city = list(real_city)
            if list_real_city[0] in "abcdefghijklmnopqrstuvwxyz":
                list_real_city[0] = list_real_city[0].upper()
                new_city_in_function = "".join(list_real_city)
                first_word = new_city_in_function
                new_first_word = []
                for i in first_word:
                    if i == " ":
                        break
                    new_first_word.append(i)

                #  If there is more than one single word, the program makes the first letter of the second word the uppercase one
                if " " in list_real_city:

                    list_real_city.reverse()
                    new_list_real_city = []

                    for i in list_real_city:
                        if i == " ":
                            break
                        new_list_real_city.append(i)
                    new_list_real_city.reverse()
                    new_list_real_city[0] = new_list_real_city[0].upper()

                    first_word = "".join(new_first_word)
                    second_word = "".join(new_list_real_city)
                    return f"{first_word} {second_word}"
                return first_word

#  Here the new profile that will contain all our entered values
new_profile = {}

entered_name = input("Enter the name: ").lower()
#  Now we have to turn the function for this on adding the key
new_profile["name"] = incorrect_name(real_name=entered_name)

entered_surname = input("Enter the surname: ").lower()
#  Now we have to turn the function for this on adding the key
new_profile["surname"] = incorrect_surname(real_surname=entered_surname)

entered_age = int(input("Enter the age: "))
#  Now we have to turn the function for this on adding the key
new_profile["age"] = incorrect_age(real_age=entered_age)

entered_job = input("Enter the job: ").lower()
#  Now we have to turn the function for this on adding the key
new_profile["job"] = incorrect_job(real_job=entered_job)

entered_city = input("Enter the city: ").lower()
#  Now we have to turn the function for this on adding the key
new_profile["city"] = incorrect_city(real_city=entered_city)




#  If you entered everything right, the program will terminate showing us the new profile
print(f"""You've made the accurate copy of the main dict
Here it is:
{new_profile}

The program terminated
Thanks for using!""")

