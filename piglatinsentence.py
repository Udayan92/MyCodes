while(1):
    print "Enter y or Y to enter a sentence, or q/Q to quit"
    x = raw_input()
    if(x == 'y' or x == 'Y'):
        print "how many words does your sentence have?"
        num = int(raw_input())
        print "enter your sentence please.."
        sentence = []
       
        for i in range(num):
            tmp = raw_input()
            sentence.append(tmp)
            i = i+1
     
        sentence_pl = []    

        for j in sentence:
            if(j[0] =='a' or j[0] == 'e' or j[0] == 'i' or j[0] == 'o' or j[0] =='u'):
                j_pl = j + "yay"
                sentence_pl.append(j_pl)
            else:
                j_pl = j[1:len(j)]+j[0]+"ay"     
                sentence_pl.append(j_pl)
            
        print "Your sentence in pig latin is",sentence_pl
          
    elif(x == 'q' or x == 'Q'):
        break
    
    else:
        print "Invalid input entered.Exiting...."
        break     
