# -*- coding: utf-8 -*-

__all__ = ["my_cool_function"]

import numpy as np


def my_cool_function(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """This is a clever function that adds two numpy arrays

    Args:
        a (np.ndarray): The first array
        b (np.ndarray): The second array (shocker!!)

    Returns:
        np.ndarray: The sum of `a` and `b`
    """
    return a + b
