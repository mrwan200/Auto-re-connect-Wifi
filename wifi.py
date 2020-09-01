#code by Punuy_48_TGT
#Python 3.7.x
#Version 0.1

import os
import time
import winwifi

def infinity():
    i=0
    while True:
        i+=1
        yield i

for i in infinity():
	try:

		Wifi_name = 'Kctc-wifi' #nane wifi

		os.system('netsh wlan disconnect interface="Wi-Fi"')
		print('Wifi Disconnect')
		time.sleep(1)
		winwifi.WinWiFi.connect(Wifi_name)
		print('Wifi Connect {}'.format(Wifi_name))
		time.sleep(300)

	except Exception:
                continue
