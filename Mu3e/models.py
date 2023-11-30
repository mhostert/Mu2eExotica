import numpy as np
from particle import literals as lp

from .mudecays import Gamma_mu
from . import const
from .plot_tools import sci_notation


# Phase space factors
def f_PS(x):
    return (1 - 4 * x**2 + 12 * x**4) * np.sqrt(1 - 4 * x**2)


def g_PS(x):
    return (1 + 2 * x**2) * np.sqrt(1 - 4 * x**2)


def F2_to_F1_V_2body(r1, rV):
    return (r1**4 + (rV**2 - 2) * r1**2 - 2 * rV**4 + rV**2 + 1) * np.sqrt(
        r1**4 - 2 * (rV**2 + 1) * r1**2 + (rV**2 - 1) ** 2
    )


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
                "Oops! Violating perturbativity. Scalar quartic, lambda = ",
                self.lambda_quartic,
            )

        self.GammaAprime = (
            const.alphaQED
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
            * const.kallen_sqrt(1, rl**2, rphi**2)
            * ((1 + rl) ** 2 - rphi**2)
            / Gamma_mu
        )

    # mm
    def get_phi_ctau0(self):
        return (
            const.get_decay_rate_in_cm(self.GammaPhi * const.MeV_to_GeV)
            * const.cm_to_mm
        )

    # s
    def get_phi_tau0(self):
        return const.get_decay_rate_in_s(self.GammaPhi * const.MeV_to_GeV)

    # mm
    def get_aprime_ctau0(self):
        return (
            const.get_decay_rate_in_cm(self.GammaAprime * const.MeV_to_GeV)
            * const.cm_to_mm
        )

    # s
    def get_aprime_tau0(self):
        return const.get_decay_rate_in_s(self.GammaAprime * const.MeV_to_GeV)


class MuonCaptureModelI:
    def __init__(self, maprime, m2, m1, Gmup, alphaD=0.1, epsilon=1e-4) -> None:
        self.maprime = maprime
        self.m2 = m2
        self.m1 = m1
        self.Gmup = Gmup
        self.Lambda_NP = 1 / np.sqrt(self.Gmup)

        self.alphaD = alphaD
        self.gD = np.sqrt(alphaD * 4 * np.pi)
        self.epsilon = epsilon

        self.pdecay_rescale = self.gD**2 * self.Gmup**2

        self.chi2_decays = self.m2 > self.m1 + self.maprime
        self.maprime_decays = self.maprime > const.m_e * 2
        self.muon_capture_open = self.m2 < const.m_proton + const.m_mu

        if not self.chi2_decays:
            print("Warning: chi2 > chi1 A' forbidden")
        if not self.maprime_decays:
            print("Warning: A' > e+ e- forbidden")
        if not self.muon_capture_open:
            print("Warning: Muon capture forbidden.")

        self.tex_scale = sci_notation(
            self.Lambda_NP * 1e-3, notex=True, decimal_digits=0
        )
        self.text_descriptor = rf"\noindent$\alpha_D = {self.alphaD:.1f}$\\$G_{{\mu p}} = ({self.tex_scale}$ \,TeV$)^{{-2}}$\\$m_2 = {self.m2*1e3:.0f}$ MeV\\$m_1 = {self.m1*1e3:.0f}$ MeV\\$m_{{A^\prime}} = {self.maprime*1e3:.0f}$ MeV"

        self.GammaAprime = (
            const.alphaQED
            * self.epsilon**2
            * self.maprime
            / 3
            * g_PS(const.m_e / self.maprime)
        )
        self.Gammachi2 = (
            self.alphaD
            * self.m2**3
            / self.maprime**2
            / 8
            * F2_to_F1_V_2body(self.m1 / self.m2, self.maprime / self.m2)
        )

    def get_open_pdecay_channels(self):
        channels = []
        if self.m2 < const.m_proton - const.m_mu:
            channels.append(f"p > mu chi2 v")
        if self.m1 + self.maprime < const.m_proton - const.m_mu:
            channels.append(f"p > mu (chi2 > chi1 Ap) v")
        if self.m1 < const.m_proton - const.m_mu - 2 * const.m_e:
            channels.append(f"p > mu (chi2 > chi1 (Ap > ee)) v")
        if self.m2 < const.m_proton - const.m_mu - 2 * const.m_e:
            channels.append(f"p > (mu> e v v) chi2 v")
        if self.m2 < const.m_proton - const.m_e:
            channels.append(f"p > (mu> e v v) chi2 v")
        if const.m_proton > self.m1 + self.maprime + const.m_e:
            channels.append(f"p > (mu> e v v) (chi2 > chi1 (Ap > ee)) v")

        if const.m_proton + const.m_mu < self.m2:
            print("Warning: Muon capture not possible.")

        return channels

    def get_mu_capture_rate(self, Z=13, Gamma_cap=4.6e-19):
        return (
            self.Gmup**2
            * const.m_mu**5
            / 4
            / np.pi
            * Z**2
            / Gamma_cap
            * np.sqrt(1 - self.m2**2 / (const.m_mu + const.m_proton) ** 2)
        )

    # mm
    def get_chi2_ctau0(self):
        return (
            const.get_decay_rate_in_cm(self.Gammachi2 * const.MeV_to_GeV)
            * const.cm_to_mm
        )

    # s
    def get_chi2_tau0(self):
        return const.get_decay_rate_in_s(self.Gammachi2 * const.MeV_to_GeV)

    # mm
    def get_aprime_ctau0(self):
        return (
            const.get_decay_rate_in_cm(self.GammaAprime * const.MeV_to_GeV)
            * const.cm_to_mm
        )

    # s
    def get_aprime_tau0(self):
        return const.get_decay_rate_in_s(self.GammaAprime * const.MeV_to_GeV)
