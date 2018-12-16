"""
Staff Tester project
Author: Adrian Navas <adrian dot navas dot ajenjo1 @ gmail dot com>
"""

import staff_tester
from tkinter import * 
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox


class GUI():
	"""
	GUI Interface management class
	It uses one window and two frames to navigate (main frame and settings frame)

	TODO: finish navigation bar functionality
	TODO: add an entry option to change attachment name (it helps on mobile devices and maybe on desktop OS to cheat targets)

	"""

	def __init__(self):

		self.main = Tk()
		self.main.geometry("700x400")
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

		menu = Menu(self.main)
		self.main.config(menu=menu)

		mainmenu = Menu(menu)
		menu.add_cascade(label="File", menu=mainmenu)
		mainmenu.add_command(label="New",command=self.create_new)
		mainmenu.add_separator()
		mainmenu.add_command(label="Close",command=self.create_new)

		settingsmenu = Menu(menu)
		menu.add_cascade(label="Configuration", menu=settingsmenu)
		settingsmenu.add_command(label="Settings",command=self.configuration_frame)
		settingsmenu.add_separator()
		settingsmenu.add_command(label="Help",command=self.create_new)
		self.frame = None
		self.main_frame()

	def main_frame(self):
		"""
		Creates the main frame
		
		"""
		if(self.frame != None):
			self.frame.destroy()

		self.frame = Frame(self.main)
		self.frame.configure(bg="beige",width=700,height=400)
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
	
		send_button = Button(self.frame, text="Send mails!",command=self.send_mails).grid(row=5,column=0,pady=10,padx=10,ipady=5,ipadx=5)
		#send_button.place(x=10,y=180,width=147,height=40)
			
		exit_button = Button(self.frame, text="Exit",command=self.main.destroy)
		exit_button.grid(row=5,column=1,pady=10,padx=10,ipady=5,ipadx=5)
		

	def create_new(self):
		"""
		Foo function used by all not implemented navigation bar functions
		
		"""
		self.main.destroy()

	def configuration_frame(self):
		"""
		Creates the configuration frame
		
		"""
		self.frame.destroy()
		self.frame = Frame(self.main,width=700, height=400)
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

if __name__ == '__main__':
	gui = GUI()
	gui.main.mainloop()