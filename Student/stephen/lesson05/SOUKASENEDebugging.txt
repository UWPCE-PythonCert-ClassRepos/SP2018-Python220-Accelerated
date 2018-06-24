import sys


def my_fun(n):
    if n == 2:
        return True
    # to get the desired result need to include
    # another termination case like below
    elif n < 2:
        return False

    return my_fun(n/2)

if __name__ == '__main__':
    n = int(sys.argv[1])
    print(my_fun(n))



# results from debugging:
# As we go deeper into the recursion using 15 as n
# we see that n eventually just keeps dividing the results by 2
# and never reaches an end. We need something to terminate the function
# and return False once n goes below 2

# $ python -m pdb recursive.py 15
# > c:\users\ssouk\documents\python\python programming 220 ac\lesson05\recursive.py(1)<module>()
# -> import sys
# (Pdb) n
# > c:\users\ssouk\documents\python\python programming 220 ac\lesson05\recursive.py(4)<module>()
# -> def my_fun(n):
# (Pdb) n
# > c:\users\ssouk\documents\python\python programming 220 ac\lesson05\recursive.py(10)<module>()
# -> if __name__ == '__main__':
# (Pdb) n
# > c:\users\ssouk\documents\python\python programming 220 ac\lesson05\recursive.py(11)<module>()
# -> n = int(sys.argv[1])
# (Pdb) s
# > c:\users\ssouk\documents\python\python programming 220 ac\lesson05\recursive.py(12)<module>()
# -> print(my_fun(n))
# (Pdb) s
# --Call--
# > c:\users\ssouk\documents\python\python programming 220 ac\lesson05\recursive.py(4)my_fun()
# -> def my_fun(n):
# (Pdb) s
# > c:\users\ssouk\documents\python\python programming 220 ac\lesson05\recursive.py(5)my_fun()
# -> if n == 2:
# (Pdb) s
# > c:\users\ssouk\documents\python\python programming 220 ac\lesson05\recursive.py(8)my_fun()
# -> return my_fun(n/2)
# (Pdb) pp n
# 15
# (Pdb) s
# --Call--
# > c:\users\ssouk\documents\python\python programming 220 ac\lesson05\recursive.py(4)my_fun()
# -> def my_fun(n):
# (Pdb) pp n
# 7.5
# (Pdb) s
# > c:\users\ssouk\documents\python\python programming 220 ac\lesson05\recursive.py(5)my_fun()
# -> if n == 2:
# (Pdb) s
# > c:\users\ssouk\documents\python\python programming 220 ac\lesson05\recursive.py(8)my_fun()
# -> return my_fun(n/2)
# (Pdb) pp n
# 7.5
# (Pdb) s
# --Call--
# > c:\users\ssouk\documents\python\python programming 220 ac\lesson05\recursive.py(4)my_fun()
# -> def my_fun(n):
# (Pdb) pp n
# 3.75
# (Pdb) s
# > c:\users\ssouk\documents\python\python programming 220 ac\lesson05\recursive.py(5)my_fun()
# -> if n == 2:
# (Pdb) s
# > c:\users\ssouk\documents\python\python programming 220 ac\lesson05\recursive.py(8)my_fun()
# -> return my_fun(n/2)
# (Pdb) s
# --Call--
# > c:\users\ssouk\documents\python\python programming 220 ac\lesson05\recursive.py(4)my_fun()
# -> def my_fun(n):
# (Pdb) pp n
# 1.875
# (Pdb)


