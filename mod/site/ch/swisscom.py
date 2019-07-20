import urllib2
import json
def send(config):
	try:
		data = {
		  'from': config['user'],
		  'to':   config['number'],
			'text': config['message']
		}
		req = urllib2.Request('https://api.swisscom.com/messaging/sms')
		req.add_header('client_id', config['pass'])
		req.add_header('Content-Type', 'application/json')
		req.add_header('SCS-Version', 2)
		result = urllib2.urlopen(req, json.dumps(data))
		# print '\n'.join(result.readlines())
		return True
	except:
		return False
