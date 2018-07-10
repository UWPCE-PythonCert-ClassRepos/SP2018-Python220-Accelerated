"""
I wanted to install pypy and test the difference
with this simple script using the Fibonacci
function we created earlier this class. However,
I was met with errors which I appended at the bottom.
Using regular cPython this script runs in 4.7 seconds.
I tried creeating a virtual environment using python
and the code from here:
http://doc.pypy.org/en/latest/install.html#using-a-packaged-pypy
"""
from timeit import timeit as timer
import random

def fib(i=0):
    j = 1
    while True:
        yield j
        h = i
        i = j
        j = h + i

random.seed(10)
print('Running calculation of 1000 different Fibonacci numbers')
print(timer('s = [fib(1000//random.random()) for i in range(10)]', globals=globals()))




# ssouk@DESKTOP-9LI20UR MINGW64 ~/Documents/Python/Python Programming 220 AC/Lesson10/lesson10_assignment
# $ mkvirtualenv -p /c/pypy3/pypy3 pypy_env
# Running virtualenv with interpreter C:/pypy3/pypy3.exe
# Using base prefix 'C:\\pypy3'
# New pypy executable in C:\Users\ssouk\.virtualenvs\pypy_env\bin\pypy3.exe
# Also creating executable in C:\Users\ssouk\.virtualenvs\pypy_env\bin\pypy.exe
# Installing setuptools, pip, wheel...
#   Complete output from command C:\Users\ssouk\.virt...py_env\bin\pypy3.exe - setuptools pip wheel:
#   RPython traceback:
#   File "pypy_interpreter.c", line 42299, in BuiltinCode1_fastcall_1
#   File "pypy_module_posix.c", line 4913, in get_terminal_size
# Traceback (most recent call last):
#   File "<stdin>", line 27, in <module>
#   File "c:\program files\python36\lib\site-packages\virtualenv_support\pip-10.0.1-py2.py3-none-any.whl\pip\_internal\__init__.py", line 232, in main
#     cmd_name, cmd_args = parseopts(args)
#   File "c:\program files\python36\lib\site-packages\virtualenv_support\pip-10.0.1-py2.py3-none-any.whl\pip\_internal\__init__.py", line 172, in parseopts
#     parser = create_main_parser()
#   File "c:\program files\python36\lib\site-packages\virtualenv_support\pip-10.0.1-py2.py3-none-any.whl\pip\_internal\__init__.py", line 144, in create_main_parser
#     'formatter': UpdatingDefaultsHelpFormatter(),
#   File "c:\program files\python36\lib\site-packages\virtualenv_support\pip-10.0.1-py2.py3-none-any.whl\pip\_internal\baseparser.py", line 25, in __init__
#     kwargs['width'] = get_terminal_size()[0] - 2
#   File "c:\program files\python36\lib\site-packages\virtualenv_support\pip-10.0.1-py2.py3-none-any.whl\pip\_internal\compat.py", line 204, in get_terminal_size
#     return tuple(shutil.get_terminal_size())
#   File "C:\Users\ssouk\.virtualenvs\pypy_env\lib-python\3\shutil.py", line 1078, in get_terminal_size
#     size = os.get_terminal_size(sys.__stdout__.fileno())
# SystemError: unexpected internal exception (please report a bug): <WindowsError object at
# 0x4639238>; internal traceback was dumped to stderr
# ----------------------------------------
# ...Installing setuptools, pip, wheel...done.
# Traceback (most recent call last):
#   File "c:\program files\python36\lib\site-packages\virtualenv.py", line 2343, in <module>
#     main()
#   File "c:\program files\python36\lib\site-packages\virtualenv.py", line 712, in main
#     symlink=options.symlink)
#   File "c:\program files\python36\lib\site-packages\virtualenv.py", line 947, in create_environment    download=download,
#   File "c:\program files\python36\lib\site-packages\virtualenv.py", line 904, in install_wheel
#     call_subprocess(cmd, show_stdout=False, extra_env=env, stdin=SCRIPT)  File "c:\program files\python36\lib\site-packages\virtualenv.py", line 796, in call_subprocess
#     % (cmd_desc, proc.returncode))
# OSError: Command C:\Users\ssouk\.virt...py_env\bin\pypy3.exe - setuptools pip wheel failed with error code 1
# ssouk@DESKTOP-9LI20UR MINGW64 ~/Documents/Python/Python Programming 220 AC/Lesson10/lesson10_assignment
# $ python factorial_pypy.pyRunning factorial(10000)

# ssouk@DESKTOP-9LI20UR MINGW64 ~/Documents/Python/Python Programming 220 AC/Lesson10/lesson10_assignment$ python fib_pypy.py
# Running calculation of 1000 different Fibonacci numbers
# 4.756364268184982
