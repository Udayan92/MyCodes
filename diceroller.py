import random
print "Welcome to the dice roller..!!"
print "How many side die would you like to roll..??"
x = int(raw_input())
y = random.randint(1,x)
print "The number on the die is", y
#def rolldice(ans):
#    print "how many sides would you like?"
#    x = int(raw_input())
#    while(ans == 'y' || ans == 'Y'):
#        y = random.randint(1,x)
#        print "the number on the die is", y
#    
