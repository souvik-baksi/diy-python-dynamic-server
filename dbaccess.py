import re

def csvread(line):
	pass

def pagecontent(page):
	f = open(r'.\db\pagedb.txt',mode='r')
	line = f.readline()
	while line:
		page_r=re.findall(r'[\w\s]+',line)
		if page_r:
			if page_r[0]==page:
				return page_r[1]
		line = f.readline()

if __name__=='__main__':
	print pagecontent('home')