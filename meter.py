import pandas as pd
import matplotlib as plt
import numpy as np

d_cols = ['station_mac', 'first_seen', 'manufacturer', 'power', 'probed_ssid', 'last_seen', 'riot_id', 'current_ap_bssid', 'current_ap_essid', 'poweron_mac', 'fip_essid', 'time']

devices = pd.read_csv('files/devices_23_10_manha.csv', sep=",", names=d_cols)
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
#(2,5)

# motorola - 3:28 - 3:33
motorola_p2 = devices[(devices.time >1445365680) & (devices.time < 1445365980) & (devices.station_mac == '5C:51:88:D4:43:F1')].groupby('station_mac').agg({'power':[np.size, np.median]})
#5C:51:88:D4:43:F1    23    -81
#(4,5)


# motorola - 3:33 - 3:38
motorola_p3 = devices[(devices.time >1445365980) & (devices.time < 1445366280) & (devices.station_mac == '5C:51:88:D4:43:F1')].groupby('station_mac').agg({'power':[np.size, np.median]})
#5C:51:88:D4:43:F1     6    -88
#(4,4)


# motorola - 3:38 - 3:43
motorola_p4 = devices[(devices.time >1445366280) & (devices.time < 1445366580) & (devices.station_mac == '5C:51:88:D4:43:F1')].groupby('station_mac').agg({'power':[np.size, np.median]})
#5C:51:88:D4:43:F1    15    -75
#(2,4)


# motorola - 3:43 - 3:48
motorola_p5 = devices[(devices.time >1445366580) & (devices.time < 1445366880) & (devices.station_mac == '5C:51:88:D4:43:F1')].groupby('station_mac').agg({'power':[np.size, np.median]})
#5C:51:88:D4:43:F1     9    -89
#(0,4)

# motorola - 3:48 - 3:53
motorola_p6 = devices[(devices.time >1445366880) & (devices.time < 1445367180) & (devices.station_mac == '5C:51:88:D4:43:F1')].groupby('station_mac').agg({'power':[np.size, np.median]})
#5C:51:88:D4:43:F1     6    -86
#(0,2)

# motorola - 3:53 - 3:58
motorola_p7 = devices[(devices.time >1445367180) & (devices.time < 1445367480) & (devices.station_mac == '5C:51:88:D4:43:F1')].groupby('station_mac').agg({'power':[np.size, np.median]})
#5C:51:88:D4:43:F1     2    -85
#(1,1)


# motorola - 3:58 - 4:03
motorola_p8 = devices[(devices.time >1445367480) & (devices.time < 1445367780) & (devices.station_mac == '5C:51:88:D4:43:F1')].groupby('station_mac').agg({'power':[np.size, np.median]})
# vazio
#(3,1)

# motorola - 4:03 - 4:08
motorola_p9 = devices[(devices.time >1445367780) & (devices.time < 1445368080) & (devices.station_mac == '5C:51:88:D4:43:F1')].groupby('station_mac').agg({'power':[np.size, np.median]})
#5C:51:88:D4:43:F1     6    -87
#(5,2)

# motorola - 4:09 - 4:14
motorola_p10 = devices[(devices.time >1445368140) & (devices.time < 1445368440) & (devices.station_mac == '5C:51:88:D4:43:F1')].groupby('station_mac').agg({'power':[np.size, np.median]})
#5C:51:88:D4:43:F1    12    -86
#(2,2)

# motorola - 4:14 - 4:19
motorola_p11 = devices[(devices.time >1445368440) & (devices.time < 1445368740) & (devices.station_mac == '5C:51:88:D4:43:F1')].groupby('station_mac').agg({'power':[np.size, np.median]})
#5C:51:88:D4:43:F1    22    -75
#(3,3)

# motorola - 4:20 - 4:22
motorola_p12 = devices[(devices.time >1445368800) & (devices.time < 1445368920) & (devices.station_mac == '5C:51:88:D4:43:F1')].groupby('station_mac').agg({'power':[np.size, np.median]})
#5C:51:88:D4:43:F1     1    -89
#(0,5)


#Dados do segundo teste

#16:05 - 16:09 - (3,1)
motorola_a1 = devices[(devices.time >1445540700) & (devices.time <1445540940 ) & (devices.station_mac == '5C:51:88:D4:43:F1')].groupby('station_mac').agg({'power':[np.size, np.median]})

#16:10 - 16:14 - (1,3)
motorola_a2 = devices[(devices.time >1445541000) & (devices.time <1445541240 ) & (devices.station_mac == '5C:51:88:D4:43:F1')].groupby('station_mac').agg({'power':[np.size, np.median]})

#16:14 - 16:16 - (3,5)
motorola_a3 = devices[(devices.time >1445541240) & (devices.time <1445541420 ) & (devices.station_mac == '5C:51:88:D4:43:F1')].groupby('station_mac').agg({'power':[np.size, np.median]})

#16:14 - 16:16 - (3,5)
motorola_a4 = devices[(devices.time >1445541540) & (devices.time <1445541720 ) & (devices.station_mac == '5C:51:88:D4:43:F1')].groupby('station_mac').agg({'power':[np.size, np.median]})

print(motorola_a1, motorola_a2, motorola_a3, motorola_a4)

"""
:51:88:D4:43:F1      8     -64

[1 rows x 2 columns],                    power        
                    size  median
station_mac                     
5C:51:88:D4:43:F1      9     -71

[1 rows x 2 columns],                    power        
                    size  median
station_mac                     
5C:51:88:D4:43:F1      8     -76

[1 rows x 2 columns],                    power        
                    size  median
station_mac                     
5C:51:88:D4:43:F1     14     -75
"""


#16:05 - 16:09 - (3,1)
samsung_a1 = devices[(devices.time >1445540700) & (devices.time <1445540940 ) & (devices.station_mac == 'F0:25:B7:8B:9E:28')].groupby('station_mac').agg({'power':[np.size, np.median]})

#16:10 - 16:14 - (1,3)
samsung_a2 = devices[(devices.time >1445541000) & (devices.time <1445541240 ) & (devices.station_mac == 'F0:25:B7:8B:9E:28')].groupby('station_mac').agg({'power':[np.size, np.median]})

#16:14 - 16:16 - (3,5)
samsung_a3 = devices[(devices.time >1445541240) & (devices.time <1445541420 ) & (devices.station_mac == 'F0:25:B7:8B:9E:28')].groupby('station_mac').agg({'power':[np.size, np.median]})

#16:14 - 16:16 - (3,5)
samsung_a4 = devices[(devices.time >1445541540) & (devices.time <1445541720 ) & (devices.station_mac == 'F0:25:B7:8B:9E:28')].groupby('station_mac').agg({'power':[np.size, np.median]})

print(samsung_a1, samsung_a2, samsung_a3, samsung_a4)

print (devices[(devices.time > 1445609357) & (devices.time < 1445610137)].groupby('last_seen').agg({'power':[np.size, np.median]}))
