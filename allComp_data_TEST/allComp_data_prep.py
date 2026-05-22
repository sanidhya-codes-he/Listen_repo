import glob
import numpy as np
import pandas as pd


files_00_abnormal = glob.glob("/Users/hiteshchandra/PycharmProjects/Listen_repo/features/processed_features/fan/id_00/abnormal/*.npy")
array_fan_id_00_abnormal = np.vstack([np.load(f) for f in files_00_abnormal])
fan_id_00_abnormal = pd.DataFrame(array_fan_id_00_abnormal)

files_00_normal = glob.glob("/Users/hiteshchandra/PycharmProjects/Listen_repo/features/processed_features/fan/id_00/normal/*.npy")
array_fan_id_00_normal = np.load("/Users/hiteshchandra/PycharmProjects/Listen_repo/features/processed_features/fan/id_00/normal") if not files_00_normal else np.vstack([np.load(f) for f in files_00_normal])
fan_id_00_normal = pd.DataFrame(array_fan_id_00_normal)


files_02_abnormal = glob.glob("/Users/hiteshchandra/PycharmProjects/Listen_repo/features/processed_features/fan/id_02/abnormal/*.npy")
array_fan_id_02_abnormal = np.vstack([np.load(f) for f in files_02_abnormal])
fan_id_02_abnormal = pd.DataFrame(array_fan_id_02_abnormal)

files_02_normal = glob.glob("/Users/hiteshchandra/PycharmProjects/Listen_repo/features/processed_features/fan/id_02/normal/*.npy")
array_fan_id_02_normal = np.vstack([np.load(f) for f in files_02_normal])
fan_id_02_normal = pd.DataFrame(array_fan_id_02_normal)


files_04_abnormal = glob.glob("/Users/hiteshchandra/PycharmProjects/Listen_repo/features/processed_features/fan/id_04/abnormal/*.npy")
array_fan_id_04_abnormal = np.vstack([np.load(f) for f in files_04_abnormal])
fan_id_04_abnormal = pd.DataFrame(array_fan_id_04_abnormal)

files_04_normal = glob.glob("/Users/hiteshchandra/PycharmProjects/Listen_repo/features/processed_features/fan/id_04/normal/*.npy")
array_fan_id_04_normal = np.vstack([np.load(f) for f in files_04_normal])
fan_id_04_normal = pd.DataFrame(array_fan_id_04_normal)

files_06_abnormal = glob.glob("/Users/hiteshchandra/PycharmProjects/Listen_repo/features/processed_features/fan/id_06/abnormal/*.npy")
array_fan_id_06_abnormal = np.vstack([np.load(f) for f in files_06_abnormal])
fan_id_06_abnormal = pd.DataFrame(array_fan_id_06_abnormal)

files_06_normal = glob.glob("/Users/hiteshchandra/PycharmProjects/Listen_repo/features/processed_features/fan/id_06/normal/*.npy")
array_fan_id_06_normal = np.vstack([np.load(f) for f in files_06_normal])
fan_id_06_normal = pd.DataFrame(array_fan_id_06_normal)



fan0 = pd.concat([fan_id_00_abnormal, fan_id_00_normal], ignore_index=True)
fan2 = pd.concat([fan_id_02_abnormal, fan_id_02_normal], ignore_index=True)
fan4 = pd.concat([fan_id_04_abnormal, fan_id_04_normal], ignore_index=True)
fan6 = pd.concat([fan_id_06_abnormal, fan_id_06_normal], ignore_index=True)

fan = pd.concat([fan0, fan2, fan4, fan6], ignore_index=True)
fan['comp_id']=0



files_00_abnormal = glob.glob("/Users/hiteshchandra/PycharmProjects/Listen_repo/features/processed_features/pump/id_00/abnormal/*.npy")
array_pump_id_00_abnormal = np.vstack([np.load(f) for f in files_00_abnormal])
pump_id_00_abnormal = pd.DataFrame(array_pump_id_00_abnormal)

files_00_normal = glob.glob("/Users/hiteshchandra/PycharmProjects/Listen_repo/features/processed_features/pump/id_00/normal/*.npy")
array_pump_id_00_normal = np.load("/Users/hiteshchandra/PycharmProjects/Listen_repo/features/processed_features/pump/id_00/normal") if not files_00_normal else np.vstack([np.load(f) for f in files_00_normal])
pump_id_00_normal = pd.DataFrame(array_pump_id_00_normal)

files_02_abnormal = glob.glob("/Users/hiteshchandra/PycharmProjects/Listen_repo/features/processed_features/pump/id_02/abnormal/*.npy")
array_pump_id_02_abnormal = np.vstack([np.load(f) for f in files_02_abnormal])
pump_id_02_abnormal = pd.DataFrame(array_pump_id_02_abnormal)

files_02_normal = glob.glob("/Users/hiteshchandra/PycharmProjects/Listen_repo/features/processed_features/pump/id_02/normal/*.npy")
array_pump_id_02_normal = np.vstack([np.load(f) for f in files_02_normal])
pump_id_02_normal = pd.DataFrame(array_pump_id_02_normal)

files_04_abnormal = glob.glob("/Users/hiteshchandra/PycharmProjects/Listen_repo/features/processed_features/pump/id_04/abnormal/*.npy")
array_pump_id_04_abnormal = np.vstack([np.load(f) for f in files_04_abnormal])
pump_id_04_abnormal = pd.DataFrame(array_pump_id_04_abnormal)

files_04_normal = glob.glob("/Users/hiteshchandra/PycharmProjects/Listen_repo/features/processed_features/pump/id_04/normal/*.npy")
array_pump_id_04_normal = np.vstack([np.load(f) for f in files_04_normal])
pump_id_04_normal = pd.DataFrame(array_pump_id_04_normal)

files_06_abnormal = glob.glob("/Users/hiteshchandra/PycharmProjects/Listen_repo/features/processed_features/pump/id_06/abnormal/*.npy")
array_pump_id_06_abnormal = np.vstack([np.load(f) for f in files_06_abnormal])
pump_id_06_abnormal = pd.DataFrame(array_pump_id_06_abnormal)

files_06_normal = glob.glob("/Users/hiteshchandra/PycharmProjects/Listen_repo/features/processed_features/pump/id_06/normal/*.npy")
array_pump_id_06_normal = np.vstack([np.load(f) for f in files_06_normal])
pump_id_06_normal = pd.DataFrame(array_pump_id_06_normal)

pump0 = pd.concat([pump_id_00_abnormal, pump_id_00_normal], ignore_index=True)
pump2 = pd.concat([pump_id_02_abnormal, pump_id_02_normal], ignore_index=True)
pump4 = pd.concat([pump_id_04_abnormal, pump_id_04_normal], ignore_index=True)
pump6 = pd.concat([pump_id_06_abnormal, pump_id_06_normal], ignore_index=True)


pump = pd.concat([pump0, pump2, pump4, pump6], ignore_index=True)
pump['comp_id'] = 1


files_00_abnormal = glob.glob("/Users/hiteshchandra/PycharmProjects/Listen_repo/features/processed_features/valve/id_00/abnormal/*.npy")
array_valve_id_00_abnormal = np.vstack([np.load(f) for f in files_00_abnormal])
valve_id_00_abnormal = pd.DataFrame(array_valve_id_00_abnormal)


files_00_normal = glob.glob("/Users/hiteshchandra/PycharmProjects/Listen_repo/features/processed_features/valve/id_00/normal/*.npy")
array_valve_id_00_normal = np.load("/Users/hiteshchandra/PycharmProjects/Listen_repo/features/processed_features/valve/id_00/normal") if not files_00_normal else np.vstack([np.load(f) for f in files_00_normal])
valve_id_00_normal = pd.DataFrame(array_valve_id_00_normal)


# --- VALVE ID 02 ---
files_02_abnormal = glob.glob("/Users/hiteshchandra/PycharmProjects/Listen_repo/features/processed_features/valve/id_02/abnormal/*.npy")
array_valve_id_02_abnormal = np.vstack([np.load(f) for f in files_02_abnormal])
valve_id_02_abnormal = pd.DataFrame(array_valve_id_02_abnormal)

files_02_normal = glob.glob("/Users/hiteshchandra/PycharmProjects/Listen_repo/features/processed_features/valve/id_02/normal/*.npy")
array_valve_id_02_normal = np.vstack([np.load(f) for f in files_02_normal])
valve_id_02_normal = pd.DataFrame(array_valve_id_02_normal)


# --- VALVE ID 04 ---
files_04_abnormal = glob.glob("/Users/hiteshchandra/PycharmProjects/Listen_repo/features/processed_features/valve/id_04/abnormal/*.npy")
array_valve_id_04_abnormal = np.vstack([np.load(f) for f in files_04_abnormal])
valve_id_04_abnormal = pd.DataFrame(array_valve_id_04_abnormal)

files_04_normal = glob.glob("/Users/hiteshchandra/PycharmProjects/Listen_repo/features/processed_features/valve/id_04/normal/*.npy")
array_valve_id_04_normal = np.vstack([np.load(f) for f in files_04_normal])
valve_id_04_normal = pd.DataFrame(array_valve_id_04_normal)


# --- VALVE ID 06 ---
files_06_abnormal = glob.glob("/Users/hiteshchandra/PycharmProjects/Listen_repo/features/processed_features/valve/id_06/abnormal/*.npy")
array_valve_id_06_abnormal = np.vstack([np.load(f) for f in files_06_abnormal])
valve_id_06_abnormal = pd.DataFrame(array_valve_id_06_abnormal)

files_06_normal = glob.glob("/Users/hiteshchandra/PycharmProjects/Listen_repo/features/processed_features/valve/id_06/normal/*.npy")
array_valve_id_06_normal = np.vstack([np.load(f) for f in files_06_normal])
valve_id_06_normal = pd.DataFrame(array_valve_id_06_normal)

# Combine normal and abnormal data for each ID
valve0 = pd.concat([valve_id_00_abnormal, valve_id_00_normal], ignore_index=True)
valve2 = pd.concat([valve_id_02_abnormal, valve_id_02_normal], ignore_index=True)
valve4 = pd.concat([valve_id_04_abnormal, valve_id_04_normal], ignore_index=True)
valve6 = pd.concat([valve_id_06_abnormal, valve_id_06_normal], ignore_index=True)


# Combine all IDs into a single master valve DataFrame
valve = pd.concat([valve0, valve2, valve4, valve6], ignore_index=True)
valve['comp_id'] = 2



# --- SLIDER ID 00 ---
files_00_abnormal = glob.glob("/Users/hiteshchandra/PycharmProjects/Listen_repo/features/processed_features/slider/id_00/abnormal/*.npy")
array_slider_id_00_abnormal = np.vstack([np.load(f) for f in files_00_abnormal])
slider_id_00_abnormal = pd.DataFrame(array_slider_id_00_abnormal)

# Find and load all .npy files inside the normal folder
files_00_normal = glob.glob("/Users/hiteshchandra/PycharmProjects/Listen_repo/features/processed_features/slider/id_00/normal/*.npy")
array_slider_id_00_normal = np.load("/Users/hiteshchandra/PycharmProjects/Listen_repo/features/processed_features/slider/id_00/normal") if not files_00_normal else np.vstack([np.load(f) for f in files_00_normal])
slider_id_00_normal = pd.DataFrame(array_slider_id_00_normal)


# --- SLIDER ID 02 ---
files_02_abnormal = glob.glob("/Users/hiteshchandra/PycharmProjects/Listen_repo/features/processed_features/slider/id_02/abnormal/*.npy")
array_slider_id_02_abnormal = np.vstack([np.load(f) for f in files_02_abnormal])
slider_id_02_abnormal = pd.DataFrame(array_slider_id_02_abnormal)

files_02_normal = glob.glob("/Users/hiteshchandra/PycharmProjects/Listen_repo/features/processed_features/slider/id_02/normal/*.npy")
array_slider_id_02_normal = np.vstack([np.load(f) for f in files_02_normal])
slider_id_02_normal = pd.DataFrame(array_slider_id_02_normal)


# --- SLIDER ID 04 ---
files_04_abnormal = glob.glob("/Users/hiteshchandra/PycharmProjects/Listen_repo/features/processed_features/slider/id_04/abnormal/*.npy")
array_slider_id_04_abnormal = np.vstack([np.load(f) for f in files_04_abnormal])
slider_id_04_abnormal = pd.DataFrame(array_slider_id_04_abnormal)

files_04_normal = glob.glob("/Users/hiteshchandra/PycharmProjects/Listen_repo/features/processed_features/slider/id_04/normal/*.npy")
array_slider_id_04_normal = np.vstack([np.load(f) for f in files_04_normal])
slider_id_04_normal = pd.DataFrame(array_slider_id_04_normal)


# --- SLIDER ID 06 ---
files_06_abnormal = glob.glob("/Users/hiteshchandra/PycharmProjects/Listen_repo/features/processed_features/slider/id_06/abnormal/*.npy")
array_slider_id_06_abnormal = np.vstack([np.load(f) for f in files_06_abnormal])
slider_id_06_abnormal = pd.DataFrame(array_slider_id_06_abnormal)

files_06_normal = glob.glob("/Users/hiteshchandra/PycharmProjects/Listen_repo/features/processed_features/slider/id_06/normal/*.npy")
array_slider_id_06_normal = np.vstack([np.load(f) for f in files_06_normal])
slider_id_06_normal = pd.DataFrame(array_slider_id_06_normal)


# --- CONCATENATING & LABELLING SLIDER ---
slider0 = pd.concat([slider_id_00_abnormal, slider_id_00_normal], ignore_index=True)
slider2 = pd.concat([slider_id_02_abnormal, slider_id_02_normal], ignore_index=True)
slider4 = pd.concat([slider_id_04_abnormal, slider_id_04_normal], ignore_index=True)
slider6 = pd.concat([slider_id_06_abnormal, slider_id_06_normal], ignore_index=True)

slider = pd.concat([slider0, slider2, slider4, slider6], ignore_index=True)
slider['comp_id'] = 3

data=pd.concat([fan,valve,pump,slider], ignore_index=True);






