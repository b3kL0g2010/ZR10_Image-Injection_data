import pandas as pd

INTERVAL = 3  # ever 3 seconds?

gps = pd.read_csv("gps_utc.csv")
att = pd.read_csv("attitude.csv")

gps["utc"] = pd.to_datetime(gps["utc"])
att["timestamp"] = pd.to_datetime(att["timestamp"], unit="us")

start = gps["utc"].iloc[0]
end = gps["utc"].iloc[-1]

sample_times = pd.date_range(start=start, end=end, freq=f"{INTERVAL}s")

samples = pd.DataFrame({"utc": sample_times})

samples = pd.merge_asof(
    samples,
    gps.sort_values("utc"),
    on="utc",
    direction="nearest",
    tolerance=pd.Timedelta(seconds=1)
)

samples.to_csv("sampled_metadata.csv", index=False)

print("✔ Telemetry sampled at 5-second intervals")
