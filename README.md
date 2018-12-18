# What's staff-tester project?
It's an open source social engineering tool to test employees knowledge about email-based phishing attacks.

You can create your own HTML templates to send to your employees (or your company employees if you are the information security manager) and know wich ones are succesfully aware about this type of attacks and wich ones maybe need more information about by cheating them with a phishing email created by yourself and not by any real criminal.

The basic usage is to, using an SMTP server, send massively one email (using an HTML template to create it) to a list of target emails and then see wich ones trust the fake attack and wich ones report this phishing attack try.

## How to create the email template?
To create a new template, please use HTML format. You have one example template into template directory.
To manage email design, use html tags.
To add images, please add them directly from internet (otherwise they are not going to be shown at the received email).
If you want to add any attachment to simulate an attack by an infected file. You can also change the showing name of the attachment in the main panel.

## Supported platforms
* Linux
* Windows
* Not tested in MAC OS X

# Installation

### Windows
You need to have installed [Python 3.0 or higher](https://www.python.org/ftp/python/3.7.1/Python-3.7.1.tar.xz) or higher and [git](https://code.google.com/p/msysgit/downloads/list)

Run this commands:
```bash
	git clone https://github.com/adrinavaas/staff-tester.git
	cd staff-tester
	./python3 gui.py
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
To configure the target list add all the target mails (one per line)
You can use # to add one-line comment


# Disclaimer
This tool is only for testing or learning purposes and can only be used where strict consent has been given. Do not use this for any illegal purposes.
Use this tool by your own responsability.

# Contributors
Adrian Navas <adrian dot navas dot ajenjo1@gmail dot com> (http://github.com/adrinavaas)

#### Special thanks
Icon made by Freepik from www.flaticon.com 
