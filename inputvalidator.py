while(1):
    print "This is a input validator"
    print "Enter y/Y to continue, or q/Q to quit"
    
    ans = raw_input()
    
    if(ans == 'y' or ans == 'Y'):
        while(1):
            try:
                print "Enter a number please.."
                x = int(raw_input())
                break
            except ValueError:
                print "You did not enter a number.."
        print "A number was entered..."                 
           
    elif(ans == 'q' or ans == 'Q'):
        print "Exiting now..."
        break 
    else:
        print "Enter the correct options please.." 
      
