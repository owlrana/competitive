# Creating a guessing game in python using very basic structures

secret_word = "giraffe"
guess = ""
guess_count = 0
guess_list = []
out_of_guesses = False
guess_limit = 3

while guess != secret_word and guess != "STOP" and not out_of_guesses :
    if guess_count < guess_limit:
        guess = input("Guess what the SECRET WORD is: ")
        guess_count +=1
        guess_list.append(guess)
    else:
        out_of_guesses = True

if out_of_guesses or guess_list[len(guess_list)-1] == "STOP":
    print("You LOSE!")
    print("These were your guesses: ", guess_list)
else:
    print("Yayyyy v nice you finally guessed it right!")
    print("These were your guesses: ", guess_list)