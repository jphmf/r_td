import pandas as pd
import matplotlib as plt

d_cols = ['station_mac', 'first_seen', 'manufacturer', 'power', 'probed_ssid', 'last_seen', 'riot_id', 'current_ap_bssid', 'current_ap_essid', 'poweron_mac', 'fip_essid', 'time']




devices = pd.read_csv('files/file.csv', sep=",", names=d_cols)
devices['time'] = devices['time'].convert_objects(convert_numeric=True)


#print(devices[(devices.time > 1445368920) & (devices.time < 1445372520) & (devices.station_mac == 'F0:25:B7:8B:9E:28')])

most_viewed = devices.groupby('manufacturer').size().order(ascending=False).head()

devices_outliers = devices.station_mac[devices.power > -10].value_counts()


devices_normal = devices.station_mac[devices.power < -20].value_counts()

devices_stats = devices.groupby('manufacturer').agg({'power': [np.size, np.median]})

# samsung - 3:23 - 4:23
samsung_s1 = devices[(devices.time >1445368980) & (devices.time < 1445372580) & (devices.station_mac == 'F0:25:B7:8B:9E:28')].groupby('manufacturer').agg({'power': [np.size, np.median]})



print(devices.power.describe())
