import urllib2
import json
def send(config):
	try:
		data = {
				'outboundSMSMessageRequest': {
				'address':['tel:+'+config['number']],
				'senderAddress':'tel:+'+config['user'],
				'outboundSMSTextMessage': {
				    'message':config['message']
					}
				}
			}
		req = urllib2.Request('https://api.swisscom.com/v1/messaging/sms/outbound/tel%3A%'+config['user']+'/requests')
		req.add_header('Content-Type', 'application/json; charset=utf-8')
		req.add_header('client_id', config['pass'])
		result = urllib2.urlopen(req, json.dumps(data))
		# print '\n'.join(result.readlines())
		# print result["outboundSMSMessageRequest"]["deliveryInfoList"]["deliveryInfo"][0]["deliveryStatus"] is "DeliveredToNetwork"
		return True
	except:
		return False
