while(1):
    print "Enter a string to reverse, or q if you want to quit.."
    x = raw_input()
    if (x == 'q' or x == 'Q'):
        break;

    else:
        x_len = len(x)
        x_new = x[::-1]
        print "The reversed string is"
        print(x_new)

 

