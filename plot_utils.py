from functools import wraps
from os import makedirs
from os.path import exists

from matplotlib.pyplot import figure, plot, xlabel, ylabel, title, legend, grid, savefig, show
from pandas import read_csv


def plot_decorator(xlabel_text, ylabel_text, legend_title=None, fig_size=(10, 6)):
    def decorator(plot_func):
        @wraps(plot_func)
        def wrapper(*args, **kwargs):
            figure(figsize=fig_size)
            plot_func(*args, **kwargs)
            xlabel(xlabel_text)
            ylabel(ylabel_text)
            legend(title=legend_title)
            grid(True)
            if "save_path" in kwargs:
                savefig(kwargs.get("save_path"), dpi=150)
            show()

        return wrapper

    return decorator


def create_directory_if_not_exists(directory_path: str):
    """Create the directory if it does not exist."""
    if not exists(directory_path):
        makedirs(directory_path)
        print(f"Created directory at \"{directory_path}\"...")


@plot_decorator("Time (Seconds)", "OCV (Volts)")
def plot_ocv_vs_time(data, save_path: str):
    """Plot Open Circuit Voltage (OCV) vs. Time."""
    print(f"Plotting OCV vs. Time for mode=SOFC, saving to {save_path}")
    title("OCV vs. Time for mode=SOFC")
    plot(data["T(Seconds)"], data["E(Volts)"], label="OCV vs Time")


@plot_decorator("Current Density (A/cm2)", "Voltage (V)", "% H2O")
def plot_i_v_curves(data_files, mode: str, save_path: str):
    """Plot Current Density vs. Voltage for given mode."""
    print(f"Plotting I-V Curves for {mode=}, saving to {save_path}")
    title(f"I-V Curves for {mode=}")
    for file in data_files:
        file_df = read_csv(file, sep=r"\s+")
        file_df["I(A/cm2)"] = file_df["I(A/cm2)"].abs()
        plot(file_df["I(A/cm2)"], file_df["E(Volts)"], label=f"{file.split('/')[-1].split('_')[3]} H2O")


@plot_decorator("Current Density (A/cm2)", "Power Density (W/cm2)", "% H2O")
def plot_p_i_curves(data_files, mode: str, save_path: str):
    """Plot Power Density vs. Current Density for given mode."""
    print(f"Plotting P-I Curves for {mode=}, saving to {save_path}")
    title(f"P-I Curves for {mode=}")
    for file in data_files:
        file_df = read_csv(file, sep=r"\s+")
        file_df["I(A/cm2)"] = file_df["I(A/cm2)"].abs()
        power = file_df["E(Volts)"] * file_df["I(A/cm2)"]
        plot(file_df["I(A/cm2)"], power, label=f"{file.split('/')[-1].split('_')[3]} H2O")


@plot_decorator("Z' (Real Impedance, Ω)", "Z'' (Imaginary Impedance, Ω)", "% H2O")
def plot_nyquist_curves(data_files, mode: str, save_path: str):
    """Plot Nyquist curves for given mode."""
    print(f"Plotting Nyquist Curves for {mode=}, saving to {save_path}")
    title(f"Nyquist Plot for {mode=}")
    for file in data_files:
        data = read_csv(file, sep=r"\s+")
        imag = -data["Z''"][data["Z''"] <= 0]
        real = data["Z'"][data["Z''"] <= 0]
        plot(real, imag, label=f"{file.split('/')[-1].split('_')[2]} H2O")
