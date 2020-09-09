# Computes how much money you will have on day *day*, if you start with *starting_amount* of cash
# and earn *earn_percent* percents of what you already have every day.
def HowMuchMoney(starting_amount, earn_percent, day):
    day_multiplier = 1 + (earn_percent / 100.0)
    return starting_amount * (day_multiplier ** (day - 1))
    
def PrintExample(starting_amount, earn_percent, day):
    print("If you start with $%d and earn %d%% each day, you will have more than $%.0f on day %d!" % 
          (starting_amount, earn_percent, HowMuchMoney(starting_amount, earn_percent, day), day))

# Prints what will happen by day 350 if you start with $1000 and earn 2% every day
PrintExample(1000, 2, 350)