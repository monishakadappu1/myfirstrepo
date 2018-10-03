import subprocess
import time
cmdcam="adb shell am start -a android.media.action.IMAGE_CAPTURE"
cmd="adb shell input keyevent KEYCODE_CAMERA"
cmdop="adb shell am start -n com.google.android.apps.photos/.home.HomeActivity t457"
subprocess.call(cmdcam,shell=True)
subprocess.call(cmd,shell=True)
subprocess.call(cmdop,shell=True)