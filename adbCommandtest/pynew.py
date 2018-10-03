import subprocess
import os
print("the devices found are")
result=subprocess.check_output("adb devices",shell=True)
print("the devices connected are")
#for i in result:
print(result)
print("enter the device no")
input1=raw_input()
cmd1="adb -s "+input1+" shell"
var1=os.system(cmd1)