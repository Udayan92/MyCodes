print "Enter the month of the year.#1 month is march"
a = raw_input()
a1 = int(a)
print "Enter the day of the month."
b = raw_input()
b1 = int(b)
print "Enter the year of the century."
c = raw_input()
c1 = int(c)
print "Enter the century."
d = raw_input()
d1 = int(d)

w = (13*a1 - 1)/5
x = c1/4
y = d1/4
z = w + x + y + b1 + c1 - 2*d1
r = z%7

print "Your day was on %d day of the week" %r



