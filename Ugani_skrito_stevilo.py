secret = 11

guess = int(raw_input("Enter a secret number (between 1 and 20): "))

if guess == secret:
    print "You guess the right number!"
else:
    print "Sorry, wrong number, Try again!"