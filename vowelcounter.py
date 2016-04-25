while(1):
    print "This program will count the number of vowels in a given word."
    print "Please press y/Y to continue or q/Q to quit"
    choice = raw_input()
    
    if(choice == 'y' or choice =='Y'):
        print "Enter the word please.."
        word = raw_input()
        vowels = 0
            
        for i in word:
            if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
                vowels = vowels + 1;
            else:
                pass
           
        print "The given word has the number of vowels", vowels

  
    elif(choice == 'q' or choice == 'Q'):
        print "Exiting now...."
        break

    else:
        print "Invalid input entered.."

  
        
  
