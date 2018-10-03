import subprocess
import time

for i in range(5):
	subprocess.call("adb shell input keyevent 5",shell=True)
	time.sleep(3)
	subprocess.call("adb shell input keyevent 3",shell=True)
	time.sleep(3)