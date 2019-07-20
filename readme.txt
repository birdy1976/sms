=== SMS ===
Contributors: birdy1976
Tags: cellular, cli, message, phone, python, sms, terminal
Stable tag: 0.2

== Description ==

Send SMS (Short Message Service) messages from the command line interface (CLI)

== Installation ==

For Linux users:
1. Register at https://digital.swisscom.com
2. Subscribe to the free „Text Messaging (SMS)“ (100 text messages per month)
3. Open a terminal (e.g. ctrl+alt+t)
4. To install SMS do a) or b)
a) git clone git@github.com:birdy1976/sms.git
b) curl -L https://github.com/birdy1976/sms/tarball/master | tar zx
5. Copy mod/conf/sample.py and create your profile, e.g. myconf.py
6. Add an alias to ~/.bashrc: alias sms='python /path/to/sms.py myconf'
7. Send your first SMS: sms 41761234567 'Hello world :)'

== Screenshots ==

1. Help message
2. Message to one addressee
3. Message to several addressees
