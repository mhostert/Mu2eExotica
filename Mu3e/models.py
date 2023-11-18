import numpy as np
import DarkNews as dn
from particle import literals as lp

from .mudecays import Gamma_mu

MeV_to_GeV = 1e-3
cm_to_mm = 1e1


def f_PS(x):
    return (1 - 4 * x**2 + 12 * x**4) * np.sqrt(1 - 4 * x**2)


def g_PS(x):
    return (1 + 2 * x**2) * np.sqrt(1 - 4 * x**2)


class DS:
    def __init__(self, maprime, mphi, Femu=1.0, alphaD=0.1, epsilon=1e-4) -> None:
        self.maprime = maprime
        self.mphi = mphi

        self.alphaD = alphaD
        self.gD = np.sqrt(alphaD * 4 * np.pi)
        self.epsilon = epsilon
        self.Femu = Femu

        self.vevD = self.maprime / self.gD
        self.lambda_quartic = (self.mphi / self.vevD) ** 2 / 2

        if self.lambda_quartic > np.sqrt(4 * np.pi):
            print(
                "Oops! Violating perturbativity. Scalar quartic coupling, lambda = ",
                self.lambda_quartic,
            )

        self.GammaAprime = (
            dn.const.alphaQED
            * self.epsilon**2
            * self.maprime
            / 3
            * g_PS(lp.e_minus.mass / self.maprime)
        )
        self.GammaPhi = (
            self.alphaD
            * self.mphi**3
            / self.maprime**2
            / 8
            * g_PS(self.maprime / self.mphi)
        )

    def get_mu5e_BR(self):
        rl = lp.e_minus.mass / lp.mu_minus.mass
        rphi = self.mphi * 1e-3 / lp.mu_minus.mass

        return (
            self.Femu**2
            * lp.mu_minus.mass
            / 16
            / np.pi
            * dn.const.kallen_sqrt(1, rl**2, rphi**2)
            * ((1 + rl) ** 2 - rphi**2)
            / Gamma_mu
        )

    # mm
    def get_phi_ctau0(self):
        return dn.const.get_decay_rate_in_cm(self.GammaPhi * MeV_to_GeV) * cm_to_mm

    # s
    def get_phi_tau0(self):
        return dn.const.get_decay_rate_in_s(self.GammaPhi * MeV_to_GeV)

    # mm
    def get_aprime_ctau0(self):
        return dn.const.get_decay_rate_in_cm(self.GammaAprime * MeV_to_GeV) * cm_to_mm

    # s
    def get_aprime_tau0(self):
        return dn.const.get_decay_rate_in_s(self.GammaAprime * MeV_to_GeV)
