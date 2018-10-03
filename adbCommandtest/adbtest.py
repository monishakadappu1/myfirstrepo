from lttsadblibrary import ADB

def adbmethods(device):
	#ADB()
	sno=ADB.adb_get_serial_number(device)     #get serial working 
	print(sno)
	print(device.adb_set_serial(deviceno))        #set serial also working fine
	#device.adb_push_data("cameraop.py")				#working
	#device.adb_pull_data("/sdcard/cameraop.py")
	print(device.adb_get_build_details())				#working
	print(device.adb_get_build_type())
	print(device.adb_get_sdk_version())
	print(device.adb_get_security_patch_version())
	print(device.adb_get_android_version())
	device.adb_get_manufacturer_detail()
	device.adb_get_model_name()
	device.adb_get_battery_percent()
	print(device.adb_get_battery_voltage())
	print(device.adb_get_battery_temperature())
	print(device.adb_check_battery_presence())
	#print(device.adb_get_approximate_battery_remaining_time())										#wont work on 8.0 coz there is no property called time in dumpsys battery
	print(device.adb_get_bluetooth_status())
	print(device.adb_get_bluetooth_address())
	print(device.adb_get_cpu_utilisation())
	print(device.adb_get_display_brightness())
	device.adb_get_auto_brightness_status()
	device.adb_get_ram_utilisation()
	device.adb_get_stay_awake_status()
	device.adb_get_mobile_data_status()
	device.adb_get_wifi_status()
	device.adb_get_wifi_mac_id()
	device.adb_get_flight_mode_status()
	device.adb_get_location_service_status()
device=ADB()
deviceno="18073522504556"
adbmethods(device)