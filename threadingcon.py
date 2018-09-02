import threading
import time
from selenium import webdriver
from selenium import common

class myThread(threading.Thread):
	def __init__(self, threadId, name):
		threading.Thread.__init__(self)
		self.threadId=threadId
		self.name=name

	def run(self):
		print(self)
		driver=webdriver.Firefox()
		driver.get("https://www.google.com/")
		driver.quit()
# thread1=myThread(id,"thread1")
# thread1.start()
threadl=[]
for id in range(5):
	threadl.append(myThread(id,"thread"+str(id)))

for worker in threadl:
	worker.start()

print("existing main thread")
