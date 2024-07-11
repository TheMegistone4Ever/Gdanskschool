from os import path, makedirs

import matplotlib.pyplot as plt
import pandas as pd

if not path.exists(r".\plots"):
    makedirs(r".\plots")

# Load the OCV data files
ocv1_data = pd.read_csv(r".\mnt\data\ocv1_reductionH2_H2O_4.txt", sep="\s+")
ocv2_data = pd.read_csv(r".\mnt\data\ocv2_H2O_4_to_12.txt", sep="\s+")

# Combine the data into a single DataFrame
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

# Load SOFC mode data files
sofc_files = [
    r".\mnt\data\800_SOFC_test_4_H2O.txt",
    r".\mnt\data\800_SOFC_test_12_H2O.txt",
    r".\mnt\data\800_SOFC_test_25_H2O.txt",
    r".\mnt\data\800_SOFC_test_50_H2O.txt"
]

# Read and plot I-V curves for SOFC mode
plt.figure(figsize=(10, 6))

for file in sofc_files:
    data = pd.read_csv(file, sep="\s+")
    plt.plot(data["I(A/cm2)"], data["E(Volts)"], label=f"{file.split('/')[-1].split('_')[3]} H2O")

plt.xlabel("Current Density (A/cm2)")
plt.ylabel("Voltage (V)")
plt.title("I-V Curves for SOFC Mode")
plt.legend(title="% H2O")
plt.grid(True)
plt.savefig(r".\plots\iv_curves_sofc_mode.png", dpi=150)
plt.show()

# Load SOEC mode data files
soec_files = [
    r".\mnt\data\800_SOEC_test_4_H2O.txt",
    r".\mnt\data\800_SOEC_test_12_H2O.txt",
    r".\mnt\data\800_SOEC_test_25_H2O.txt",
    r".\mnt\data\800_SOEC_test_50_H2O.txt"
]

# Read and plot I-V curves for SOEC mode
plt.figure(figsize=(10, 6))

for file in soec_files:
    data = pd.read_csv(file, sep="\s+")
    plt.plot(data["I(A/cm2)"], data["E(Volts)"], label=f"{file.split('/')[-1].split('_')[3]} H2O")

plt.xlabel("Current Density (A/cm2)")
plt.ylabel("Voltage (V)")
plt.title("I-V Curves for SOEC Mode")
plt.legend(title="% H2O")
plt.grid(True)
plt.savefig(r".\plots\iv_curves_soec_mode.png", dpi=150)
plt.show()

# Read and plot P-I curves for SOFC mode
plt.figure(figsize=(10, 6))

for file in sofc_files:
    data = pd.read_csv(file, sep="\s+")
    power = data["E(Volts)"] * data["I(A/cm2)"]
    plt.plot(data["I(A/cm2)"], power, label=f"{file.split('/')[-1].split('_')[3]} H2O")

plt.xlabel("Current Density (A/cm2)")
plt.ylabel("Power Density (W/cm2)")
plt.title("P-I Curves for SOFC Mode")
plt.legend(title="% H2O")
plt.grid(True)
plt.savefig(r".\plots\pi_curves_sofc_mode.png", dpi=150)
plt.show()

# Load impedance spectroscopy data files for both SOFC and SOEC
impedance_files = {
    "SOFC": [
        r".\mnt\data\IS_800_SOFC_4_H2O.txt",
        r".\mnt\data\IS_800_SOFC_12_H2O.txt",
        r".\mnt\data\IS_800_SOFC_25_H2O.txt",
        r".\mnt\data\IS_800_SOFC_50_H2O.txt"
    ],
    "SOEC": [
        r".\mnt\data\IS_800_SOEC_4_H2O.txt",
        r".\mnt\data\IS_800_SOEC_12_H2O.txt",
        r".\mnt\data\IS_800_SOEC_25_H2O.txt",
        r".\mnt\data\IS_800_SOEC_50_H2O.txt"
    ]
}

# Plot Nyquist plots for both SOFC and SOEC modes with adjusted column names
for mode, files in impedance_files.items():
    plt.figure(figsize=(10, 6))
    for file in files:
        data = pd.read_csv(file, sep="\s+")
        plt.plot(data["Z'"], data["Z''"], label=f"{file.split('/')[-1].split('_')[2]} H2O")

    plt.xlabel("Z' (Real Impedance, Ω)")
    plt.ylabel("Z'' (Imaginary Impedance, Ω)")
    plt.title(f"Nyquist Plot for {mode} Mode")
    plt.legend(title="% H2O")
    plt.grid(True)
    plt.savefig(rf".\plots\nyquist_plot_{mode.lower()}_mode.png", dpi=150)
    plt.show()

# Load one impedance spectroscopy data file to check the column names
data_example = pd.read_csv(r".\mnt\data\IS_800_SOFC_4_H2O.txt", sep="\s+")
print(data_example.columns)
