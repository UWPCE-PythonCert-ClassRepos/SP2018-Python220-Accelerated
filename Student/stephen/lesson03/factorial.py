## >>> from factorial import factorial
## >>> factorial(4)

def factorial(n):
	if n==1:
	   return 1
	return n*factorial(n-1)

# Tests:
# In [2]: factorial(10)
# Out[2]: 3628800

# In [3]: factorial(5)
# Out[3]: 120

# In [4]: factorial(5) / factorial(3)
# Out[4]: 20.0