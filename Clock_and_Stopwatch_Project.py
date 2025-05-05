# This is the program that can work as a stopwatch or a basic clock.
# I wrote a program using 'time' module, 'while' and 'for' loops.
import time
choice = input("""What do you want to see? (Q to quit the program)
> Clock
> Stopwatch
> """).lower()
while not choice == "q":
    if choice == "clock":
        start = input("""What do you want to know? (Q to quit the program)
> Year
> Month
> Day
> Time 
> """).lower()
        while not start == "q":
            year = time.strftime("%Y")
            month = time.strftime("%B")
            month_ = time.strftime("%m")
            day = time.strftime("%d")
            hour = time.strftime("%H")
            minute = time.strftime("%M")
            second = time.strftime("%S")
            if start == "year":
                print(f"The current year is {year} now!")
                start = input("""Do you want to know anything else? (Q to quit the program)
> """).lower()
            elif start == "month":
                print(f"The current month is {month}!")
                start = input("""Do you want to know anything else? (Q to quit the program)
> """).lower()
            elif start == "day":
                print(f"The current day of {month} is {day} now!")
                start = input("""Do you want to know anything else? (Q to quit the program)
> """).lower()
            elif start == "time":
                if hour == "00" or hour == "01" or hour == "02" or hour == "03" or hour == "04" or hour == "05" or hour == "06" or hour == "07" or hour == "08" or hour == "09" or hour == "10" or hour == "11" or hour == "12":
                    print(f"The current hour of {day}.{month_}.{year} is {hour}:{minute} am!")
                    start = input("""Do you want to know anything else? (Q to quit the program)
> """).lower()
                elif hour == "13" or hour == "14" or hour == "15" or hour == "16" or hour == "17" or hour == "18" or hour == "19" or hour == "20" or hour == "21" or hour == "22" or hour == "23":
                    print(f"The current hour of {day}.{month_}.{year} is {hour}:{minute} pm!")
                    start = input("""Do you want to know anything else? (Q to quit the program)
> """).lower()
            elif len(start) > 0:
                print("I don't understand that...")
                start = input("""What do you want to know? (Q to quit the program)
> Year
> Month
> Day
> Time
> """).lower()
        print("""The program terminated
Thanks for using!""")
        break
    elif choice == "stopwatch":
        print("The stopwatch has been started")
        for line in range(1, 60):
            time.sleep(1)
            print(line)
        print("The stopwatch has been stopped")
        choice = input("""What do you want to see? (Q to quit the program)
> Clock
> Stopwatch
> """).lower()
        print("""The program terminated
Thanks for using!""")
    elif len(choice) > 0:
        print("I don't understand that...")
        choice = input("""What do you want to see? (Q to quit the program)
> Clock
> Stopwatch
> """).lower()
        print("""The program terminated
Thanks for using!""")

