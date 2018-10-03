import subprocess
import os 
import time
from uiautomator import Device
from subprocess import PIPE, Popen

class Phone:
	def __init__(self):
		self.AppName={'camera' : 'org.codeaurora.snapcam/com.android.camera.CameraLauncher',
			 'Photos' : 'com.google.android.apps.photos/com.google.android.apps.photos.home.HomeActivity',
			 'gmail' : 'com.google.android.gm/com.google.android.gm.ConversationListActivityGmail',
			 'Phone' : 'com.android.dialer/com.android.dialer.app.DialtactsActivity',
			 'contact': 'com.android.contacts/com.android.contacts.activities.PeopleActivity',
			 'chrome' : 'com.android.chrome/com.google.android.apps.chrome.Main',
			 'Settings' : 'com.android.settings/com.android.settings.Settings',
			 'playmusic' : 'com.google.android.music/com.android.music.activitymanagement.TopLevelActivity1'
				}
				
	
	def launch_App(self,name):
		#p=Popen(["adb","shell","am","start","-n",self.AppName[name]],stdin=PIPE,stdout=PIPE)
		p=Popen(["adb","shell","am","start","-n",self.AppName[name]])
		print p
	
device1=Phone()
device1.launch_App("playmusic")

# com.android.dialer/com.android.dialer.DialtactsActivity

# com.android.dialer/com.android.dialer.DialtactsActivity