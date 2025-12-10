import random
sec_num = random.randint(1,50)
print("Welcome to the Game, Guess a interger b/w 1 to 50.\nyou have only 10 chance")
counter=10
chance_exausted=False
while counter!=0:
    a = input("Enter the number: ")
    if a.isdigit():
        a = int(a)
        if a==sec_num:
            print("You won!")
            chance_exausted=True
            break
        else:
            if a < sec_num:
                print("Try a higher number.")
            else:            
                print("Try a lower number.")
            counter-= 1
            print(f"{counter} chances remaining.")
    else:
        print("Invalid data type used!, You have to use only intergers.")
if not chance_exausted:
    print("You have exausted all your chances!! Try again.")
print(f"Secret number was {sec_num}, Game over!")