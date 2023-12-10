import numpy as np
import pylhe

import os

this_dir = os.path.dirname(os.path.realpath(__file__))


def mu_PS(x):
    return 1 - 8 * x - 12 * x**2 * np.log(x) + 8 * x**3 - x**4


def get_P_and_id_from_MG5(filename):
    # self.mg5events = pylhe.read_lhe_with_attributes(self.import_from_mg5)
    mg5events = pylhe.read_lhe(filename)

    # Create akward array objects for convinience
    mg5events = pylhe.to_awkward(mg5events)

    P_grid = np.array(
        [
            np.array(mg5events["particles", "vector", ind])
            for ind in ["t", "x", "y", "z"]
        ]
    )
    P_grid = np.transpose(P_grid, axes=(1, 0, 2)) * 1e3  # convert from GeV to MeV

    return P_grid, mg5events["particles", "id"][0]
