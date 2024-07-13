from os.path import join

from pandas import read_csv, concat


def load_ocv_data(data_path: str):
    """Load OCV data from the specified path."""
    ocv1_data = read_csv(join(data_path, "ocv1_reductionH2_H2O_4.txt"), sep=r"\s+")
    ocv2_data = read_csv(join(data_path, "ocv2_H2O_4_to_12.txt"), sep=r"\s+")
    ocv_data = concat([ocv1_data, ocv2_data], ignore_index=True)
    return ocv_data


def load_data_files(data_path: str, file_patterns: dict):
    """Load data files for given file patterns."""
    return {
        mode: [join(data_path, filename) for filename in filenames]
        for mode, filenames in file_patterns.items()
    }
