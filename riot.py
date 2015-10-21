import pandas as pd

d_cols = ['station_mac', 'first_seen', 'manufacturer', 'power', 'probed_ssid', 'last_seen', 'riot_id', 'current_ap_bssid', 'current_ap_essid', 'poweron_mac', 'fip_essid', 'time']


devices = pd.read_csv('files/file.csv', sep=",", names=d_cols)
devices['time'] = devices['time'].convert_objects(convert_numeric=True)


print(devices[(devices.time > 1445368920) & (devices.time < 1445372520) & (devices.station_mac == 'F0:25:B7:8B:9E:28')])
