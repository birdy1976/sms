from selenium import webdriver
from time import sleep
from urlparse import parse_qs, urlparse

def login(config):
	# open browser
	config['driver'] = webdriver.Firefox()
	# open webpage
	config['driver'].get("http://ecall.ch/sms/ecall-sms-fax.asp")
	# login to web service
	config['driver'].find_element_by_name("AccountName").clear()
	config['driver'].find_element_by_name("AccountName").send_keys(config['user'])
	config['driver'].find_element_by_name("Password").clear()
	config['driver'].find_element_by_name("Password").send_keys(config['pass'])
	config['driver'].find_element_by_name("Anmelden").click()
	sleep(1)
	# get wcu (session)
	url = urlparse(config['driver'].current_url)
	params = parse_qs(url.query)
	config['wcu'] = params['WCU'][0]
	return config

def send(config):
	try:
		config['driver'].get("http://www2.ecall.ch/ecall/ecall.ASP?WCI=Message_Create&WCU=" + config['wcu'])
		sleep(1)
		config['driver'].find_element_by_name("FreeNo").clear()
		config['driver'].find_element_by_name("FreeNo").send_keys(config['number'])
		config['driver'].find_element_by_css_selector("textarea[name=\"Message\"]").clear()
		config['driver'].find_element_by_css_selector("textarea[name=\"Message\"]").send_keys(config['message'])
		config['driver'].find_element_by_xpath("(//input[@name='Senden'])[2]").click()
		sleep(1)
		return True
	except:
		return False
