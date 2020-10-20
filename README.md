# Window ops
> Naive and fast implementations of common window operations.


```python
%load_ext autoreload
%autoreload 2
```

This library is intended to be used as a replacement to `pd.rolling` and `pd.expanding` to gain a speedup by operating on numpy arrays and avoiding input checks.

## Install

`pip install window_ops`

## How to use

Simply use `rolling_{op}` with a one dimensional `np.ndarray` by specifying the window size and the minimum number of samples to compute the operation (by default `min_samples` equals `window_size`). The result will have `min_samples` - 1 `np.nan`'s at the beggining of the array.

```python
import numpy as np
import pandas as pd

np.random.seed(0)
y = np.random.rand(10)
window_size = 3
y
```




    array([0.5488135 , 0.71518937, 0.60276338, 0.54488318, 0.4236548 ,
           0.64589411, 0.43758721, 0.891773  , 0.96366276, 0.38344152])



```python
rolling_mean(y, window_size=window_size)
```




    array([       nan,        nan, 0.62225544, 0.62094533, 0.5237671 ,
           0.53814405, 0.5023787 , 0.6584181 , 0.764341  , 0.7462924 ],
          dtype=float32)



```python
ys = pd.Series(y)
ys.rolling(window_size).mean().values
```




    array([       nan,        nan, 0.62225542, 0.62094531, 0.52376712,
           0.53814403, 0.50237871, 0.65841811, 0.76434099, 0.74629243])



```python
y = np.random.rand(1_000)

%timeit rolling_mean(y, window_size=8)
```

    2.53 µs ± 55.6 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)


```python
ys = pd.Series(y)

%timeit ys.rolling(8).mean()
```

    309 µs ± 19.3 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

