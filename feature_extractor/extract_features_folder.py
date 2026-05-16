import librosa
import numpy as np
import pandas as pd
import os

def extract_features(wav_path, sr=22050):
    y, sr = librosa.load(wav_path, sr=sr)
    features = {}

    # MFCCs (13 coefficients)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    for i in range(13):
        features[f"mfcc_{i+1}_mean"] = np.mean(mfccs[i])
        features[f"mfcc_{i+1}_std"] = np.std(mfccs[i])

    # Spectral Centroid
    sc = librosa.feature.spectral_centroid(y=y, sr=sr)[0]
    features["spectral_centroid_mean"] = np.mean(sc)
    features["spectral_centroid_std"] = np.std(sc)

    # Spectral Bandwidth
    sb = librosa.feature.spectral_bandwidth(y=y, sr=sr)[0]
    features["spectral_bandwidth_mean"] = np.mean(sb)
    features["spectral_bandwidth_std"] = np.std(sb)

    # Spectral Flatness
    sf = librosa.feature.spectral_flatness(y=y)[0]
    features["spectral_flatness_mean"] = np.mean(sf)
    features["spectral_flatness_std"] = np.std(sf)

    # Spectral Rolloff
    sr_feat = librosa.feature.spectral_rolloff(y=y, sr=sr)[0]
    features["spectral_rolloff_mean"] = np.mean(sr_feat)

    # RMS Energy
    rms = librosa.feature.rms(y=y)[0]
    features["rms_energy_mean"] = np.mean(rms)
    features["rms_energy_std"] = np.std(rms)

    # Zero-Crossing Rate
    zcr = librosa.feature.zero_crossing_rate(y)[0]
    features["zcr_mean"] = np.mean(zcr)
    features["zcr_std"] = np.std(zcr)

    return features

df = pd.DataFrame()
for comp_type in os.listdir("C:\\Users\\sanid\\PycharmProjects\\Listen\\components"):
    for comp_type_id in os.listdir(f"C:\\Users\\sanid\\PycharmProjects\\Listen\\components\\{comp_type}"):
        for comp_type_id_state in os.listdir(f"C:\\Users\\sanid\\PycharmProjects\\Listen\\valve\\{comp_type}\\{comp_type_id}"):
            for filename in os.listdir(f"C:\\Users\\sanid\\PycharmProjects\\Listen\\valve\\{comp_type}\\{comp_type_id}\\{comp_type_id_state}"):
                features = extract_features(f"C:\\Users\\sanid\\PycharmProjects\\Listen\\valve\\{comp_type}\\{comp_type_id}\\{comp_type_id_state}\\{filename}")
                df_features = pd.DataFrame([features])
                df = pd.concat([df, df_features], ignore_index=True)
                print("Done with ", filename)
            print(f"Done with {comp_type_id}")
            df.to_csv(f"{comp_type}_{comp_type_id}_{comp_type_id_state}", index=False)

