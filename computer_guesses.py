import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ""

    while feedback != "c":
    	guess = random.randint(low, high)
    	feedback = input(f"Je li {guess} pre visok (H), pre nizak(L) ili točan (C)? ")

    	if feedback == "h":
    		high = guess - 1
    	elif feedback == "l":
    		low = guess + 1
    		
    print(f"JEJ, kompjuter je točno pogodio {guess}")

computer_guess(20)
