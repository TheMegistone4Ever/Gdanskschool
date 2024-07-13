from os import makedirs
from os.path import exists

from matplotlib.pyplot import figure, plot, xlabel, ylabel, title, legend, grid, savefig, show
from pandas import read_csv


def create_directory_if_not_exists(directory_path: str):
    """Create the directory if it does not exist."""
    if not exists(directory_path):
        makedirs(directory_path)
        print(f"Created directory at \"{directory_path}\"...")


def plot_ocv_vs_time(data, save_path: str):
    """Plot Open Circuit Voltage (OCV) vs. Time."""
    figure(figsize=(10, 6))
    plot(data["T(Seconds)"], data["E(Volts)"], label="OCV vs Time")
    xlabel("Time (Seconds)")
    ylabel("OCV (Volts)")
    title("OCV vs. Time for SOFC Mode")
    legend()
    grid(True)
    savefig(save_path, dpi=150)
    show()


def plot_i_v_curves(data_files, mode: str, save_path: str):
    """Plot Current Density vs. Voltage for given mode."""
    figure(figsize=(10, 6))
    for file in data_files:
        file_df = read_csv(file, sep=r"\s+")
        plot(abs(file_df["I(A/cm2)"]), file_df["E(Volts)"], label=f"{file.split('/')[-1].split('_')[3]} H2O")
    xlabel("Current Density (A/cm2)")
    ylabel("Voltage (V)")
    title(f"I-V Curves for {mode} Mode")
    legend(title="% H2O")
    grid(True)
    savefig(save_path, dpi=150)
    show()


def plot_p_i_curves(data_files, mode: str, save_path: str):
    """Plot Power Density vs. Current Density for given mode."""
    figure(figsize=(10, 6))
    for file in data_files:
        file_df = read_csv(file, sep=r"\s+")
        power = abs(file_df["E(Volts)"] * file_df["I(A/cm2)"])
        plot(abs(file_df["I(A/cm2)"]), power, label=f"{file.split('/')[-1].split('_')[3]} H2O")
    xlabel("Current Density (A/cm2)")
    ylabel("Power Density (W/cm2)")
    title(f"P-I Curves for {mode} Mode")
    legend(title="% H2O")
    grid(True)
    savefig(save_path, dpi=150)
    show()


def plot_nyquist_curves(data_files, mode: str, save_path: str):
    """Plot Nyquist curves for given mode."""
    figure(figsize=(10, 6))
    for file in data_files:
        data = read_csv(file, sep=r"\s+")
        imag = -data["Z''"][data["Z''"] <= 0]
        real = data["Z'"][data["Z''"] <= 0]
        plot(real, imag[imag > 0], label=f"{file.split('/')[-1].split('_')[2]} H2O")
    xlabel("Z' (Real Impedance, Ω)")
    ylabel("Z'' (Imaginary Impedance, Ω)")
    title(f"Nyquist Plot for {mode} Mode")
    legend(title="% H2O")
    grid(True)
    savefig(save_path, dpi=150)
    show()
