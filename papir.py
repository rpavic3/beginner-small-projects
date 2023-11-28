import random

while True:
    choices = ["papir", "škare", "dijamant"]
    computer = random.choice(choices)

    player = None

    while player not in choices:
        player = input("\n""papir, škare ili dijamant?: ").lower()

    print("\n""Ti si izabrao: ",player)
    print("\n""Kompjuter je izabrao: ",computer)

    if player == computer:
	    print("\n""Igra je neriješena")

    if player == "papir" and computer == "škare":
	    print("\n""Izgubili ste!")

    if player == "papir" and computer == "dijamant":
	    print("\n""Pobijedili ste!")

    if player == "škare" and computer == "papir":
	    print("\n""Pobijedili ste!")

    if player == "škare" and computer == "dijamant":
	    print("\n""Izgubili ste!")

    if player == "dijamant" and computer == "papir":
	    print("\n""Izgubili ste!")

    if player == "dijamant" and computer == "škare":
	    print("\n""Pobijedili ste!")

    again = input("\n""Igrati ponovo? da/ne: ").lower()

    if again == "ne":
	    break
    elif again == "da":
        print("NOVA IGRA")
    else:
        again = input("\n""Igrati ponovo? da/ne: ").lower()
	




