# Window ops
> Naive and fast implementations of common window operations.


This library is intended to be used as an alternative to `pd.Series.rolling` and `pd.Series.expanding` to gain a speedup by using numba optimized functions operating on numpy arrays and avoiding input checks. There are also online classes for more efficient updates of window statistics.

## Install

`pip install window-ops`

## How to use

For a transformations `n_samples` -> `n_samples` you can use `{[seasonal_](rolling|expanding)}_{(mean|max|min|std)}` on an array.

#### Benchmarks

```python
n_samples = 1_000  # array size
window_size = 8  # for rolling operations
season_length = 7  # for seasonal operations
execute_times = 1_000 # number of times each function will be executed
```

Average times in milliseconds.

```python
display_dataframe(times, fmt='{:.2f}')
```




|                         |   window_ops |   pandas |
|:------------------------|-------------:|---------:|
| rolling_mean            |         0    |     0.19 |
| rolling_max             |         0.01 |     0.2  |
| rolling_min             |         0.01 |     0.2  |
| rolling_std             |         0.01 |     0.22 |
| expanding_mean          |         0    |     0.13 |
| expanding_max           |         0.01 |     0.14 |
| expanding_min           |         0.01 |     0.13 |
| expanding_std           |         0.01 |     0.15 |
| seasonal_rolling_mean   |         0.01 |     2.99 |
| seasonal_rolling_max    |         0.02 |     2.68 |
| seasonal_rolling_min    |         0.02 |     2.64 |
| seasonal_rolling_std    |         0.02 |     2.84 |
| seasonal_expanding_mean |         0.02 |     2.36 |
| seasonal_expanding_max  |         0.02 |     2.19 |
| seasonal_expanding_min  |         0.02 |     2.24 |
| seasonal_expanding_std  |         0.02 |     2.43 |



```python
display_dataframe(speedups, fmt='{:.0f}')
```




|                         |   times faster |
|:------------------------|---------------:|
| rolling_mean            |             89 |
| rolling_max             |             16 |
| rolling_min             |             15 |
| rolling_std             |             38 |
| expanding_mean          |             55 |
| expanding_max           |             11 |
| expanding_min           |             10 |
| expanding_std           |             17 |
| seasonal_rolling_mean   |            204 |
| seasonal_rolling_max    |            110 |
| seasonal_rolling_min    |            111 |
| seasonal_rolling_std    |            161 |
| seasonal_expanding_mean |            156 |
| seasonal_expanding_max  |            127 |
| seasonal_expanding_min  |            130 |
| seasonal_expanding_std  |            119 |


