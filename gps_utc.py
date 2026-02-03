import pandas as pd
from datetime import datetime, timezone

gps = pd.read_csv("gps.csv")

gps["utc"] = gps["utc_usec"].apply(
    lambda t: datetime.fromtimestamp(t / 1e6, tz=timezone.utc)
)

gps.to_csv("gps_utc.csv", index=False)

print("✔ GPS timestamps converted to real UTC")
