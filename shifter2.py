print "Enter the phrase to be encoded"
c = raw_input()
print "Enter the shift value."
s1 = raw_input()
s = int(s1)

for z1 in c:
   ascii_code = ord(z1)
   ascii_code1 = ascii_code + s
   letter_res = chr(ascii_code1)
   print "Encrypted phase is %s" %letter_res




 
