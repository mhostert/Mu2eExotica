import os
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import rc, rcParams
from matplotlib import animation
from matplotlib.pyplot import cm

from . import fastmc as fm

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
        if precision is None:
            precision = decimal_digits
        if notex:
            return r"{0:.{2}f}\times 10^{{{1:d}}}".format(coeff, exponent, precision)
        else:
            return r"${0:.{2}f}\times 10^{{{1:d}}}$".format(coeff, exponent, precision)
    else:
        return r"0"


def EventDraw(
    decay,
    event,
    path=None,
    draw_momentum=False,
    density=True,
    animate=False,
    frames=100,
    **kwargs,
):
    scale_factor = 4.5 / 4
    fig, ax = std_fig(figsize=(std_figsize[0] * scale_factor, std_figsize[1]))
    ax.add_patch(
        patches.Circle(
            (0, 0), fm.target_R, fill=False, color="silver", lw=0.5, zorder=1
        )
    )

    det_kwargs = {"lw": 0.75, "color": "grey", "fill": False, "zorder": 1}
    layers_R = [fm.layer1_R, fm.layer2_R, fm.layer3_R, fm.layer4_R]
    layers_vert = [8, 10, 24, 28]

    for R, vert in zip(layers_R, layers_vert):
        draw_layer(ax, R, vert, **det_kwargs)

    if density:
        draw_decay_density(fig, ax, density)

    ax.plot([], [], label=r"$e^-$", color=electron_color, lw=1, ls="-")
    ax.plot([], [], label=r"$e^+$", color=positron_color, lw=1, ls="-")
    ax.legend(
        frameon=False, fontsize=10, loc=(0.9, 0.85), handlelength=1.2, handletextpad=0.5
    )
    XY_geometry(ax)

    def new_event(time):
        # remove previous event
        for child in ax.get_children():
            if (
                isinstance(child, mpl.text.Annotation)
                or isinstance(child, mpl.lines.Line2D)
                or isinstance(child, mpl.patches.Arc)
            ):
                child.remove()

        i = 0
        for name, p in decay.particles_true.items():
            p = p[event]
            position = decay.pos[event]
            if "e+" in name:
                color = positron_color
                draw_track(
                    ax,
                    p,
                    position,
                    name,
                    TIME=time / frames,
                    draw_momentum=draw_momentum,
                )
                i += 1
            elif "e-" in name:
                color = electron_color
                draw_track(
                    ax,
                    p,
                    position,
                    name,
                    TIME=time / frames,
                    draw_momentum=draw_momentum,
                )
                i += 1
            elif "nu_" in name:
                color = "black"
                draw_momentum_track(ax, p)
                i += 1
            else:
                continue

            sub = rf"$p_{{{particle_name[name[:2]]}}}"
            if get_pmag(p) < 1:
                label = rf"{sub} <1$ MeV\\"
            else:
                label = rf"{sub} = {get_pmag(p):.0f}$ MeV"

            ax.annotate(
                label,
                xy=(90, -105 + i * 9.5),
                fontsize=7,
                color=color,
                xycoords="data",
                ha="left",
                va="bottom",
                zorder=4,
                alpha=0.75,
            )

        ax.set_aspect("equal", adjustable="box")

    new_event(frames)

    if path is None:
        path = f"plots/event_{decay.channel}_{event}.png"

    fig.savefig(path, dpi=400, bbox_inches="tight")

    if animate:
        anim = animation.FuncAnimation(fig, new_event, frames=frames, repeat=False)
        return anim


def XY_geometry(ax):
    ax.spines[["left", "bottom"]].set_position("center")
    ax.spines[["left", "bottom"]].set_edgecolor(ax_colors)
    ax.spines[["left", "bottom"]].set_zorder(-1)
    ax.spines[["top", "right"]].set_visible(False)
    R = 105
    ax.set_ylim(-R, R)
    ax.set_xlim(-R, R)
    ax.set_xticks([-100, -75, -50, -25, 25, 50, 75, 100])
    ax.set_yticks([-100, -75, -50, -25, 25, 50, 75, 100])
    ax.set_xticklabels(
        [-100, "", -50, "", "", 50, "", 100], fontsize=10, color=ax_colors, zorder=-1
    )
    ax.set_yticklabels(
        [-100, "", -50, "", "", 50, "", 100], fontsize=10, color=ax_colors, zorder=-1
    )
    ax.tick_params(axis="x", colors=ax_colors, direction="inout", length=3, zorder=-1)
    ax.tick_params(axis="y", colors=ax_colors, direction="inout", length=3, zorder=-1)

    ax.scatter(
        0,
        ax.get_ylim()[1],
        marker=10,
        color=ax_colors,
        linewidth=0.0,
        clip_on=False,
        zorder=-1,
    )
    ax.scatter(
        ax.get_xlim()[1],
        0,
        marker=9,
        color=ax_colors,
        linewidth=0.0,
        clip_on=False,
        zorder=-1,
    )

    ax.text(
        1.02,
        0.53,
        r"x/mm",
        fontsize=10,
        color=ax_colors,
        transform=ax.transAxes,
        ha="left",
        va="bottom",
        zorder=-1,
    )
    ax.text(
        0.53,
        1.02,
        r"y/mm",
        fontsize=10,
        color=ax_colors,
        transform=ax.transAxes,
        ha="left",
        va="bottom",
        zorder=-1,
    )


def draw_decay_density(fig, ax, decay, **kwargs):
    h = ax.hist2d(
        decay.x,
        decay.y,
        weights=decay.weights / decay.weights.max(),
        bins=(40, 40),
        cmap="Blues",
        cmin=0,
        # cmax=1,
        density=False,
        zorder=0,
        **kwargs,
    )

    cb = fig.colorbar(h[3], fraction=0.025, pad=0.025, location="bottom", aspect=20)

    cb.ax.set_ylabel(
        r"$\mu$ decays", fontsize=8, rotation=0, labelpad=30, color=text_color
    )
    cb.ax.yaxis.set_label_position("right")
    cb.ax.zorder = -1
    cb.ax.tick_params(axis="y", colors=text_color, labelsize=8)
    cb.ax.tick_params(axis="x", colors=text_color, labelsize=8)


def draw_momentum_track(ax, p):
    phi = np.arctan2(p[2], p[1])
    # draw initial direction
    ax.plot(
        [0, 100 * np.cos(phi)], [0, 100 * np.sin(phi)], color="black", lw=0.3, ls="--"
    )


def draw_track(
    ax,
    p,
    position,
    name,
    TIME=1.0,
    pos=np.array([0, 0, 0]),
    draw_momentum=True,
    **kwargs,
):
    # vel in z direction
    beta_L = p[-1] / p[0]

    # transverse p and velocity
    pT = np.sqrt(p[1] ** 2 + p[2] ** 2)
    beta_T = pT / p[0]
    # theta = np.arccos(p[-1]/get_pmag(p))
    phi = np.arctan2(p[2], p[1])

    arc_R = fm.radius_of_curvature(pT, Bfield=1.0)
    t_exit = fm.time_of_exit(position[-1], beta_L)
    max_arc_angle = (
        t_exit * np.abs(beta_T) * fm.c_light / (2 * np.pi * arc_R) * 2 * np.pi
        if arc_R > 0
        else 0
    )  # degrees

    t_recurl = fm.time_of_recurl(arc_R, beta_T)
    z_recurl = t_recurl * beta_L * fm.c_light

    hit_recurler = (np.abs(z_recurl) > fm.recurler_L / 2 + fm.outer_recurler_gap) & (
        np.abs(z_recurl) < fm.recurler_L / 2 + fm.recurler_L + fm.outer_recurler_gap
    )
    long_track = (np.abs(z_recurl) < fm.recurler_L / 2) | hit_recurler
    short_track = 2 * arc_R > fm.layer4_R

    # did it pass selection criteria?
    signal_event = short_track  # & long_track

    # if full loop, then just draw circle
    if max_arc_angle > 2 * np.pi:
        max_arc_angle = 2 * np.pi

    arc_kwargs = {
        "width": np.abs(arc_R) * 2,
        "height": np.abs(arc_R) * 2,
        "lw": (1 if signal_event else 0.5),
        "ls": ((0, (1, 0)) if signal_event else (0, (3, 1))),
        "fill": False,
        "zorder": 2,
        "alpha": (1 if signal_event else 0.75),
    }
    if "e+" in name:
        arc_kwargs["color"] = positron_color
        arc_kwargs["xy"] = (
            arc_R * np.cos(np.pi / 2 + phi),
            arc_R * np.sin(np.pi / 2 + phi),
        )
        arc_kwargs["theta2"] = (np.pi + (np.pi / 2 + phi)) + max_arc_angle * TIME
        arc_kwargs["theta1"] = np.pi + (np.pi / 2 + phi)
    elif "e-" in name:
        arc_kwargs["color"] = electron_color
        arc_kwargs["xy"] = (
            arc_R * np.cos(phi - np.pi / 2),
            arc_R * np.sin(phi - np.pi / 2),
        )
        arc_kwargs["theta2"] = np.pi + (phi - np.pi / 2)
        arc_kwargs["theta1"] = (np.pi + (phi - np.pi / 2)) - max_arc_angle * TIME
    else:
        raise ValueError(f"Could not draw tracks for: {name}.")

    arc_kwargs.update(kwargs)
    arc_kwargs["xy"] = (arc_kwargs["xy"][0] + pos[0], arc_kwargs["xy"][1] + pos[1])
    arc_kwargs["theta1"] = 180 / np.pi * arc_kwargs["theta1"]
    arc_kwargs["theta2"] = 180 / np.pi * arc_kwargs["theta2"]

    if np.abs(arc_kwargs["theta2"] - arc_kwargs["theta1"]) >= 360:
        arc_kwargs["theta1"] = 0
        arc_kwargs["theta2"] = 360

    # draw track
    track = patches.Arc(clip_on=True, **arc_kwargs)
    # track.set_clip_box(ax.bbox)
    ax.add_patch(track)

    # if signal_event:
    # print(f"Track: {name} passed selection criteria.")

    if draw_momentum:
        # draw initial direction
        draw_momentum_track(ax, p)


def get_radius_from_apothem(a, vertices):
    return a / np.cos(np.pi / vertices)


def get_pmag(p):
    return np.sqrt(p[3] ** 2 + p[1] ** 2 + p[2] ** 2)


def draw_layer(ax, apothem, vertices, pos=np.array([0, 0]), **kwargs):
    ax.add_patch(
        patches.RegularPolygon(
            pos, vertices, radius=get_radius_from_apothem(apothem, vertices), **kwargs
        )
    )
    kwargs.update({"lw": 0.25})
    ax.add_patch(
        patches.RegularPolygon(
            pos,
            vertices,
            radius=get_radius_from_apothem(apothem, vertices) + 1.5,
            **kwargs,
        )
    )
