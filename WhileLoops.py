import random
random_number = random.randint(1, 100)
while True:
    x = int(input("Pick a number between 1 and 100: "))

    if x!=random_number:
        print("Wrong number.")
    else:
        print("Correct!")
        break






