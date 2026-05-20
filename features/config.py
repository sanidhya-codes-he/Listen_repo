from pathlib import Path

BASE_DIR = Path(__file__).parent  # C:\Users\sanid\PycharmProjects\Listen

SAMPLING_RATE = 16000
N_FFT = 2048
HOP_LENGTH = 512
N_MELS = 128
FIXED_WIDTH = 313

INPUT_DIRS = [
    BASE_DIR / "feature_extraction/raw_data/slider/id_00",
    BASE_DIR / "feature_extraction/raw_data/slider/id_02",
    BASE_DIR / "feature_extraction/raw_data/slider/id_04",
    BASE_DIR / "feature_extraction/raw_data/slider/id_06",
]
OUTPUT_DIRS = [
    BASE_DIR / "processed_features/slider/id_00",
    BASE_DIR / "processed_features/slider/id_02",
    BASE_DIR / "processed_features/slider/id_04",
    BASE_DIR / "processed_features/slider/id_06",
]
SCALER_DIRS = [
    BASE_DIR / "scalers/slider/id_00",
    BASE_DIR / "scalers/slider/id_02",
    BASE_DIR / "scalers/slider/id_04",
    BASE_DIR / "scalers/slider/id_06",
]
