import random
print "This is a random number guesser.."
x = random.randrange(1, 100)
print "I just generated a number between 1 and 100, can you guess what it is?"

count = 0
while(count < 4):
    y = int(raw_input())
    if (y == x):
        print "You got it right..!!"
        break
    elif (y > x):
        print "bit higher than expected,try again"
        count = count + 1
    elif (y < x):
        print "bit lower than expected,try again"
        count = count + 1;
    else:
        print "invalid input."
        break

print "The number guessed by me was,", x
 


