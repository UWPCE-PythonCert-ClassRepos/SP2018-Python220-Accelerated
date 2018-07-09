#=========================================================================================
#Name: Generators
#Author: Wesley Wang
#Date: 5/29/2018
#=========================================================================================

def intsum():
  pos = 0
  total = 0
  while True:
    total += pos
    yield total
    pos += 1

def doubler():
  pwr = 0
  while True:
    yield 2 ** pwr
    pwr += 1

def fib():
  prev = 0
  current = 1
  while True:
    yield current
    prev, current = current, prev + current

def check_prime(number):
  for divisor in range(2, int(number ** 0.5) + 1):
    if number % divisor == 0:
      return False
  return True

def prime():
  pos = 1
  while True:
    pos += 1
    if check_prime(pos):
        yield pos
