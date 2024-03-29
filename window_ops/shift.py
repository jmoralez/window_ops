# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/shift.ipynb.

# %% auto 0
__all__ = ['shift_array']

# %% ../nbs/shift.ipynb 2
import numpy as np
from numba import njit  # type: ignore

# %% ../nbs/shift.ipynb 3
@njit
def shift_array(input_array: np.ndarray, offset: int) -> np.ndarray:
    n_samples = input_array.size
    output_array = np.full_like(input_array, np.nan)
    for i in range(n_samples - offset):
        output_array[i + offset] = input_array[i]
    return output_array
