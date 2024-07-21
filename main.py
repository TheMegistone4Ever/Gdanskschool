from os.path import exists, join

from data_processing import load_ocv_data, load_data_files
from plot_utils import (create_directory_if_not_exists, plot_ocv_vs_time, plot_i_v_curves, plot_p_i_curves,
                        plot_nyquist_curves)

DATA_PATH = r".\mnt\data"
PLOTS_PATH = r".\plots"

# Ensure the data path exists
if not exists(DATA_PATH):
    raise FileNotFoundError(f"Data path \"{DATA_PATH}\" does not exist, exiting...")

# Ensure the plots directory exists
create_directory_if_not_exists(PLOTS_PATH)

# Load the OCV data
ocv_data = load_ocv_data(DATA_PATH)
plot_ocv_vs_time(ocv_data, save_path=join(PLOTS_PATH, "ocv_vs_time.png"))

# Define data file patterns
impedance_file_patterns = {
    "SOFC": [
        "800_SOFC_test_4_H2O.txt",
        "800_SOFC_test_12_H2O.txt",
        "800_SOFC_test_25_H2O.txt",
        "800_SOFC_test_50_H2O.txt",
    ],
    "SOEC": [
        "800_SOEC_test_4_H2O.txt",
        "800_SOEC_test_12_H2O.txt",
        "800_SOEC_test_25_H2O.txt",
        "800_SOEC_test_50_H2O.txt",
    ],
}

nyquist_file_patterns = {
    "SOFC": [
        "IS_800_SOFC_4_H2O.txt",
        "IS_800_SOFC_12_H2O.txt",
        "IS_800_SOFC_25_H2O.txt",
        "IS_800_SOFC_50_H2O.txt",
    ],
    "SOEC": [
        "IS_800_SOEC_4_H2O.txt",
        "IS_800_SOEC_12_H2O.txt",
        "IS_800_SOEC_25_H2O.txt",
        "IS_800_SOEC_50_H2O.txt",
    ],
}

# Load data files
impedance_files = load_data_files(DATA_PATH, impedance_file_patterns)
nyquist_files = load_data_files(DATA_PATH, nyquist_file_patterns)

# Plot I-V and P-I curves for both SOFC and SOEC modes
for mode, files in impedance_files.items():
    plot_i_v_curves(files, mode, save_path=join(PLOTS_PATH, f"iv_curves_{mode.lower()}_mode.png"))
    plot_p_i_curves(files, mode, save_path=join(PLOTS_PATH, f"pi_curves_{mode.lower()}_mode.png"))

# Plot Nyquist curves for both SOFC and SOEC modes
for mode, files in nyquist_files.items():
    plot_nyquist_curves(files, mode, save_path=join(PLOTS_PATH, f"nyquist_plot_{mode.lower()}_mode.png"))
