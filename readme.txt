=== SMS ===
Contributors: birdy1976
Tags: cellular, cli, message, phone, python, selenium, sms, terminal, webdriver
Stable tag: 0.2

== Description ==

Send SMS (Short Message Service) messages from the command line interface (CLI)

== Installation ==

For Linux users:
1. Open a terminal (e.g. ctrl+alt+t)
2. sudo apt-get install python-pip
3. sudo pip install selenium
4. To install SMS do a) or b)
a) git clone git@github.com:birdy1976/sms.git
b) Unzip: https://github.com/birdy1976/t2w/zipball/master
5. Copy mod/conf/sample.py and create your profile, e.g. myconf.py
6. Add an alias to ~/.bashrc: alias sms='python /path/to/sms.py'
7. Send your first SMS: sms myconf 0041761234567 'Hello world :)'

== Frequently Asked Questions ==

= My provider is missing =

1. Open the Firefox browser
2. Install IDE: http://seleniumhq.org/download/
3. Open "Extras > Selenium IDE > Options > Options"
4. Tick check box "Enable experimental features"
5. "Record" sending of an SMS with your provider
6. Terminal (useful): sudo apt-get install ipython
7. Develop and contribute your provider ;-)

== Screenshots ==

1. Help message
2. Message to one addressee
3. Message to several addressees

== Changelog ==

= 0.2 =
added: mod/site/ch/ecall.py
modified: mod/site/ch/coopmobile.py
modified: readme.txt
modified: sms.py

= 0.1 =
* Initial release: Here we go :)
