# mx={}
# def fibx(index):
#         if index==1 or index==2:
#             return 1
#         if index in mx:
#             return mx[index]
#         t=fibx(index-1)+fibx(index-2)
#         mx[index]=t
#         return t
# print(fibx(1434))


# Function for nth fibonacci number - Dynamic Programming
# Taking 1st two fibonacci numbers as 0 and 1

# FibArray = [0, 1]

# def fibonacci(n):
# 	if n<0:
# 		print("Incorrect input")
# 	elif n<= len(FibArray):
# 		return FibArray[n-1]
# 	else:
# 		temp_fib = fibonacci(n-1)+fibonacci(n-2)
# 		FibArray.append(temp_fib)
# 		return temp_fib

# # Driver Program

# print(fibonacci(1434))
# To find the n-th Fibonacci Number using formula
from math import sqrt
# import square-root method from math library
def nthFib(n):
	res = (((1+sqrt(5))**n)-((1-sqrt(5)))**n)/(2**n*sqrt(5))
	return res
	# format and print the number
	
# driver code
# for i in range(50):
# 	t=nthFib(i)
# 	if t>=100000:
# 		break
# print(i)
print(nthFib(25))

# This code is contributed by Kush Mehta
