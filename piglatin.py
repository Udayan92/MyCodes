while(1):
    print "Enter a string to see its pig latin version, or q/Q to quit.."
    x = raw_input()
    
    if(x == 'q' or x == 'Q'):
        break
    
    else:
        x_start = x[0]
        x_len = len(x)

        if(x_start == 'a' or x_start == 'e' or x_start =='i' or x_start=='o' or x_start=='u'):
            x_pl = x + "yay"
        else:
            x_pl = x[1:x_len]+x[0]+"ay"
        
        print "The pig latin translation is", x_pl
