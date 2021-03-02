from typing import Callable, List, Type, Union

import numpy as np
import tensorflow as tf
import tensorflow.keras as keras

from tensorflow.keras.callbacks import Callback as TF_Callback
from tensorflow.keras.losses import Loss as TF_Loss
from tensorflow.keras.metrics import Metric as TF_Metric
from tensorflow.keras.optimizers import Optimizer as TF_Optimizer


Model = Union[Callable[..., keras.Model], keras.Model]
RandomState = Union[int, np.random.RandomState]
Optimizer = Union[str, TF_Optimizer, Type[TF_Optimizer]]
Loss = Union[str, TF_Loss, Type[TF_Loss], Callable]
Metrics = Union[List[Union[str, TF_Metric, Type[TF_Metric], Callable]]]
Callbacks = Union[List[Union[TF_Callback, Type[TF_Callback]]]]