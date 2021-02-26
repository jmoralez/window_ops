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
display_dataframe(times)
```




|                         |   window_ops |   pandas |
|:------------------------|-------------:|---------:|
| rolling_mean            |         0    |     0.33 |
| rolling_max             |         0.01 |     0.37 |
| rolling_min             |         0.01 |     0.32 |
| rolling_std             |         0.01 |     0.33 |
| expanding_mean          |         0    |     0.31 |
| expanding_max           |         0.01 |     0.32 |
| expanding_min           |         0.01 |     0.32 |
| expanding_std           |         0.01 |     0.33 |
| seasonal_rolling_mean   |         0.01 |     3.78 |
| seasonal_rolling_max    |         0.03 |     3.85 |
| seasonal_rolling_min    |         0.02 |     3.8  |
| seasonal_rolling_std    |         0.02 |     3.93 |
| seasonal_expanding_mean |         0.01 |     3.73 |
| seasonal_expanding_max  |         0.24 |     3.86 |
| seasonal_expanding_min  |         0.22 |     3.83 |
| seasonal_expanding_std  |         0.02 |     3.86 |



```python
display_dataframe(speedups)
```




|                         |   times faster |
|:------------------------|---------------:|
| rolling_mean            |         122.05 |
| rolling_max             |          29.85 |
| rolling_min             |          23.45 |
| rolling_std             |          64.31 |
| expanding_mean          |         104.72 |
| expanding_max           |          22.17 |
| expanding_min           |          23.35 |
| expanding_std           |          40.69 |
| seasonal_rolling_mean   |         275.68 |
| seasonal_rolling_max    |         148.73 |
| seasonal_rolling_min    |         154.22 |
| seasonal_rolling_std    |         229.91 |
| seasonal_expanding_mean |         267.48 |
| seasonal_expanding_max  |          16.25 |
| seasonal_expanding_min  |          17.34 |
| seasonal_expanding_std  |         212.16 |


