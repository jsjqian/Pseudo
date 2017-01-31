print "Hello World!"
print "This is a Pseudo program!"
FOO = 5 + 6 
print "The value of foo is:"
print FOO 
def FOOBAR():
	print "Inside foobar!"
def FOOBAR2(FOO):
	print "Inside foobar2!"
	print "The value of foo is:"
	print FOO 
print FOOBAR()
FOOBAR2(FOO)
print 5 > 6 
print 4 >= 4 
print 4 != 2 
print 5 == 4 
print 12 % 5 
print 4 == 5 and 6 == 6 
print 4 == 5 or 6 == 6 
if 5 == 3 :
	print "This is true!"
elif 5 == 5 :
	print "This is true!"
else: 
	print "None are true"
I = 0 
while I < 5 :
	print I 
	I = I + 1 
for I in range(0,10,2):
	print I 
	if I > 3 :
		print I + 100 
	else: 
		print I - 100 
