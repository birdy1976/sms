=== SMS ===
Contributors: birdy1976
Tags: cellular, cli, message, phone, python, sms, terminal
Stable tag: 0.2

== Description ==

Send SMS (Short Message Service) messages from the command line interface (CLI)

== Installation ==

For Linux users:
1. Open a terminal (e.g. ctrl+alt+t)
2. Register at https://api-developer.swisscom.com/
3. „Add New API“ to configure SMS later in step 5
4. To install SMS do a) or b)
a) git clone git@github.com:birdy1976/sms.git
b) Unzip: https://github.com/birdy1976/t2w/zipball/master
5. Copy mod/conf/sample.py and create your profile, e.g. myconf.py
6. Add an alias to ~/.bashrc: alias sms='python /path/to/sms.py'
7. Send your first SMS: sms myconf 41761234567 'Hello world :)'

== Screenshots ==

1. Help message
2. Message to one addressee
3. Message to several addressees
