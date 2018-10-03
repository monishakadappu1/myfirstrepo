import subprocess
import time

def delDcim():
	subprocess.call(cmd2,shell=True)
	result2=subprocess.check_output(cmd1,shell=True)
	return result2
	
def deviceFound():
	result=subprocess.check_output("adb devices",shell=True)
	return result

modeCheck="adb shell su"
cmd1="adb shell ls /storage/emulated/0/"
cmdcam="adb shell am start -a android.media.action.IMAGE_CAPTURE"
cmd2="adb shell rm -rf /storage/emulated/0/DCIM"
cmd3="adb reboot"
cmd4="adb shell input keyevent 27"
cmd5="adb wait-for-device"

result0=subprocess.check_output(modeCheck,shell=True) 
subprocess.call("exit",shell=True)

if result0=="su command not found":
	print("clearing is not p[ossible ,pls make it test version")
else:
	print("device found and performing test")
	result5=deviceFound()
	if "device" in result5:
		print("the device is connected")
		result1=subprocess.check_output(cmd1,shell=True)
		if "DCIM" in result1:
			print("DCIM already found deleting files")
			result2=delDcim()
			if "DCIM" in result2: 
				print("file not deleted")
			else:
				print("file deleted")
				#subprocess.call(cmd3,shell=True)
				#subprocess.call(cmd5,shell=True)
				#time.sleep(30)
				result3=subprocess.check_output(cmd1,shell=True)
				if "DCIM" in result3: 
					print("DCIM still found error")
				else:
					print("file is not present after deleting ,now taking new photo")
					subprocess.call(cmdcam,shell=True)
					subprocess.call(cmd4,shell=True)
					result4=subprocess.check_output(cmd1,shell=True)
					if "DCIM" in result4:
						print("Camera folder deleted and successfull created after new flash")
					else:
						print("failed testcase")
	else:
		print("device not connected")
	