from os import path, makedirs

import matplotlib.pyplot as plt
import pandas as pd

if not path.exists(r".\plots"):
    makedirs(r".\plots")

# Load the OCV data files
ocv1_data = pd.read_csv(r".\mnt\data\ocv1_reductionH2_H2O_4.txt", sep=r"\s+")
ocv2_data = pd.read_csv(r".\mnt\data\ocv2_H2O_4_to_12.txt", sep=r"\s+")

# Combine the OCV data into a single DataFrame
ocv_data = pd.concat([ocv1_data, ocv2_data], ignore_index=True)

# Plot OCV vs. Time
plt.figure(figsize=(10, 6))
plt.plot(ocv_data["T(Seconds)"], ocv_data["E(Volts)"], label="OCV vs Time")
plt.xlabel("Time (Seconds)")
plt.ylabel("OCV (Volts)")
plt.title("OCV vs. Time for SOFC Mode")
plt.legend()
plt.grid(True)
plt.savefig(r".\plots\ocv_vs_time.png", dpi=150)
plt.show()


def plot_i_v_curves(data_files, i_v_mode):
    plt.figure(figsize=(10, 6))
    for f in data_files:
        file_df = pd.read_csv(f, sep=r"\s+")
        plt.plot(file_df["I(A/cm2)"], file_df["E(Volts)"], label=f"{f.split('/')[-1].split('_')[3]} H2O")
    plt.xlabel("Current Density (A/cm2)")
    plt.ylabel("Voltage (V)")
    plt.title(f"I-V Curves for {i_v_mode} Mode")
    plt.legend(title="% H2O")
    plt.grid(True)
    plt.savefig(rf".\plots\iv_curves_{i_v_mode.lower()}_mode.png", dpi=150)
    plt.show()


def plot_p_i_curves(data_files, p_i_mode):
    plt.figure(figsize=(10, 6))
    for f in data_files:
        file_df = pd.read_csv(f, sep=r"\s+")
        power = file_df["E(Volts)"] * file_df["I(A/cm2)"]
        plt.plot(file_df["I(A/cm2)"], power, label=f"{f.split('/')[-1].split('_')[3]} H2O")
    plt.xlabel("Current Density (A/cm2)")
    plt.ylabel("Power Density (W/cm2)")
    plt.title(f"P-I Curves for {p_i_mode} Mode")
    plt.legend(title="% H2O")
    plt.grid(True)
    plt.savefig(rf".\plots\pi_curves_{p_i_mode.lower()}_mode.png", dpi=150)
    plt.show()


def plot_nyquist_plots(data_files, nyquist_mode):
    plt.figure(figsize=(10, 6))
    for file in data_files:
        data = pd.read_csv(file, sep=r"\s+")
        plt.plot(data["Z'"], data["Z''"], label=f"{file.split('/')[-1].split('_')[2]} H2O")
    plt.xlabel("Z' (Real Impedance, Ω)")
    plt.ylabel("Z'' (Imaginary Impedance, Ω)")
    plt.title(f"Nyquist Plot for {nyquist_mode} Mode")
    plt.legend(title="% H2O")
    plt.grid(True)
    plt.savefig(rf".\plots\nyquist_plot_{nyquist_mode.lower()}_mode.png", dpi=150)
    plt.show()


# Define impedance spectroscopy data files for both SOFC and SOEC modes
impedance_files = {
    "SOFC": [
        r".\mnt\data\800_SOFC_test_4_H2O.txt",
        r".\mnt\data\800_SOFC_test_12_H2O.txt",
        r".\mnt\data\800_SOFC_test_25_H2O.txt",
        r".\mnt\data\800_SOFC_test_50_H2O.txt",
    ],
    "SOEC": [
        r".\mnt\data\800_SOEC_test_4_H2O.txt",
        r".\mnt\data\800_SOEC_test_12_H2O.txt",
        r".\mnt\data\800_SOEC_test_25_H2O.txt",
        r".\mnt\data\800_SOEC_test_50_H2O.txt",
    ],
}

# Define Nyquist data files for both SOFC and SOEC modes
nyquist_files = {
    "SOFC": [
        r".\mnt\data\IS_800_SOFC_4_H2O.txt",
        r".\mnt\data\IS_800_SOFC_12_H2O.txt",
        r".\mnt\data\IS_800_SOFC_25_H2O.txt",
        r".\mnt\data\IS_800_SOFC_50_H2O.txt",
    ],
    "SOEC": [
        r".\mnt\data\IS_800_SOEC_4_H2O.txt",
        r".\mnt\data\IS_800_SOEC_12_H2O.txt",
        r".\mnt\data\IS_800_SOEC_25_H2O.txt",
        r".\mnt\data\IS_800_SOEC_50_H2O.txt",
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
data_example = pd.read_csv(r".\mnt\data\IS_800_SOFC_4_H2O.txt", sep=r"\s+")
print(data_example.columns)
