import subprocess
import time

cmd="adb reboot"
cmd2="adb wait-for-device"
cmd1="adb shell dumpsys battery"
c="adb shell get serial
for i in range(3):
	subprocess.call(cmd,shell=True)
	subprocess.call(cmd2,shell=True)
	f=subprocess.check_output(cmd1,shell=True)
#print(f)
	if 'USB powered' not in f: 
		print("Its not in Homescreen")
	else:
		print("fl")
	
	time.sleep(30)
	g=subprocess.check_output(cmd1,shell=True)
#print(g)
	if 'USB powered' in g: 
		print("Its in Homescreen")
		c+=1
	else:
		print("Testcase failed")
		break

#print(result)
