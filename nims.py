# Name:
# Section:
# nims.py
def play_nims(pile, max_stones):
    '''
    An interactive two-person game; also known as Stones.
    @param pile: the number of stones in the pile to start
    @param max_stones: the maximum number of stones you can take on one turn
    '''
    
    if max_stones > pile:
      print "You cannot bite off more than you can chew,mate."
    else:
      pile = pile - max_stones
      print "There are currently %d stones in the pile." % pile
    if pile == 0:
      print "You win"
      exit()
      
print "How much of a big pile we will have?"
pile1 = raw_input()
pile = int(pile1)
while (isinstance(pile, int) == True):
    print "You first, player1"
    print "How many stones can you pick up at a time,player1?"
    max_stones11 = raw_input()
    max_stones1 = int(max_stones11)
    play_nims(pile, max_stones1)
    pile = pile - max_stones1
    print "And how many stones can *you* pick up at a time,player2?"
    max_stones22 = raw_input()
    max_stones2 = int(max_stones22)
    play_nims(pile, max_stones2)
    pile = pile - max_stones2

