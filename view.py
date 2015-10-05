#!/server/template engine

import socket
import dbaccess
from string import replace
from re import findall

pagelist=['home','about','contact']  #### centralise pagelist

def render(template,content,connection):

	#load HTML Template
	response=''
	f = open(template,mode='r')
	line = f.readline()
	while line:
		response=response+line 
		line = f.readline()

	match=findall('<python>.+<python>',response)
	if match !=[]:
		match=[replace(l,'<python>','') for l in match ]
		response = replace(response,'<python>','')
		statement ='replacement =' +match[0]
		exec statement
		response=replace(response,match[0],replacement)
	connection.send(response)



def respond(page,connection):
	page =page[0]
	if page in pagelist:
		content=dbaccess.pagecontent(page)
		render('template.html',content,connection)

	# render error page
	else:
		page ='404error'
		connection.send('<html><head><title>404</title><body style="background:#000; color: #fff; text-align: center"><h1>ERROR 404</h1><p>Page Not Found<br><br>Python Personal Server</p></body></html>')
	print page,'rendered successfully'