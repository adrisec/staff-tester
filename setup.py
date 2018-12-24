from distutils.core import setup

setup(name="Staff Tester",
	version = "0.1.0",
	author="Adrian Navas",
	author_email='adrian.navas.ajenjo1@gmail.com',
	url="http://github.com/adrinavaas/staff-tester",
	download_url = "https://github.com/adrinavaas/staff-tester/archive/master.zip",
	keywords = ['staff-tester', 'social-engineering'],
	license = 'GPLv3',
	long_description="""Phishing testing tool written in Python to test people awareness about phishing attacks""",
	packages=['staff-tester'],
	classifiers=[],
	install_requires=[
		"tkinter",
		"pickle",
		"smtplib",
		"re",
		"email",
		"os",
	],
)
