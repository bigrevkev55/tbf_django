

fighters_fatigue_rating = int(input("Welcome to the Thomas Boxing Federation Fatigue Calculator! Enter the fighter's "
                                    "fatigue rating: "))
rounds_in_the_fight = int(input("Now enter amount of rounds in the Fight: "))

adjusted_fatigue_rating = (fighters_fatigue_rating/12)*rounds_in_the_fight

# Prompt to enter the fighters fatigue rating and the amount of rounds in the fight.
print({fighters_fatigue_rating} and {rounds_in_the_fight})

# Give the fighters adjusted fatigue rating.
print(f"The fighter's adjusted fatigue rating is {adjusted_fatigue_rating}")
