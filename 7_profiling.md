# Profiling Python

Any measurable resource can be profiled (not just CPU!). You will often end up fixing the wrong thing if you don't profile. First have an hypothesis of what could be the problem and __first profile__ to test, __before making changes to the structure of your code.__

Profiling tipically adds an overhead (10x to 100x slowdowns can be typical).

Some of the resources you can profile are:

- Memory (RAM)
- CPU Time
- Network bandwidth
- Disk I/O

Some techniques for profiling:

- time.time and decorators
- timeit console command disable garbage collection.
- IPython %%time and %%timeit magic functions. 
- cProfile module (built-in) -> High level
- line_profiler -> Line by line execution time.
- perf stat: To know the number of instructions that are executed by the cpu, and how efficiently the cpu caches are utilized.
- heapy: For track all the objects inside Python's memory to hunting down memory leaks.
- dowser: For long running systems via a web browser interface.
- memory_profiler: Help you understand why RAM usage is high.

## time Unix

We get 3 results:
- __real__: real time of execution.
- __user__: amount of time the CPU spent on your task outside kernel functions.
- __sys__: records amount of time spent in kernel-level functions.

How to use it:

```shell
/usr/bin/time -p python python_file.py
```

## cProfile

How to use it:
```shell
python -m cProfile -s cumulative python_file.py
```

```python
import cProfile

def fn():
    print("Hello world!")

cProfile.run('fn()')
```

cProfiler decorator

```python
import cProfile, pstats, io

def profile(fnc):
    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        retval = fnc(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        print(s.getvalue())
        return retval
    return inner
```


## line_profiler

Profiles in line-by-line basis.

To install line_profiler:

```shell
pip install line_profiler
```

```python
from line_profiler import LineProfiler

def rock(rk):
    print(rk)

rk = "Hello World!"
profile = LineProfiler(rock(rk))

print(profile)
```

## memory_profiler

Memory profiler will make your code run 10x to 100x times slower. Installing psutil makes memory_profiler run faster.
To install memory_profiler:

```shell
pip install psutil memory_profiler
```

## heapy

To look the number and size of each object on Python's heap.
To install heapy:

```shell
pip install guppy
```

## dis

Inspect the underlying bytecode that is running inside the stack-based CPython virtual machine. It help to understand why some styles of code are more faster than others.

More lines of bytecode will execute more slowly.

dis is a built-in module.