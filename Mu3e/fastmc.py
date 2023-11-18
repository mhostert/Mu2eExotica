import numpy as np
import os
from scipy.interpolate import interp1d
from particle import literals as lp
from DarkNews import Cfourvec as Cfv

this_dir = os.path.dirname(os.path.realpath(__file__))

import hepunits as u

c_light = u.c_light / u.mm * u.s

##########################
# Geometrical properties
target_R = 19  # mm
target_L = 100  # mm
TanTheta = target_R / (target_L / 2)

layer1_R = 23.3  # mm
layer2_R = 29.8  # mm
layer3_R = 73.9  # mm
layer4_R = 86.3  # mm

layer1_L = 124.7  # mm
layer2_L = 124.7  # mm
layer3_L = 351.9  # mm
layer4_L = 372.6  # mm

outer_recurler_gap = 20  # mm
recurler_L = 340  # mm


def r(x, y):
    return np.sqrt(x**2 + y**2)


def radius_of_curvature(p, Bfield=1.0):
    # radius in mm, Bfield in Tesla, and p in MeV
    return p / 0.3 / (Bfield)  # in mm


def time_of_recurl(R, beta_T):
    # in seconds
    return 2 * np.pi * R * 0.6 / (c_light * np.abs(beta_T))


def time_of_exit(z, beta_L):
    # in seconds
    L = layer4_L / 2 + recurler_L + outer_recurler_gap
    return np.where(beta_L * z >= 0, (L - np.abs(z)), (L + np.abs(z))) / (
        c_light * np.abs(beta_L)
    )


def z_of_recurl(R, beta_T):
    # in mm
    return 2 * np.pi * R * 0.6 / (c_light * np.abs(beta_T))


def Rcone(z):
    return TanTheta * (target_L / 2 - np.abs(z))


def gauss(x, sigma):
    return np.exp(-0.5 * x**2 / sigma**2)


# millimeter
def beam_transverse(x, y):
    return gauss(x, 7.50) * gauss(y, 8.74)


def get_decay_positions_in_target(nsamples: int):
    """get_decay_positions_in_target returns x,y,z positions muon decays inside double-cone target

    Parameters
    ----------
    nsamples : int
        number of events desired

    Returns
    -------
    np.array(nsamples,3), np.array(nsamples)
        events, normalized weights
    """
    nsamples = int(nsamples)
    target_samples = 0
    events = np.array(3 * [[]]).T
    while target_samples < nsamples:
        z = np.random.uniform(-target_L / 2, target_L / 2, nsamples)
        x = np.random.uniform(-target_R, target_R, nsamples)
        y = np.random.uniform(-target_R, target_R, nsamples)
        new_events = np.array([x, y, z]).T
        events = np.concatenate(
            (events, new_events[np.where(r(x, y) < Rcone(z))]), axis=0
        )
        target_samples = np.shape(events)[0]

    events = events[:nsamples]

    # weights
    zposfit = np.poly1d(np.load(f"{this_dir}/exp_params/zpos_fit_pdf.npy"))

    weights = zposfit(events[:, -1])
    weights *= beam_transverse(events[:, 0], events[:, 1])

    return events, weights / np.sum(weights)


p, dp = np.genfromtxt(f"{this_dir}/exp_params/p_resolution_long_8hits.dat", unpack=True)
res_long_8 = interp1d(
    p, dp, kind="linear", fill_value=(dp[0], dp[-1]), bounds_error=False
)
p, dp = np.genfromtxt(f"{this_dir}/exp_params/p_resolution_long_6hits.dat", unpack=True)
res_long_6 = interp1d(
    p, dp, kind="linear", fill_value=(dp[0], dp[-1]), bounds_error=False
)

p, dp = np.genfromtxt(f"{this_dir}/exp_params/p_resolution_short.dat", unpack=True)
res_short = interp1d(
    p, dp, kind="linear", fill_value=(dp[0], dp[-1]), bounds_error=False
)


def smear_samples(particles, nhits):
    mass = lp.e_minus.mass
    for name, samples in particles.items():
        if "e+" in name or "e-" in name:
            p = np.sqrt(samples[:, 0] ** 2 - mass**2)

            res = np.zeros(len(p))
            res[(nhits[name] >= 8)] = res_long_8(p[(nhits[name] >= 8)])
            res[(nhits[name] == 6)] = res_long_6(p[(nhits[name] == 6)])
            res[(nhits[name] <= 4)] = res_short(p[(nhits[name] <= 4)])

            sigma_p = res

            # compute kinetic energy and spherical angles
            p_r = Cfv.random_normal(p, sigma_p)

            # Unfortunately, a Gaussian energy smearing can give non-physical results.
            p_r[p_r < 0] = 0  # force smearing to be positive for p

            # put data in an array and then in a DataFrame
            samples[:, 0] = np.sqrt(p_r**2 + mass**2)
            samples[:, 1] *= p_r / p
            samples[:, 2] *= p_r / p
            samples[:, 3] *= p_r / p
            particles[name] = samples

    return particles
