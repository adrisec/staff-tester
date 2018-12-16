"""
Staff Tester project
Author: Adrian Navas <adrian dot navas dot ajenjo1 @ gmail dot com>
"""

import staff_tester
from tkinter import * 
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import pickle


class GUI():
	"""
	GUI Interface management class
	It uses one window and two frames to navigate (main frame and settings frame)

	TODO: Improve help frame
	"""

	def __init__(self):

		self.main = Tk()
		self.main.geometry("700x500")
		self.main.resizable(width=False,height=False)
		self.main.configure(bg="beige")
		self.main.title("Staff Tester")

		self.ftarget = StringVar(self.main,value="")
		self.fmail = StringVar(self.main,value="")
		self.fattachment = StringVar(self.main,value="")

		self.smtp_server = StringVar(self.main,value="smtp.enterprise.com")
		self.smtp_port = StringVar(self.main,value="4567")
		self.smtp_user = StringVar(self.main,value="ceo@enterprise.com")
		self.smtp_password = StringVar(self.main,value="password")
		self.sent_from = StringVar(self.main,value="Enterprise CEO <ceo@enterprise.com>")
		self.subject = StringVar(self.main,value="Important file!")
		self.attachment_name = StringVar(self.main,value="")

		menu = Menu(self.main)
		self.main.config(menu=menu)

		mainmenu = Menu(menu)
		menu.add_cascade(label="File", menu=mainmenu)
		mainmenu.add_command(label="New",command=self.create_new)
		mainmenu.add_command(label="Save As",command=self.save)
		mainmenu.add_command(label="Open",command=self.open)
		mainmenu.add_separator()
		mainmenu.add_command(label="Close",command=self.finish)

		settingsmenu = Menu(menu)
		menu.add_cascade(label="Configuration", menu=settingsmenu)
		settingsmenu.add_command(label="Settings",command=self.configuration_frame)
		settingsmenu.add_separator()
		settingsmenu.add_command(label="Help",command=self.help)
		self.frame = None
		self.main_frame()

	def main_frame(self):
		"""
		Creates the main frame
		
		"""
		if(self.frame != None):
			self.frame.destroy()

		self.frame = Frame(self.main)
		self.frame.configure(bg="beige",width=700,height=500)
		self.frame.pack()

		
		sent_from_label = Label(self.frame,text="Sent from name",bg="beige",anchor=W)
		sent_from_label.grid(row=0,column=0,pady=10,padx=10,ipady=5,ipadx=5)
		sent_from_entry = Entry(self.frame,text=self.sent_from,bg="white",width=50).grid(row=0,column=1,pady=10,padx=10,ipady=5,ipadx=5)

		subject_label = Label(self.frame,text="Mail subject",bg="beige",anchor=W)
		subject_label.grid(row=1,column=0,pady=10,padx=10,ipady=5,ipadx=5)
		subject_entry = Entry(self.frame,text=self.subject,bg="white",width=50).grid(row=1,column=1,pady=10,padx=10,ipady=5,ipadx=5)

		target_button = Button(self.frame, text='Select target file', command=self.get_target_file,width=25)
		target_button.grid(row=2,column=0,pady=10,padx=10,ipady=5,ipadx=5)
		target_button_label = Label(self.frame, textvariable=self.ftarget,width=50,bg="white",borderwidth=2, relief="groove",anchor=W)
		target_button_label.grid(row=2,column=1,pady=10,padx=10,ipady=5,ipadx=5)

		mail_button = Button(self.frame, text='Select HTML template mail file', command=self.get_mail_file,width=25)
		mail_button.grid(row=3,column=0,pady=10,padx=10,ipady=5,ipadx=5)
		mail_button_label = Label(self.frame, textvariable=self.fmail,width=50,bg="white",borderwidth=2, relief="groove",anchor=W)
		mail_button_label.grid(row=3,column=1,pady=10,padx=10,ipady=5,ipadx=5)

		attachment_button = Button(self.frame, text='Select attachment file', command=self.get_attachment_file,width=25)
		attachment_button.grid(row=4,column=0,pady=10,padx=10,ipady=5,ipadx=5)
		attachment_button_label = Label(self.frame, textvariable=self.fattachment,width=50,bg="white",borderwidth=2, relief="groove",anchor=W)
		attachment_button_label.grid(row=4,column=1,pady=10,padx=10,ipady=5,ipadx=5)

		attachment_name_label = Label(self.frame,text="Attachment name (if blank, we'll\nuse the real attachment name)",bg="beige",anchor=W)
		attachment_name_label.grid(row=5,column=0,pady=10,padx=10,ipady=5,ipadx=5)
		attachment_name_entry = Entry(self.frame,text=self.attachment_name,bg="white",width=50)
		attachment_name_entry.grid(row=5,column=1,pady=10,padx=10,ipady=5,ipadx=5)
	
		send_button = Button(self.frame, text="Send mails!",command=self.send_mails).grid(row=6,column=0,pady=10,padx=10,ipady=5,ipadx=5)
		#send_button.place(x=10,y=180,width=147,height=40)
			
		exit_button = Button(self.frame, text="Exit",command=self.main.destroy)
		exit_button.grid(row=6,column=1,pady=10,padx=10,ipady=5,ipadx=5)
		

	def create_new(self):
		"""
		Creates a new session
		
		"""
		self.main.destroy()
		gui = GUI()
		gui.main.mainloop()

	def finish(self):
		self.main.destroy()

	def save(self):
		file = filedialog.asksaveasfile(title="Save File",mode='wb', defaultextension=".stf")
		if(file != None):
			dump = dumpObject(self.ftarget,self.fmail,self.fattachment,self.smtp_server,self.smtp_port,
							self.smtp_user,self.smtp_password,self.sent_from,self.subject,self.attachment_name)
			pickle.dump(dump, file, pickle.HIGHEST_PROTOCOL)
			file.close()
			messagebox.showinfo("Saved", "Data saved correctly")


	def open(self):
		file = filedialog.askopenfile(filetypes =((("STF files", "*.stf"),
											("All files", "*.*") )), title="Choose a file",mode="rb")
		if(file != None):
			try:
				dump = pickle.load(file)
				self.ftarget.set(dump.ftarget)
				self.fmail.set(dump.fmail)
				self.fattachment.set(dump.fattachment)
				self.smtp_server.set(dump.smtp_server)
				self.smtp_port.set(dump.smtp_port)
				self.smtp_user.set(dump.smtp_user)
				self.smtp_password.set(dump.smtp_password)
				self.sent_from.set(dump.sent_from)
				self.subject.set(dump.subject)
				self.attachment_name.set(dump.attachment_name)
				messagebox.showinfo("Open File", "Data loaded correctly")
			except:
				messagebox.showerror("ERROR", "Error opening file. Check if it's corrupted or blank")
			file.close()

	def configuration_frame(self):
		"""
		Creates the configuration frame
		
		"""
		self.frame.destroy()
		self.frame = Frame(self.main,width=700, height=500)
		self.frame.configure(bg='beige')
		self.frame.pack()

		smtp_server_label = Label(self.frame,text="SMTP Server",bg="beige")
		smtp_server_label.grid(row=0,column=0,pady=10,padx=10,ipady=5,ipadx=5)
		smtp_server_entry = Entry(self.frame, textvariable=self.smtp_server,bg="white")
		smtp_server_entry.grid(row=0,column=1,pady=10,padx=10,ipady=5,ipadx=5)
		
		smtp_port_label = Label(self.frame,text="SMTP Port",bg="beige")
		smtp_port_label.grid(row=1,column=0,pady=10,padx=10,ipady=5,ipadx=5)
		smtp_port_entry = Entry(self.frame,text=self.smtp_port,bg="white")
		smtp_port_entry.grid(row=1,column=1,pady=10,padx=10,ipady=5,ipadx=5)


		smtp_user_label = Label(self.frame,text="SMTP User",bg="beige")
		smtp_user_label.grid(row=2,column=0,pady=10,padx=10,ipady=5,ipadx=5)
		smtp_user_entry = Entry(self.frame,text=self.smtp_user,bg="white")
		smtp_user_entry.grid(row=2,column=1,pady=10,padx=10,ipady=5,ipadx=5)


		smtp_password_label = Label(self.frame,text="SMTP Password",bg="beige")
		smtp_password_label.grid(row=3,column=0,pady=10,padx=10,ipady=5,ipadx=5)
		smtp_password_entry = Entry(self.frame,show="*",text=self.smtp_password,bg="white")
		smtp_password_entry.grid(row=3,column=1,pady=10,padx=10,ipady=5,ipadx=5)


		back_button = Button(self.frame, text='Back and save', command=self.main_frame)
		back_button.grid(row=5,columnspan=2,pady=10,padx=10,ipady=5,ipadx=5)

	def help(self):
		help_window = Tk()
		help_window.geometry("650x300")
		help_window.resizable(width=False,height=False)
		help_window.configure(bg="beige")
		help_window.title("Help")

		scroll = Scrollbar(help_window)
		text = Text(help_window,bg="beige")
		scroll.pack(side=RIGHT, fill=Y)
		text.pack(side=LEFT, fill=Y)
		scroll.config(command=text.yview)
		text.config(yscrollcommand=scroll.set)
		str_text = "This tool can help you to check if your employees are succesfully aware about phishing attacks.\n"
		str_text+= "You can configure your STMP configuration at settings menu and your email configuration at the main page.\n"
		str_text += "Author: Adrian Navas <adrian dot navas dot ajenjo1@gmail dot com>"
		text.insert(END, str_text)
		text.configure(state=DISABLED)

	def get_target_file(self):
		"""
		Target filename set up
		
		"""
		file = filedialog.askopenfile(title="Choose a target file.")
		if(file != None):
			self.ftarget.set(file.name)

	def get_mail_file(self):
		"""
		Mail filename set up
		
		"""
		file = filedialog.askopenfile(filetypes =((("HTML files", "*.html"),
											("All files", "*.*") )), title = "Choose a HTML template mail file.")
		if(file != None):
			self.fmail.set(file.name)

	def get_attachment_file(self):
		"""
		Mail filename set up
		
		"""
		file = filedialog.askopenfile(title = "Choose an attachment file.")
		if(file != None):
			self.fattachment.set(file.name)

	def send_mails(self):
		"""
		If all needed params are completed, call to staff_tester module to send mails
		TODO: check all params introduced by user manually
		
		"""
		if(self.ftarget.get() == ""):
			messagebox.showerror("ERROR", "You must select target file name")
		elif(self.fmail.get() == ""):
			messagebox.showerror("ERROR", "You must select mail template file name")
		else:
			try:
				staff_tester.init(self)
			except Exception as e:
				messagebox.showerror("ERROR", e)

class dumpObject():
	def __init__(self,ftarget,fmail,fattachment,smtp_server,smtp_port,smtp_user,smtp_password,sent_from,subject,attachment_name):
		self.ftarget = ftarget.get()
		self.fmail = fmail.get()
		self.fattachment = fattachment.get()

		self.smtp_server = smtp_server.get()
		self.smtp_port = smtp_port.get()
		self.smtp_user = smtp_user.get()
		self.smtp_password = smtp_password.get()
		self.sent_from = sent_from.get()
		self.subject = subject.get()
		self.attachment_name = attachment_name.get()


if __name__ == '__main__':
	gui = GUI()
	gui.main.mainloop()