#code by Punuy_48_TGT
#Python 3.7.4
#Version 0.1

import os
import time
import winwifi

#Setting Wi-Fi and Time Refresh!
wifi = "[ Enter Wi-Fi name here it! ]"
timerefrsh = 300

def auto_connect(Wifi_name=None,timerefresh=300) :
	if not Wifi_name is None :
		try :
			os.system('netsh wlan disconnect interface="Wi-Fi"')
			time.sleep(0.5)
			winwifi.WinWiFi.connect(Wifi_name)
			print(f"Wifi Connect {Wifi_name}")
			time.sleep(timerefresh)
		except :
			pass
	else :
		raise Exception("Please enter Wi-Fi name!")
		
if __name__ == "__main__" :
	while True :
		auto_connect(Wifi_name=wifi,timerefresh=timerefresh)
