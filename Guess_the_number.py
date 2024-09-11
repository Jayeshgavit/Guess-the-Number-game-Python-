import random as rd    

n = rd.randint(1,100)

num = -1
count = 0 

print(" Welcome to Guess Game".center(50, '-'))
while (num != n):
    count = count + 1
    num = int(input(" Geuss the Number : "))

    if (num > n):
        print("Too High...!! Enter lower Number")
    elif (num < n):
        print("Too Low...!! Enter higher Number")
    else:
        print("Congratulations!!! You guessed it right.")
        

print(f"You guessed the number in {count} attempts.")







