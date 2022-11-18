# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/expanding.ipynb.

# %% auto 0
__all__ = ['expanding_mean', 'expanding_std', 'expanding_max', 'expanding_min', 'seasonal_expanding_mean',
           'seasonal_expanding_std', 'seasonal_expanding_min', 'seasonal_expanding_max']

# %% ../nbs/expanding.ipynb 4
from typing import Callable, Optional

import numpy as np
from numba import njit  # type: ignore

from window_ops.rolling import (
    rolling_max,
    rolling_mean,
    rolling_min,
    rolling_std,
    seasonal_rolling_max,
    seasonal_rolling_mean,
    seasonal_rolling_min,
    seasonal_rolling_std,
)

# %% ../nbs/expanding.ipynb 6
@njit
def _expanding_op(
    rolling_op: Callable,
    x: np.ndarray,
    min_samples: int = 1,
    out: Optional[np.ndarray] = None,
) -> np.ndarray:
    n_samples = x.size
    return rolling_op(x, window_size=n_samples, min_samples=min_samples, out=out)

# %% ../nbs/expanding.ipynb 7
@njit
def expanding_mean(
    x: np.ndarray,
    out: Optional[np.ndarray] = None,
) -> np.ndarray:
    return _expanding_op(rolling_mean, x, out=out)

# %% ../nbs/expanding.ipynb 9
@njit
def expanding_std(
    x: np.ndarray,
    out: Optional[np.ndarray] = None,
) -> np.ndarray:
    return _expanding_op(rolling_std, x, min_samples=2, out=out)

# %% ../nbs/expanding.ipynb 11
@njit
def expanding_max(x: np.ndarray, out: Optional[np.ndarray] = None) -> np.ndarray:
    return _expanding_op(rolling_max, x, out=out)

# %% ../nbs/expanding.ipynb 13
@njit
def expanding_min(x: np.ndarray, out: Optional[np.ndarray] = None) -> np.ndarray:
    return _expanding_op(rolling_min, x, out=out)

# %% ../nbs/expanding.ipynb 17
@njit
def _seasonal_expanding_op(
    rolling_op: Callable,
    x: np.ndarray,
    season_length: int,
    min_samples: int = 1,
    out: Optional[np.ndarray] = None,
) -> np.ndarray:
    n_samples = x.size
    return rolling_op(
        x,
        season_length=season_length,
        window_size=n_samples,
        min_samples=min_samples,
        out=out,
    )

# %% ../nbs/expanding.ipynb 18
@njit
def seasonal_expanding_mean(
    x: np.ndarray, season_length: int, out: Optional[np.ndarray] = None
) -> np.ndarray:
    return _seasonal_expanding_op(seasonal_rolling_mean, x, season_length, out=out)

# %% ../nbs/expanding.ipynb 20
@njit
def seasonal_expanding_std(
    x: np.ndarray, season_length: int, out: Optional[np.ndarray] = None
) -> np.ndarray:
    return _seasonal_expanding_op(
        seasonal_rolling_std, x, season_length, min_samples=2, out=out
    )

# %% ../nbs/expanding.ipynb 22
@njit
def seasonal_expanding_min(
    x: np.ndarray, season_length: int, out: Optional[np.ndarray] = None
):
    return _seasonal_expanding_op(seasonal_rolling_min, x, season_length, out=out)

# %% ../nbs/expanding.ipynb 24
@njit
def seasonal_expanding_max(
    x: np.ndarray, season_length: int, out: Optional[np.ndarray] = None
):
    return _seasonal_expanding_op(seasonal_rolling_max, x, season_length, out=out)
