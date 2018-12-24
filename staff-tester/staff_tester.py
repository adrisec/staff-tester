"""
Staff Tester project
-Main working module-
Author: Adrian Navas <adrian dot navas dot ajenjo1 @ gmail dot com>
"""

import smtplib
import re
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import os

error_msg = "[!] ERROR:"

#TODO: add if it's possible more security to conections.
#TODO: check user inputs to avoid possible attacks
#TODO: documentation

def open_server(conf):
	"""Creates a server and the mime_message without the body
	Sends mails to all targets using conf dict creating a MIME message


	Params:
	conf -- contains all info needed to connect the server and create the mail except the target list

	
	*conf dictionary has: smtp_user,smtp_password,body,sent_from,subject,smtp_server,smtp_port
	
	
	"""
	smtp_user = conf["smtp_user"] 
	smtp_password = conf["smtp_password"]

	
	try:  
		server = smtplib.SMTP(conf["smtp_server"], conf["smtp_port"])
		server.starttls()
		server.ehlo()
		server.login(smtp_user, smtp_password)
		return server

	except Exception as e:
		raise Exception(e)

def send_mail(server,to,conf,body):
	"""Sends mails to all targets using conf dict creating a MIME message


	Params:
	server -- open SMTP server 
	to -- target list
	conf -- contains all info needed to create the mail except the target list
	body -- contains the HTML mail body
	
	"""
	mime_message = MIMEMultipart()

	fattachment = conf["attachment"]
	if(fattachment != ""):
		attachment = MIMEApplication(open(fattachment,"rb").read())
		if(conf["attachment_name"] == ""):
			split = fattachment.split("/")
			fname = split[-1]
		else:
			fname = conf["attachment_name"]
		attachment.add_header('Content-Disposition', 'attachment', filename=fname)
		mime_message.attach(attachment)

	mime_message["From"] = conf["sent_from"]
	mime_message["Subject"] = conf["subject"]
	mime_message.attach(body)

	try:
		server.sendmail(conf["sent_from"], to, mime_message.as_string())
	except Exception as e:
		raise Exception(e)
	return True
	

def parse_mail(text,params,mail):
	"""Parses mail line by line, checking if there are any parameter included at mail and if so,
	it changes them using the params argument received


	Params:
	text -- contains html body as string
	params -- contains params used to fill the mail custom params
	mail -- target mail. Used only in case of error

	Returns:
	new html custom message
	
	"""
	body = ""
	regex = re.compile(r"[^\[]*\[[^\]]+\][\[.\]]*")
	regex_find = re.compile(r"\[[^\[ ]*\]")
	for line in text:
		line_aux = line
		if(regex.match(line)):
			for term in regex_find.findall(line):
				if term[1:-1] in params:
					line_aux = line_aux.replace(term, params[term[1:-1]])
				else:
					error_msg = "Key " + term[1:-1] + " not found. Check that var " 
					error_msg += term[1:-1] + " is defined at " + mail + " entry"
					raise Exception(error_msg)
		body+=line_aux
	return body

def parse_line(line):
	"""String parser that avoid comment lines (begins with #) and blank lines.
	Then it erases '\n' character if exists and then returns it splitted by '=''


	Params:
	line -- line to parse

	Returns:
	line parsed and splitted
	
	"""
	if line == "\n":
		return None
	i = 0
	while(line[i] == " "):
		i+=1
	if line[i] == "#":
		return None
	if(line[-1] == "\n"):
		return line[0:-1].split(" ")
	else:
		return line.split(" ")

def is_email_valid(email):
	"""Checks if an email is correct using a simple regex check
	

	Params:
	email -- email string to check

	Returns:
	True -- if OK
	False -- if ERROR

	TODO: Improve email regular expression
	
	"""
	mail_regex = re.compile(r"[^@]+@[^@]+\.[^@]+") 

	if not mail_regex.match(email):
		return False
	return True

def init(params):
	"""Reads all files required
	

	Params:
	params -- object that contains all info needed

	Returns:
	True -- if OK
	False -- if ERROR
	
	"""
	conf = {}
	conf_req = ["smtp_user","smtp_password","sent_from","subject","smtp_server","smtp_port"]

	#Config params reading
	
	conf["smtp_server"] = params.smtp_server.get()
	conf["smtp_user"] = params.smtp_user.get()
	conf["smtp_password"] = params.smtp_password.get()
	conf["sent_from"] = params.sent_from.get()
	conf["smtp_port"] = params.smtp_port.get()
	conf["subject"] = params.subject.get()
	conf["attachment"] = params.fattachment.get()
	conf["attachment_name"] = params.attachment_name.get()

	for key in conf_req:
		if not key in conf:
			error = error_msg + " '" +  key + "'' is not present on conf file"
			raise Exception(error)

	#Target mails reading
	to_params = {}
	try:
		g = open(params.ftarget.get(),"r",encoding="ISO-8859-1")
	except:
		error = error_msg + " can't open target list file, check filename"
		raise Exception(error)
	for line in g:
		ret = parse_line(line)
		if(ret != None):
			if(len(ret)>0):
				if(is_email_valid(ret[0])):
					dicc = {}
					for entry in ret:
						new = entry.split("=")
						if(len(new)>1):
							dicc[new[0]] = new[1]
					to_params[ret[0]] = dicc
	g.close()

	
	#mail reading
	try:
		h = open(params.fmail.get(),"r",encoding="ISO-8859-1")
		mail = h.readlines()
	except:
		error = error_msg + " can't open mail file, check filename"
		raise Exception(error)

	if(len(to_params) < 1):
		error = error_msg + " Target list is empty or it doesn't any valid mails, check filename"
		raise Exception(error)

	else:
		server = open_server(conf)
		try:
			for key in to_params:
				text = parse_mail(mail,to_params[key],key)
				message = MIMEText(text, "html")
				send_mail(server,key,conf,message)
			server.close()
			return True

		except Exception as e:
			raise Exception(e)