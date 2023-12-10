import os
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import rc, rcParams

###########################
fsize = 12
fsize_annotate = 10

std_figsize = (1.2 * 3.7, 1.6 * 2.3617)
std_axes_form = [0.16, 0.15, 0.81, 0.76]

electron_color = (0.85, 0.39, 0.14)
positron_color = (0.16, 0.37, 0.65)
ax_colors = "#CFCFCF"
text_color = "grey"

particle_name = {"e+": r"e^+", "e-": r"e^-", "nu": r"\nu"}


# standard figure
def std_fig(ax_form=std_axes_form, figsize=std_figsize, rasterized=False):
    rcparams = {
        "axes.labelsize": fsize,
        "xtick.labelsize": fsize,
        "ytick.labelsize": fsize,
        "figure.figsize": std_figsize,
        "legend.frameon": False,
        "legend.loc": "best",
    }
    plt.rcParams["text.latex.preamble"] = r"\usepackage{amsmath}\usepackage{amssymb}"
    rc("font", **{"family": "serif", "serif": ["Computer Modern"]})
    rc("text", usetex=True)
    rcParams.update(rcparams)
    mpl.rcParams["hatch.linewidth"] = 0.25
    fig = plt.figure(figsize=figsize)
    ax = fig.add_axes(ax_form, rasterized=rasterized)
    ax.patch.set_alpha(0.0)

    return fig, ax


# standard saving function
def std_savefig(fig, path, dpi=400, **kwargs):
    dir_tree = os.path.dirname(path)
    os.makedirs(dir_tree, exist_ok=True)
    fig.savefig(path, dpi=dpi, **kwargs)


def sci_notation(num, decimal_digits=1, precision=None, exponent=None, notex=False):
    """
    Returns a string representation of the scientific
    notation of the given number formatted for use with
    LaTeX or Mathtext, with specified number of significant
    decimal digits and precision (number of decimal digits
    to show). The exponent to be used can also be specified
    explicitly.
    """
    if num != 0:
        if exponent is None:
            exponent = int(np.floor(np.log10(abs(num))))
        coeff = round(num / float(10**exponent), decimal_digits)
        if coeff == 10:
            coeff = 1
            exponent += 1
        if precision is None:
            precision = decimal_digits
        if notex:
            return r"{0:.{2}f}\times 10^{{{1:d}}}".format(coeff, exponent, precision)
        else:
            return r"${0:.{2}f}\times 10^{{{1:d}}}$".format(coeff, exponent, precision)
    else:
        return r"0"
