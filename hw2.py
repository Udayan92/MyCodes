# Name:
# Section:
# hw2.py

##### Template for Homework 2, exercises 2.0 - 2.5  ######

# **********  Exercise 2.0 ********** 

def f1(x):
    print x + 1

def f2(x):
    return x + 1

# **********  Exercise 2.1 ********** 

def outcome(player1, player2):
    if player1 == 'rock' and player2 == 'rock':
      print "TIE"
    elif player1 == 'rock' and player2 == 'paper':
      print "paper beats rock.player2 wins"
    elif player1 == 'rock' and player2 == 'scissors':
      print "rock beats scissors.player1 wins."
    
    elif player1 == 'paper' and player2 == 'paper':
      print "TIE"
    elif player1 == 'paper' and player2 == 'rock':
      print "paper beats rock.player1 wins."
    elif player1 == 'paper' and player2 == 'scissors':
      print "scissors cut paper.player2 wins."

    elif player1 == 'scissors' and player2 == 'scissors':
      print "TIE"
    elif player1 == 'scissors' and player2 == 'rock':
      print "rock beats scissors.player2 wins."
    elif player1 == 'scissors' and player2 == 'paper':
      print "scissors cut paper.player2 wins."
    
    else: 
      print "Invalid choice." 
   ##### YOUR CODE HERE #####
print "Welcome to rock,paper,scissors game."
print "What do you select,player1?rock,paper or scissors?"
player1 = raw_input()
print "And what do you select,player2?rock paper or scissors?"
player2 = raw_input()
outcome(player1, player2) 
  
# Test Cases for Exercise 2.1
outcome('rock', 'rock')
outcome('rock', 'paper')
outcome('scissors', 'paper')
outcome('abc', 'xyz')


# ********** Exercise 2.2 ********** 

# Define is_divisible function here
def is_divisible(m, n):
    if m % n == 0:
      return True
    else:
      return False

# Test cases for is_divisible
## Provided for you... uncomment when you're done defining your function

print is_divisible(10, 5)  # This should return True
print is_divisible(18, 7)  # This should return False
#print is_divisible(42, 0)  # What should this return?


# Define not_equal function here
def not_equal(a, b):
    if a - b == 0:
      return True
    else:
      return False
# Test cases for not_equal
not_equal(3, 3)
not_equal(4, 5)

# ********** Exercise 2.3 ********** 

## 1 - multadd function
def multadd(a, b, c):
    return (a*b) + c

## 2 - Equations
##### YOUR CODE HERE #####
    import math
    return math.sin(pi/4) + (cos(pi/4))/2
    return math.ceil(276/19) + 2 * math.log(12, 7)
    

# Test Cases
# angle_test =
# print "sin(pi/4) + cos(pi/4)/2 is:"
# print angle_test

# ceiling_test =
# print "ceiling(276/19) + 2 log_7(12) is:"
# print ceiling_test

## 3 - yikes function
##### YOUR CODE HERE #####
def yikes(x):
    import math
    return x*(math.e)**(-x) +(1 - (math.e)**(-x))**0.5

# Test Cases
# x = 5
# print "yikes(5) =", yikes(x)

# ********** Exercise 2.4 **********

## 1 - rand_divis_3 function
##### YOUR CODE HERE #####
def rand_divis_3():
    import math
    import random
    x = random.randint(0, 100)
    if x % 3 == 0:
      return True
    else:
      return False
    
    

# Test Cases
##### YOUR CODE HERE #####

## 2 - roll_dice function - remember that a die's lowest number is 1;
                            #its highest is the number of sides it has

##### YOUR CODE HERE #####
def roll_dice(s, n):
    import random
    while (n!=0):
        print random.randint(1, s)
        n = n-1
        print "Thats all folks!!"
# Test Cases
roll_dice(6,3)
roll_dice(10, 100)
roll_dice(5, 3)

##### YOUR CODE HERE #####                            


# ********** Exercise 2.5 **********

# code for roots function
def roots(a, b, c):
    import math
    d = b**2 - 4*a*c
    if d<0:
      print "The roots are complex.Cannot proceed further."
      exit()
    else
    r1 = (-b + d**0.5)/(2*a)
    r2 = (-b - d**0.5)/(2*a)
    print "The roots of the equation are %r and %r" %(r1, r2)
# Test Cases
##### YOUR CODE HERE #####   
