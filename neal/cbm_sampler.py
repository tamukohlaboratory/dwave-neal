import math
from neal.sampler import SimulatedAnnealingSampler

from numbers import Integral
from random import randint
from collections import defaultdict

import dimod
import numpy as np

__all__ = ["ChaoticBoltzmannMachineSampler"]


def null_annealer(num_samples, h, coupler_starts, coupler_ends,
                  coupler_weights, sweeps_per_beta, beta_schedule, seed,
                  states_numpy,
                  interrupt_function=None):
    print('null annealer')

    return 0, 1


class ChaoticBoltzmannMachineSampler(SimulatedAnnealingSampler):
    def __init__(self):
        super().__init__()
        self.annealer = null_annealer
