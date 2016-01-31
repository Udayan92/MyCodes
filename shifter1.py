print "Enter the letter"
c = raw_input()
print "Enter the position to be shifted"
s1 = raw_input()
s = int(s1)

ascii_code = ord(c)
ascii_code1 = ascii_code + s

letter_res1 = chr(ascii_code1)

print "The shifted letter is %s" %letter_res1

