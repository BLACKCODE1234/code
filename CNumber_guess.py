# you're too old for this, make ti guesing game😏
# 😂😂😂🤣 okay
# print('first code now')


import random



print("HELLO WELCOME TO THE NUMBER GUESSING GAME")
print("Guess a number from 1 to 20" 
    "You have 10 attempt")

# randnumber = random.randint(1,20)
username = input("USERNAME: ").capitalize()

while True:
    computer = random.randint(1,20)
    count = 0
    totalcount = 10
    while True:
        count = count + 1 
    
        user = int(input('ENTER NUMBER: '))
        if user == computer :
            print(f"Congratulations👌✔ {username},you've won")
            print(f"Your Number: {user}     Computer: {computer}")
            break



        elif user > computer :
            print("Number's High")
            print(f"Your Number: {user}     Computer: {computer}")
        
        elif user < computer :
            print("Number's Low")
            print(f"Your Number: {user}     Computer: {computer}")


        if count == totalcount // 2:
            print(f"{username}, you have 5 attempts left ")

        elif count == totalcount:
            print(f"{username}, you have exhausted all your attempt")
            print(f"Your Number: {user}     Computer: {computer}")



    startquery = input("Do you want to play again (Y/N): ")
    if startquery == "Y":
        continue
    elif startquery == "N":
        print("Thank you for trusting us")
        break
    # else:
    #     print("Thank you")
    # print(computer)
