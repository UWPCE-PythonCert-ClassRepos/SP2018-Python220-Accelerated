# cPython activity on great circle
# Enter the below in terminal to get a report that looks like this:
"""
# profiling original version
270000219 function calls in 85.587 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:103(release)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:143(__init__)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:147(__enter__)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:151(__exit__)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:157(_get_module_lock)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:176(cb)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:211(_call_with_frames_removed)
       19    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:222(_verbose_message)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:307(__init__)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:311(__enter__)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:318(__exit__)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:321(<genexpr>)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:369(__init__)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:403(cached)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:416(parent)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:424(has_location)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:504(_init_module_attrs)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:564(module_from_spec)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:58(__init__)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:651(_load_unlocked)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:707(find_spec)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:78(acquire)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:780(find_spec)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:843(__enter__)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:847(__exit__)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:870(_find_spec)
        1    0.000    0.000    0.001    0.001 <frozen importlib._bootstrap>:936(_find_and_load_unlocked)
        1    0.000    0.000    0.001    0.001 <frozen importlib._bootstrap>:966(_find_and_load)
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1080(_path_importer_cache)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1117(_get_spec)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1149(find_spec)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1228(_get_spec)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1233(find_spec)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:361(_get_cached)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:37(_relax_case)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:524(spec_from_file_location)
       16    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:57(_path_join)
       16    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:59(<listcomp>)
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:75(_path_stat)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:85(_path_is_mode_type)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:908(__init__)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:919(create_module)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:927(exec_module)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:94(_path_isfile)
        1    8.712    8.712   85.587   85.587 great_circle.py:20(<module>)
 10000000   13.711    0.000   20.125    0.000 great_circle.py:25(great_circle_raw)
 20000000   21.266    0.000   34.035    0.000 great_circle.py:37(calculate_acos)
 10000000    5.502    0.000   22.429    0.000 great_circle.py:41(great_circle_acos)
 10000000    1.885    0.000    1.885    0.000 great_circle.py:54(calculate_x)
 20000000    2.859    0.000    2.859    0.000 great_circle.py:58(calculate_coordinate)
 10000000    1.403    0.000    1.403    0.000 great_circle.py:62(calculate_theta)
 10000000   11.066    0.000   34.320    0.000 great_circle.py:66(great_circle_factored)
        5    0.000    0.000    0.000    0.000 {built-in method _imp.acquire_lock}
        1    0.000    0.000    0.000    0.000 {built-in method _imp.create_dynamic}
        1    0.000    0.000    0.000    0.000 {built-in method _imp.exec_dynamic}
        1    0.000    0.000    0.000    0.000 {built-in method _imp.is_builtin}
        1    0.000    0.000    0.000    0.000 {built-in method _imp.is_frozen}
        5    0.000    0.000    0.000    0.000 {built-in method _imp.release_lock}
        2    0.000    0.000    0.000    0.000 {built-in method _thread.allocate_lock}
        2    0.000    0.000    0.000    0.000 {built-in method _thread.get_ident}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.any}
        1    0.000    0.000   85.587   85.587 {built-in method builtins.exec}
        6    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
        6    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
        5    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
 30000000    3.338    0.000    3.338    0.000 {built-in method math.acos}
 90000000    9.119    0.000    9.119    0.000 {built-in method math.cos}
 60000000    6.727    0.000    6.727    0.000 {built-in method math.sin}
        1    0.000    0.000    0.000    0.000 {built-in method posix.fspath}
        2    0.000    0.000    0.000    0.000 {built-in method posix.getcwd}
        5    0.000    0.000    0.000    0.000 {built-in method posix.stat}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        2    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
        2    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
       16    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
        6    0.000    0.000    0.000    0.000 {method 'rpartition' of 'str' objects}
       32    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}

# more simplified version from below:
12000220 function calls in 3.567 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:103(release)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:143(__init__)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:147(__enter__)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:151(__exit__)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:157(_get_module_lock)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:176(cb)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:211(_call_with_frames_removed)
       19    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:222(_verbose_message)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:307(__init__)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:311(__enter__)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:318(__exit__)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:321(<genexpr>)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:369(__init__)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:403(cached)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:416(parent)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:424(has_location)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:504(_init_module_attrs)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:564(module_from_spec)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:58(__init__)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:651(_load_unlocked)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:707(find_spec)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:78(acquire)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:780(find_spec)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:843(__enter__)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:847(__exit__)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:870(_find_spec)
        1    0.000    0.000    0.001    0.001 <frozen importlib._bootstrap>:936(_find_and_load_unlocked)
        1    0.000    0.000    0.001    0.001 <frozen importlib._bootstrap>:966(_find_and_load)
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1080(_path_importer_cache)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1117(_get_spec)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1149(find_spec)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1228(_get_spec)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1233(find_spec)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:361(_get_cached)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:37(_relax_case)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:524(spec_from_file_location)
       16    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:57(_path_join)
       16    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:59(<listcomp>)
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:75(_path_stat)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:85(_path_is_mode_type)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:908(__init__)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:919(create_module)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:927(exec_module)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:94(_path_isfile)
  2000000    0.220    0.000    0.220    0.000 great_circle_cpython.py:13(calculate_coordinate)
  1000000    0.125    0.000    0.125    0.000 great_circle_cpython.py:17(calculate_theta)
  1000000    1.078    0.000    1.718    0.000 great_circle_cpython.py:21(calculate_acos)
  1000000    1.067    0.000    3.296    0.000 great_circle_cpython.py:25(great_circle_factored)
        1    0.270    0.270    3.566    3.566 great_circle_cpython.py:35(main)
        1    0.000    0.000    3.567    3.567 great_circle_cpython.py:6(<module>)
  1000000    0.165    0.000    0.165    0.000 great_circle_cpython.py:9(calculate_x)
        5    0.000    0.000    0.000    0.000 {built-in method _imp.acquire_lock}
        1    0.000    0.000    0.000    0.000 {built-in method _imp.create_dynamic}
        1    0.000    0.000    0.000    0.000 {built-in method _imp.exec_dynamic}
        1    0.000    0.000    0.000    0.000 {built-in method _imp.is_builtin}
        1    0.000    0.000    0.000    0.000 {built-in method _imp.is_frozen}
        5    0.000    0.000    0.000    0.000 {built-in method _imp.release_lock}
        2    0.000    0.000    0.000    0.000 {built-in method _thread.allocate_lock}
        2    0.000    0.000    0.000    0.000 {built-in method _thread.get_ident}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.any}
        1    0.000    0.000    3.567    3.567 {built-in method builtins.exec}
        6    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
        6    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
        5    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
  1000000    0.110    0.000    0.110    0.000 {built-in method math.acos}
  3000000    0.305    0.000    0.305    0.000 {built-in method math.cos}
  2000000    0.224    0.000    0.224    0.000 {built-in method math.sin}
        1    0.000    0.000    0.000    0.000 {built-in method posix.fspath}
        2    0.000    0.000    0.000    0.000 {built-in method posix.getcwd}
        5    0.000    0.000    0.000    0.000 {built-in method posix.stat}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        2    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
        2    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
       16    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
        6    0.000    0.000    0.000    0.000 {method 'rpartition' of 'str' objects}
       32    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}
"""
# Enter the below in Terminal
# $ python -m cProfile great_circle.py



import math
lon1, lat1, lon2, lat2 = -72.345, 34.323, -61.823, 54.826

def calculate_x():
    return math.pi / 180.0


def calculate_coordinate(lat, x):
    return (90.0 - lat) * x


def calculate_theta(lon2, lon1, x):
    return (lon2 - lon1) * x


def calculate_acos(a, b, theta):
    return math.acos((math.cos(a) * math.cos(b)) + (math.sin(a) * math.sin(b) * math.cos(theta)))


def great_circle_factored(lon1, lat1, lon2, lat2):
    radius = 3956  # miles
    x = calculate_x()
    a = calculate_coordinate(lat1, x)
    b = calculate_coordinate(lat2, x)
    theta = calculate_theta(lon2, lon1, x)
    c = calculate_acos(a, b, theta)
    return radius * c


def main():
    for i in range(1000000):
        great_circle_factored(lon1, lat1, lon2, lat2)

if __name__ == "__main__":
    main()