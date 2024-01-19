# An Efficient Method to count squares between a
# and b
import math
def CountSquares(a, b):
	return (math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1)

# Driver Code
a = 11111
b = 99999
print ("Count of squares is:", int(CountSquares(a, b)))
for j in range(math.ceil(math.sqrt(a)),math.floor(math.sqrt(b))+1):
    print(j)
