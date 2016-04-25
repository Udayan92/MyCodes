while(1):
    print "This is a word counter.Press y/Y to continue or q/Q to exit.."
    choice = raw_input()
    
    if(choice == 'y' or choice == 'Y'):
        print "how many words does your sentence have..?"
        num = int(raw_input())
        print "Enter the sentence, please."
        sentence = []
        for i in range(num):
            tmp = raw_input()
            sentence.append(tmp)
            i = i + 1
     
        count = {}
         
        for x in sentence:
            if x in count.keys():
                count[x] = count[x] + 1
            else:
                count[x] = 1
      
        print "The words and their count is..", count
     
    elif(choice == 'q' or choice == 'Q'):
        print "Exiting now..."
        break
    
    else:
        print "Please enter the correct options..."
