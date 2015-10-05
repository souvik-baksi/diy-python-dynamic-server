content='BAAL'

from string import replace
from re import findall

template=''
f = open('template.html',mode='r')
line = f.readline()
while line:
	template=template+line 
	line = f.readline()

match=findall('<python>.+<python>',template)
match=[replace(l,'<python>','') for l in match ]
template = replace(template,'<python>','')
statement ='replacement =' +match[0]
exec statement
template=replace(template,match[0],replacement)
