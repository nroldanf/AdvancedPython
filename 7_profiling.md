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

## line_profiler
To install line_profiler:

```shell
pip install line_profiler
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

dis is a built-in module.