"""
Staff Tester project
Author: Adrian Navas <adrian dot navas dot ajenjo1 @ gmail dot com>
"""

import smtplib
import re
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import os

error_msg = "[!] ERROR:"

#TODO: change all print() to exceptions so that can be used at GUI module to show errors correctly.
#TODO: add if it's possible more security to conections.
#TODO: check user inputs to avoid possible attacks
#TODO: documentation
#TODO: management of owned employees (possible PHP to handle clicked links or downloaded attachments???????)

def send_mail(conf,to):
	"""Sends mails to all targets using conf dict creating a MIME message


	Params:
	conf -- contains all info needed to connect the server and create the mail except the target list
	to -- target list
	
	*conf dictionary has: smtp_user,smtp_password,body,sent_from,subject,smtp_server,smtp_port

	TODO: check attachment in windows ("/" or "\"??)
	
	"""
	smtp_user = conf["smtp_user"] 
	smtp_password = conf["smtp_password"]

	message = conf["body"]
	mime_message = MIMEMultipart()
	message = MIMEText(message, "html")
	
	mime_message.attach(message)

	fattachment = conf["attachment"]
	if(fattachment != ""):
		attachment = MIMEApplication(open(fattachment,"rb").read())
		split = fattachment.split("/")
		fname = split[-1]
		attachment.add_header('Content-Disposition', 'attachment', filename=fname)
		mime_message.attach(attachment)

	mime_message["From"] = conf["sent_from"]
	
	mime_message["Subject"] = conf["subject"]
	try:  
		server = smtplib.SMTP(conf["smtp_server"], conf["smtp_port"])
		server.starttls()
		server.ehlo()
		server.login(smtp_user, smtp_password)
		server.sendmail(conf["sent_from"], to, mime_message.as_string())
		print("Sent")
		server.close()
	except Exception as e:
		raise Exception(e)


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
		return line[0:-1].split("=")
	else:
		return line.split("=")

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
	to = []

	#Config params reading
	
	conf["smtp_server"] = params.smtp_server.get()
	conf["smtp_user"] = params.smtp_user.get()
	conf["smtp_password"] = params.smtp_password.get()
	conf["sent_from"] = params.sent_from.get()
	conf["smtp_port"] = params.smtp_port.get()
	conf["subject"] = params.subject.get()
	conf["attachment"] = params.fattachment.get()

	for key in conf_req:
		if not key in conf:
			error = error_msg + " '" +  key + "'' is not present on conf file"
			raise Exception(error)

	#Target mails reading
	try:
		g = open(params.ftarget.get(),"r")
	except:
		error = error_msg + " can't open target list file, check filename"
		raise Exception(error)
	for line in g:
		ret = parse_line(line)
		if(ret != None):
			if(len(ret)==1):
				if(is_email_valid(ret[0])):
					to.append(ret[0])
	g.close()

	#mail reading
	try:
		h = open(params.fmail.get(),"r")
	except:
		error = error_msg + " an't open mail file, check filename"
		raise Exception(e)

	conf["body"] = h.read()

	if(len(to) < 1 and conf["body"] == None):
		error = error_msg + " Target list is empty, check filename"
		raise Exception(error)

	else:
		try:
			send_mail(conf,to)
		except Exception as e:
			raise Exception(error)
