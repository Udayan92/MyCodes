while(1):
    print "This program will run a function now.."
    print "Enter y/Y to continue, or q/Q to exit."
    ans = raw_input()
    
    if(ans == 'y' or ans == 'Y'):
        print "Enter a number.."
        num = int(raw_input())
        
        def collatz(x):
            while(x != 1):
                if(x%2 == 0):
                    x = (x//2)
                    print(x)
                else:
                    x = ((x*3) + 1)
                    print(x)
            else:
                print(x)
                print "Finished.."

        collatz(num)

    elif(ans == 'q' or ans == 'Q'):
        print "Exiting.."
        break;
      
    else:
        print "Enter the correct options, please."
        
