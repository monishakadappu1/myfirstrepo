import re

text = """101 COM    Computers
205 MAT   Mathematics
189 ENG   English""" 
regex=re.compile('\s+')                                   #compiling the regex to the reg expression of one or more spaces 
regex_num=re.compile('\d+')                                #compiing and storing the object is necessary if we are using it many times
def splitSpace1(text):
	words=re.split('\s+',text)
	print("spliting text using re split method")
	print words

def splitSpace2(text):
	words=regex.split(text)
	print("spliting text using regex split method")
	print words
	
def findnum(text):
	numbers=regex_num.findall(text)
	numbers1=re.findall('\d+',text)
	print("getting numbers using regexnum findall")
	print(numbers)
	print("getting numbers using re findall")
	print(numbers1)

def searchpos(text):
	s=re.search('\d+',text)
	print(s.start())
	print(s.end())
	print(text[s.start():s.end()])
	print("this can be more simplified using group")
	print(s.group())

def matchp(text):
	#textmatch=re.match('\d+',text)
	textmatch=regex_num.match(text)
	print(textmatch.group())
	# for i in textmatch.group():
		# print i
	
# def substitutetext(text,orpattern,subpattern):
	# regpat=re.compile(orpattern)
	# print
	
	
def substitutetext(text,orpattern,subpattern):
	regpat=re.compile(orpattern)
	print(regpat.sub(subpattern,text))
	
def extract(text):
	print("extracting all the sub ids")
	print(re.findall)
	
substitutetext(text,'(?!\n)\s+',' ')
#searchpos(text)
# splitSpace1(text)
# splitSpace2(text)
# findnum(text)
#matchp(text)