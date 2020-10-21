# Window ops
> Naive and fast implementations of common window operations.


This library is intended to be used as a replacement to `pd.rolling` and `pd.expanding` to gain a speedup by operating on numpy arrays and avoiding input checks.

## Install

`pip install window-ops`

## How to use

### Rolling

Simply use `rolling_{op}` with a one dimensional `np.ndarray` by specifying the window size and the minimum number of samples to compute the operation (by default `min_samples` equals `window_size`). The result will have `min_samples` - 1 `np.nan`'s at the beggining of the array.

```python
import numpy as np
import pandas as pd
from window_ops.rolling import *
from window_ops.expanding import *

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

    2.63 µs ± 104 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)


```python
ys = pd.Series(y)

%timeit ys.rolling(8).mean()
```

    339 µs ± 16.8 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)


### Expanding

Simply use `expanding_{op}` with a one dimensional `np.ndarray`. For `expanding_std` the first value in the output array is `np.nan`, for all the other operations a full array is returned.

```python
y = np.random.rand(10)
y
```




    array([0.58231973, 0.10747257, 0.2875445 , 0.45670363, 0.02095007,
           0.41161551, 0.48945864, 0.24367788, 0.588639  , 0.75324012])



```python
expanding_mean(y)
```




    array([0.58231974, 0.34489614, 0.32577893, 0.3585101 , 0.2909981 ,
           0.311101  , 0.33658066, 0.3249678 , 0.35426462, 0.39416218],
          dtype=float32)



```python
ys = pd.Series(y)
ys.expanding().mean().values
```




    array([0.58231973, 0.34489615, 0.32577893, 0.35851011, 0.2909981 ,
           0.311101  , 0.33658066, 0.32496782, 0.35426461, 0.39416216])



```python
y = np.random.rand(1_000)

%timeit expanding_mean(y)
```

    1.92 µs ± 58.7 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)


```python
%timeit ys.expanding().mean()
```

    294 µs ± 19.1 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

