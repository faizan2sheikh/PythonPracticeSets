#only option c and d will work
#a.
#import mymod
#print(increment(4)) # Supposed to print 5
#b.
#import from mymod import increment
#print(increment(4)) # Supposed to print 5
#c.
import mymod
print(mymod.increment(4)) # Supposed to print 5
#d.
from mymod import increment
print(mymod.increment(4)) # Supposed to print 5