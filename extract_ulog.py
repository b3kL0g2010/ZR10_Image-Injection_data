from pyulog import ULog
import pandas as pd

ulog = ULog("log_27_2026-1-13-11-15-06.ulg")

gps_ds = ulog.get_dataset("vehicle_gps_position")
att_ds = ulog.get_dataset("vehicle_attitude")

gps = gps_ds.data
att = att_ds.data

gps_df = pd.DataFrame({
    "timestamp": gps["timestamp"],
    "utc_usec": gps["time_utc_usec"],
    "lat": gps["latitude_deg"],
    "lon": gps["longitude_deg"],
    "alt_msl": gps["altitude_msl_m"]
})

att_df = pd.DataFrame({
    "timestamp": att["timestamp"],
    "q0": att["q[0]"],
    "q1": att["q[1]"],
    "q2": att["q[2]"],
    "q3": att["q[3]"]
})

gps_df.to_csv("gps.csv", index=False)
att_df.to_csv("attitude.csv", index=False)

print("✔ GPS (with UTC) and attitude extracted")
