# Window ops
> Naive and fast implementations of common window operations.


This library is intended to be used as an alternative to `pd.Series.rolling` and `pd.Series.expanding` to gain a speedup by using numba optimized functions operating on numpy arrays. There are also online classes for more efficient updates of window statistics.

## Install

`pip install window-ops`

## How to use

### Transformations

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
| rolling_mean            |         0    |     0.21 |
| rolling_max             |         0.01 |     0.2  |
| rolling_min             |         0.01 |     0.21 |
| rolling_std             |         0.01 |     0.22 |
| expanding_mean          |         0    |     0.12 |
| expanding_max           |         0    |     0.14 |
| expanding_min           |         0    |     0.13 |
| expanding_std           |         0.01 |     0.15 |
| seasonal_rolling_mean   |         0.02 |     2.62 |
| seasonal_rolling_max    |         0.02 |     2.56 |
| seasonal_rolling_min    |         0.02 |     2.66 |
| seasonal_rolling_std    |         0.02 |     2.95 |
| seasonal_expanding_mean |         0.02 |     2.42 |
| seasonal_expanding_max  |         0.02 |     2.27 |
| seasonal_expanding_min  |         0.02 |     2.25 |
| seasonal_expanding_std  |         0.02 |     2.47 |



```python
display_dataframe(speedups, fmt='{:.0f}')
```




|                         |   times faster |
|:------------------------|---------------:|
| rolling_mean            |             88 |
| rolling_max             |             17 |
| rolling_min             |             17 |
| rolling_std             |             42 |
| expanding_mean          |             52 |
| expanding_max           |             31 |
| expanding_min           |             30 |
| expanding_std           |             18 |
| seasonal_rolling_mean   |            172 |
| seasonal_rolling_max    |            103 |
| seasonal_rolling_min    |            107 |
| seasonal_rolling_std    |            160 |
| seasonal_expanding_mean |            151 |
| seasonal_expanding_max  |            138 |
| seasonal_expanding_min  |            125 |
| seasonal_expanding_std  |            123 |



### Online

If you have an array for which you want to compute a window statistic and then keep updating it as more samples come in you can use the classes in the `window_ops.online` module. They all have a `fit_transform` method which take the array and return the transformations defined above but also have an `update` method that take a single value and return the new statistic.

#### Benchmarks

Average time in milliseconds it takes to transform the array and perform 100 updates.

```python
display_dataframe(times.to_frame(), '{:.2f}')
```




|                       |   average time (ms) |
|:----------------------|--------------------:|
| RollingMean           |                0.06 |
| RollingMax            |                0.08 |
| RollingMin            |                0.07 |
| RollingStd            |                0.09 |
| ExpandingMean         |                0.07 |
| ExpandingMax          |                0.02 |
| ExpandingMin          |                0.02 |
| ExpandingStd          |                0.07 |
| SeasonalRollingMean   |                0.12 |
| SeasonalRollingMax    |                0.14 |
| SeasonalRollingMin    |                0.13 |
| SeasonalRollingStd    |                0.15 |
| SeasonalExpandingMean |                0.13 |
| SeasonalExpandingMax  |                0.07 |
| SeasonalExpandingMin  |                0.09 |
| SeasonalExpandingStd  |                0.13 |


