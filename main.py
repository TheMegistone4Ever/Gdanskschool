from os import makedirs
from os.path import exists, join

from matplotlib.pyplot import figure, plot, xlabel, ylabel, title, legend, grid, savefig, show
from pandas import read_csv, concat

if not exists(r".\plots"):
    makedirs(r".\plots")

data_path = r".\mnt\data"

# Load the OCV data files
ocv1_data = read_csv(join(data_path, "ocv1_reductionH2_H2O_4.txt"), sep=r"\s+")
ocv2_data = read_csv(join(data_path, "ocv2_H2O_4_to_12.txt"), sep=r"\s+")

# Combine the OCV data into a single DataFrame
ocv_data = concat([ocv1_data, ocv2_data], ignore_index=True)

# Plot OCV vs. Time
figure(figsize=(10, 6))
plot(ocv_data["T(Seconds)"], ocv_data["E(Volts)"], label="OCV vs Time")
xlabel("Time (Seconds)")
ylabel("OCV (Volts)")
title("OCV vs. Time for SOFC Mode")
legend()
grid(True)
savefig(r".\plots\ocv_vs_time.png", dpi=150)
show()


def plot_i_v_curves(data_files, i_v_mode):
    figure(figsize=(10, 6))
    for f in data_files:
        file_df = read_csv(f, sep=r"\s+")
        plot(abs(file_df["I(A/cm2)"]), file_df["E(Volts)"], label=f"{f.split('/')[-1].split('_')[3]} H2O")
    xlabel("Current Density (A/cm2)")
    ylabel("Voltage (V)")
    title(f"I-V Curves for {i_v_mode} Mode")
    legend(title="% H2O")
    grid(True)
    savefig(rf".\plots\iv_curves_{i_v_mode.lower()}_mode.png", dpi=150)
    show()


def plot_p_i_curves(data_files, p_i_mode):
    figure(figsize=(10, 6))
    for f in data_files:
        file_df = read_csv(f, sep=r"\s+")
        power = abs(file_df["E(Volts)"] * file_df["I(A/cm2)"])
        plot(abs(file_df["I(A/cm2)"]), power, label=f"{f.split('/')[-1].split('_')[3]} H2O")
    xlabel("Current Density (A/cm2)")
    ylabel("Power Density (W/cm2)")
    title(f"P-I Curves for {p_i_mode} Mode")
    legend(title="% H2O")
    grid(True)
    savefig(rf".\plots\pi_curves_{p_i_mode.lower()}_mode.png", dpi=150)
    show()


def plot_nyquist_plots(data_files, nyquist_mode):
    figure(figsize=(10, 6))
    for file in data_files:
        data = read_csv(file, sep=r"\s+")
        imag = -data["Z''"][data["Z''"] <= 0]
        real = data["Z'"][data["Z''"] <= 0]
        plot(real, imag[imag > 0], label=f"{file.split('/')[-1].split('_')[2]} H2O")
    xlabel("Z' (Real Impedance, Ω)")
    ylabel("Z'' (Imaginary Impedance, Ω)")
    title(f"Nyquist Plot for {nyquist_mode} Mode")
    legend(title="% H2O")
    grid(True)
    savefig(rf".\plots\nyquist_plot_{nyquist_mode.lower()}_mode.png", dpi=150)
    show()


# Define impedance spectroscopy data files for both SOFC and SOEC modes
impedance_files = {
    "SOFC": [
        join(data_path, "800_SOFC_test_4_H2O.txt"),
        join(data_path, "800_SOFC_test_12_H2O.txt"),
        join(data_path, "800_SOFC_test_25_H2O.txt"),
        join(data_path, "800_SOFC_test_50_H2O.txt"),
    ],
    "SOEC": [
        join(data_path, "800_SOEC_test_4_H2O.txt"),
        join(data_path, "800_SOEC_test_12_H2O.txt"),
        join(data_path, "800_SOEC_test_25_H2O.txt"),
        join(data_path, "800_SOEC_test_50_H2O.txt"),
    ],
}

# Define Nyquist data files for both SOFC and SOEC modes
nyquist_files = {
    "SOFC": [
        join(data_path, "IS_800_SOFC_4_H2O.txt"),
        join(data_path, "IS_800_SOFC_12_H2O.txt"),
        join(data_path, "IS_800_SOFC_25_H2O.txt"),
        join(data_path, "IS_800_SOFC_50_H2O.txt"),
    ],
    "SOEC": [
        join(data_path, "IS_800_SOEC_4_H2O.txt"),
        join(data_path, "IS_800_SOEC_12_H2O.txt"),
        join(data_path, "IS_800_SOEC_25_H2O.txt"),
        join(data_path, "IS_800_SOEC_50_H2O.txt"),
    ],
}

# Plot I-V plots for both SOFC and SOEC modes
for mode, files in impedance_files.items():
    plot_i_v_curves(files, mode)

# Plot P-I plot for both SOFC and SOEC modes
for mode, files in impedance_files.items():
    plot_p_i_curves(files, mode)

# Plot Nyquist plots for both SOFC and SOEC modes
for mode, files in nyquist_files.items():
    plot_nyquist_plots(files, mode)

# Load one impedance spectroscopy data file to check the column names
data_example = read_csv(join(data_path, "IS_800_SOFC_4_H2O.txt"), sep=r"\s+")
print(data_example.columns)
