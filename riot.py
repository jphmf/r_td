import pandas as pd
import matplotlib as plt
import numpy as np

d_cols = ['station_mac', 'first_seen', 'manufacturer', 'power', 'probed_ssid', 'last_seen', 'riot_id', 'current_ap_bssid', 'current_ap_essid', 'poweron_mac', 'fip_essid', 'time']

devices = pd.read_csv('files/file.csv', sep=",", names=d_cols)
devices['time'] = devices['time'].convert_objects(convert_numeric=True)
devices['power']  = devices['power'].convert_objects(convert_numeric=True)

#print(devices[(devices.time > 1445368920) & (devices.time < 1445372520) & (devices.station_mac == 'F0:25:B7:8B:9E:28')])

#most_viewed = devices.groupby('manufacturer').size().order(ascending=False).head()

devices_outliers = devices.station_mac[devices.power > -10].value_counts()


devices_normal = devices.station_mac[devices.power < -20].value_counts()

#devices_stats = devices.groupby('manufacturer').agg({'power': [np.size, np.median]})

# samsung - 3:23 - 4:23
#samsung_s1 = devices[(devices.time >1445368980) & (devices.time < 1445372580) & (devices.station_mac == 'F0:25:B7:8B:9E:28')].groupby('manufacturer').agg({'power': [np.size, np.median]})

# motorola - 3:23 - 3:28
motorola_p1 = devices[(devices.time >1445365380) & (devices.time < 1445365680) & (devices.station_mac == '5C:51:88:D4:43:F1')].groupby('station_mac').agg({'power':[np.size, np.median]})
#5C:51:88:D4:43:F1    28    -65

# motorola - 3:28 - 3:33
motorola_p2 = devices[(devices.time >1445365680) & (devices.time < 1445365980) & (devices.station_mac == '5C:51:88:D4:43:F1')].groupby('station_mac').agg({'power':[np.size, np.median]})
#5C:51:88:D4:43:F1    23    -81

# motorola - 3:33 - 3:38
motorola_p3 = devices[(devices.time >1445365980) & (devices.time < 1445366280) & (devices.station_mac == '5C:51:88:D4:43:F1')].groupby('station_mac').agg({'power':[np.size, np.median]}
