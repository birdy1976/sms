import sys

if len(sys.argv) != 4:
	print "NAME"
	print "       sms - send sms messages from the command line"
	print "SYNOPSIS"
	print "       python /path/to/sms.py PROFILE ADDRESSEE MESSAGE"
	print "DESCRIPTION"
	print "       Send from PROFILE for ADDRESSEE a MESSAGE"
	print "PROFILE:"
	print "       Create your profile(s) in the subfolder mod/conf"
	print "ADDRESSEE:"
	print "       A single number or a list of numbers in a file, e.g."
	print "              41761234567"
	print "              41771234567"
	print "              41781234567"
	print "MESSAGE:"
	print "       The message you want to send, e.g."
	print "              'Hello world :)'"
	print "LINUX USERS:"
	print "       Add an alias to ~/.bashrc: alias sms='python /path/to/sms.py'"
	print "              http://en.wikipedia.org/wiki/Alias_%28command%29"
else:
	# execute command
	profile = sys.argv[1]
	exec "from mod.conf.%s import *" %profile
	config = conf()
	exec "from mod.site.%s import *" %config['site']
	# get addressee(s)
	addressee = sys.argv[2]
	if addressee.isdigit():
		numbers = addressee,
	else:
		f = open(addressee)
		# http://stackoverflow.com/questions/3277503/python-read-file-line-by-line-into-array
		numbers = [line.strip() for line in f]
		f.close()
	# get message
	config['message'] = sys.argv[3]
	# send sms
	for i in range(len(numbers)):
		# replace spaces from number
		number = numbers[i].replace(' ', '')
		if number.isdigit():
			config['number'] = number
			if send(config):
				print number + ": SMS was sent :)"
			else:
				print number + ": SMS wasn't sent :("
		else:
			print number + ": malformed phone number :("
