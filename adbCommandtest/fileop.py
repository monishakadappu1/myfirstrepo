import os

class FileIO:
	def __init__(self,filename):
		self.filename=filename
	
	def fileread(self):
		f=open(self.filename,'r+')
		lines=f.read()
		print(lines)
		f.close()
	
	def fileline(self,n):
		with open(self.filename,'r') as f:
			for i in range(n) :
				print(f.readline().strip())
			f.close()
	
	def filewrite(self,writetext):
		f=open(self.filename,'a')
		f.write(writetext)
		f.close()
		f=open(self.filename,'r')
		print(str(f.read()))
		f.close()
	
	def filereadtail(self,n):
		f=open(self.filename,'r')
		lines=f.readlines()
		lines1=map(lambda i:i.strip(),lines)
		print (lines1)
		i=1
		for i in range(1,n):
			print(lines1[-i])
		f.close()
	
	def readtail(self,n):
		f=open(self.filename,'r')
		#lines=f.readlines()
		#EOF=f.tell()
		for i in range(1,n):
			f.seek(-i,2)
			print(f.readline())
		f.close()

	def longestword(self):
		f=open(self.filename,'r')
		lines=f.readlines()
		maxwords=[]
		for i in lines:
			i2=i.strip()
			#print(i2)
			list1=i2.split(" ")
			lengthlist=map(lambda j : len(j),list1)
			thisDict=dict(zip(lengthlist,list1))
			intmax=max(lengthlist)
			maxwords.append(thisDict[intmax])
		lengthlist=map(lambda j : len(j),maxwords)
		Dict2=dict(zip(lengthlist,maxwords))
		maxWord=max(Dict2.keys())
		print(Dict2[maxWord])
		f.close()
		
	def sizeof(self):
		#f=open(filename,'r')
		#f.s
		fileinfo=os.stat(self.filename)
		print str(fileinfo)
		return fileinfo.st_size
	

	def writeList(self,list2):
		f=open(self.filename,'a')
		#f.write(list2)
		map(lambda i : f.write(i),list2)
		f.close()

	def copycontents(self,filename2):
		f1=open(self.filename,'r')
		f2=open(filename2,'w')
		content=f1.read()
		print(content)
		f2.write(str(content))
		f1.close()
		f2.close()

def main():
	fileop=FileIO("D:\\sampletext.txt")
	fileop.fileread()
	fileop.fileline(3)
	fileop.filewrite("fifth line")
	fileop.filereadtail(3)
	#fileop.readtail()
	fileop.longestword()
	print(fileop.sizeof())
	writewords=["hello world\n","hope you all are doing good\n","lets look at how this \n","list gets written onto\n"]
	fileop.writeList(writewords)
	fileop.copycontents("D:\\sampletext2.txt")
	
if __name__ == "__main__":
    main()
#fileread("D:\\sampletext.txt")
#fileline("D:\\sampletext.txt",3)
#filewrite("D:\\sampletext.txt","fifth line")
#filereadtail("D:\\sampletext.txt",3)
#readtail("D:\\sampletext.txt",3)   not right
#longestword("D:\\sampletext.txt")
#print(sizeof("D:\\sampletext.txt"))
# writewords=["hello world\n","hope you all are doing good\n","lets look at how this \n","list gets written onto\n"]
# writeList("D:\\sampletext.txt",writewords)
#copycontents("D:\\sampletext.txt","D:\\sampletext2.txt")
