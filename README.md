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
pd.__version__
```




    '1.2.3'



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
| rolling_mean            |         0    |     0.17 |
| rolling_max             |         0.01 |     0.19 |
| rolling_min             |         0.01 |     0.23 |
| rolling_std             |         0.01 |     0.22 |
| expanding_mean          |         0    |     0.13 |
| expanding_max           |         0    |     0.13 |
| expanding_min           |         0    |     0.13 |
| expanding_std           |         0.01 |     0.14 |
| seasonal_rolling_mean   |         0    |     2.62 |
| seasonal_rolling_max    |         0.02 |     3.04 |
| seasonal_rolling_min    |         0.02 |     2.85 |
| seasonal_rolling_std    |         0.01 |     2.37 |
| seasonal_expanding_mean |         0    |     1.9  |
| seasonal_expanding_max  |         0.01 |     1.79 |
| seasonal_expanding_min  |         0.01 |     1.81 |
| seasonal_expanding_std  |         0.01 |     2.45 |



```python
display_dataframe(speedups, fmt='{:.0f}')
```




|                         |   times faster |
|:------------------------|---------------:|
| rolling_mean            |             76 |
| rolling_max             |             14 |
| rolling_min             |             21 |
| rolling_std             |             33 |
| expanding_mean          |             44 |
| expanding_max           |             32 |
| expanding_min           |             32 |
| expanding_std           |             19 |
| seasonal_rolling_mean   |            632 |
| seasonal_rolling_max    |            201 |
| seasonal_rolling_min    |            173 |
| seasonal_rolling_std    |            322 |
| seasonal_expanding_mean |            494 |
| seasonal_expanding_max  |            353 |
| seasonal_expanding_min  |            339 |
| seasonal_expanding_std  |            238 |



### Online

If you have an array for which you want to compute a window statistic and then keep updating it as more samples come in you can use the classes in the `window_ops.online` module. They all have a `fit_transform` method which take the array and return the transformations defined above but also have an `update` method that take a single value and return the new statistic.

#### Benchmarks

Average time in milliseconds it takes to transform the array and perform 100 updates.

```python
display_dataframe(times.to_frame(), '{:.2f}')
```




|                       |   average time (ms) |
|:----------------------|--------------------:|
| RollingMean           |                0.07 |
| RollingMax            |                0.09 |
| RollingMin            |                0.09 |
| RollingStd            |                0.24 |
| ExpandingMean         |                0.08 |
| ExpandingMax          |                0.03 |
| ExpandingMin          |                0.02 |
| ExpandingStd          |                0.08 |
| SeasonalRollingMean   |                0.18 |
| SeasonalRollingMax    |                0.14 |
| SeasonalRollingMin    |                0.19 |
| SeasonalRollingStd    |                0.25 |
| SeasonalExpandingMean |                0.09 |
| SeasonalExpandingMax  |                0.06 |
| SeasonalExpandingMin  |                0.06 |
| SeasonalExpandingStd  |                0.09 |


