# Window ops
> Naive and fast implementations of common window operations.


This library is intended to be used as a replacement to `pd.rolling` and `pd.expanding` to gain a speedup by operating on numpy arrays and avoiding input checks.

## Install

`pip install window-ops`

## How to use

### Rolling

Simply use `rolling_{op}` with a one dimensional `np.ndarray` by specifying the window size and the minimum number of samples to compute the operation (by default `min_samples` equals `window_size`). The result will have `min_samples` - 1 `np.nan`'s at the beggining of the array.

```python
import random

import numpy as np
import pandas as pd
from window_ops.rolling import *
from window_ops.expanding import *
from window_ops.ewm import *

np.random.seed(0)
random.seed(0)
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
big_y = np.random.rand(1_000)

%timeit rolling_mean(big_y, window_size=8)
```

    2.53 µs ± 84 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)


```python
big_ys = pd.Series(big_y)

%timeit big_ys.rolling(8).mean()
```

    305 µs ± 11.9 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)


### Expanding

Simply use `expanding_{op}` with a one dimensional `np.ndarray`. For `expanding_std` the first value in the output array is `np.nan`, for all the other operations a full array is returned.

```python
y
```




    array([0.5488135 , 0.71518937, 0.60276338, 0.54488318, 0.4236548 ,
           0.64589411, 0.43758721, 0.891773  , 0.96366276, 0.38344152])



```python
expanding_mean(y)
```




    array([0.5488135 , 0.63200146, 0.62225544, 0.60291237, 0.5670608 ,
           0.5801997 , 0.5598265 , 0.6013198 , 0.64158016, 0.6157663 ],
          dtype=float32)



```python
ys.expanding().mean().values
```




    array([0.5488135 , 0.63200144, 0.62225542, 0.60291236, 0.56706085,
           0.58019972, 0.55982651, 0.60131982, 0.64158015, 0.61576628])



```python
%timeit expanding_mean(big_y)
```

    1.87 µs ± 50.5 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)


```python
%timeit big_ys.expanding().mean()
```

    325 µs ± 13.5 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)


### EWM

Simply use `ewm_{op}` with a one dimensional `np.ndarray` and the smoothing parameter `alpha`. Currently only `ewm_mean` is implemented.

```python
y
```




    array([0.5488135 , 0.71518937, 0.60276338, 0.54488318, 0.4236548 ,
           0.64589411, 0.43758721, 0.891773  , 0.96366276, 0.38344152])



```python
alpha = random.random()
alpha
```




    0.8444218515250481



```python
ewm_mean(y, alpha=alpha)
```




    array([0.5488135 , 0.68930495, 0.6162273 , 0.55598277, 0.44424215,
           0.6145215 , 0.46511433, 0.8253942 , 0.9421512 , 0.47036454],
          dtype=float32)



```python
ys.ewm(alpha=alpha, adjust=False).mean().values
```




    array([0.5488135 , 0.68930492, 0.61622735, 0.55598278, 0.44424214,
           0.61452147, 0.46511432, 0.82539423, 0.9421512 , 0.47036454])



```python
%timeit ewm_mean(big_y, alpha)
```

    5.56 µs ± 62.6 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)


```python
%timeit big_ys.ewm(alpha=alpha, adjust=False).mean().values
```

    302 µs ± 13 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

