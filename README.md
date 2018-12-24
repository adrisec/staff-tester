# What's staff-tester project?
It's an open source social engineering tool to test employees knowledge about email-based phishing attacks.  

You can create your own HTML templates to send to your employees (or your company employees if you are the information security manager) and know which ones are succesfully aware about this type of attacks and which ones may need more information about. You can cheat them with a phishing email created by yourself and not by any real criminal.  

The basic use of it is, using an SMTP server, sending massively one email (using an HTML template to create it) to a list of target emails and then see which ones belives in the fake attack and which ones report it.


## Supported platforms
* Linux
* !! Not working in Windows - Need to check charset codec errors
* Not tested in MAC OS X

# Installation

### Windows
You need to have installed [Python 3.0 or higher](https://www.python.org/ftp/python/3.7.1/Python-3.7.1.tar.xz) or higher and [git](https://code.google.com/p/msysgit/downloads/list)

Run this commands:
```bash
	C:\User>git clone https://github.com/adrinavaas/staff-tester.git
	C:\User>cd staff-tester
	C:\User>python3 gui.py
```

### Ubuntu/Debian
You need to have installed Python 3.0 or higher and git


Run this commands to install all requirements:
```bash
	$ apt-get install git
	$ apt-get install python3
```
Once installed, to run the GUI run this commands:
```bash
	$ git clone https://github.com/adrinavaas/staff-tester.git
	$ cd staff-tester
	$ ./python3 gui.py
```

# Configuration parameters

To configure the target list add all the target emails (one per line)    
You can use # to add one-line comment  

## How to create the email template?
To create a new template, use HTML format. You have one example template in templates directory.
To manage email design, use html tags.  
To add images, add them directly from internet (otherwise they are not going to be shown at the received email).  
If you want to add any attachment to simulate an attack by an infected file, you can also change the name shown in the attachment in the main panel.  

### Customizing emails
To create a customized email, you can use the customizing feature. You can create customized emails for each target in the list by adding specific parameters as name or surname or any link (maybe to a PHP file hosted to know which ones has clicked on it?)  

You can specify on the HTML template parameters by introducing them between brackets as at this example:
```html
	<html>
  		<head></head>
  		<body>
    			<p>Hello [name]<br>
       			Here is the <a href="[link]">payement</a> you wanted.
    			</p>
  		</body>
	</html>
```

If you add customized parameters, you must add them in your target list by adding them in each line using this syntax:
<mail> <parameter1_name>=<parameter2_value> <parameter2_name>=<parameter2_value> ...  
You can follow this example (using the parameters used in the previous example)
```text
	#Example target list file
	mail@example.com name=George link=http://mailtophpfile.com?id=1
	mail2@example.com name=Jane link=http://mailtophpfile.com?id=2
	mail3@example.com name=Jacques link=http://mailtophpfile.com?id=3
	mail4@example.com name=Jane link=http://mailtophpfile.com?id=4
```
Also if you add parameters, you must do it to every target added in your target list file.


## SMTP Server
If you don't know how to use a SMTP server, you can try this tool by using the free Gmail SMTP server ([check more info here](https://www.lifewire.com/what-are-the-gmail-smtp-settings-1170854))   
If you have a corporative email, you can may use your own SMTP server. If you don't know how to do it, ask your hosting provider.   
Otherwise, you can use any other SMTP services. A simple Google search can help you with this configuration.    
### Connection reminders
Staff-tester uses a TLS connection to the server. In the case that you have different alternatives(for example gmail SMTP uses different ports for TLS or SSL), you may need consider it.   


# Disclaimer
This tool is only for testing or learning purposes and it can only be used where strict consent has been given. Do not use this for any illegal purposes.   
Use this tool by your own responsability.

# Contributors
Adrian Navas <adrian dot navas dot ajenjo1@gmail dot com> (http://github.com/adrinavaas)

#### Special thanks
Icon made by Freepik from www.flaticon.com