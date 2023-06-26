<h1 align="center">
  <br>
  <a href="https://amirbahador-hub.github.io/myprofiler/"><img src="small_logo.png" alt="GitM" width="200"></a>
</h1>

<h4 align="center">A minimal profiler for calculating total execution time and memory usage</h4>

<p align="center">
  <a href="https://img.shields.io/badge/test-pass-green">
    <img src="https://img.shields.io/badge/test-pass-brightgreen"
         alt="TestBadge">
  </a>
  <a href="https://img.shields.io/badge/python-3.10-blue">
    <img src="https://img.shields.io/badge/python-3.10-blue"
         alt="PythonVersionBadge">
  </a>


</p>


<p align="center">
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
</p>

## Installation
```bash
pip install myprofiler
```

## Usage
```python
from myprofiler import profile

@profile
def main():
    lt = []
    for i in range(0, 100000):
        lt.append(i)

if __name__ == "__main__":
    main()
```
output:
```bash 
========================================
---- Meta Data ----
Function: main
Method: None
---- Memory Usage ----
Current memory usage:	 936.0B
Peak memory usage:	 3.4MiB
---- Time ----
Total Time:	 0:00:00.039728
seconds:	 0
microseconds:	 39728
========================================
```