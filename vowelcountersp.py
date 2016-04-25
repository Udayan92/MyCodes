while(1):
    print "This program will count individually the number of vowels in a word"
    print "please enter y/Y to continue or q/Q to quit"
    choice = raw_input()
    
    if(choice == 'y' or choice == 'Y'):
        print "Enter your word please.."
        x = raw_input()
        aA_count = 0
        eE_count = 0
        iI_count = 0
        oO_count = 0
        uU_count = 0

        for i in x:
            if(i == 'a' or i == 'A'):
                aA_count = aA_count + 1
            elif(i == 'e' or i == 'E'):
                eE_count = eE_count + 1
            elif(i == 'o' or i == 'O'):
                oO_count = oO_count + 1
            elif(i == 'i' or i == 'I'):
                iI_count = iI_count + 1
            elif(i == 'u' or i == 'U'):
                uU_count = uU_count + 1
            else:
                pass

        print "The total vowel count is", aA_count+eE_count+iI_count+oO_count+uU_count
        print "Individually, the number of vowels is"
        print "Aa",aA_count
        print "eE",eE_count
        print "iI",iI_count
        print "oO",oO_count
        print "uU",uU_count
        
    elif(choice == 'q' or choice == 'Q'):
        print "Exiting now..."
        break
    
    else:
        print "Please enter the correct options.."


       
         
