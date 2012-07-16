from selenium import webdriver
from time import sleep

def login(config):
	# open browser
	config['driver'] = webdriver.Firefox()
	# open webpage
	config['driver'].get("http://coop.nth.ch/index/login/lang/de")
	# login to web service
	config['driver'].find_element_by_id("email").clear()
	config['driver'].find_element_by_id("email").send_keys(config['user'])
	config['driver'].find_element_by_id("pwd").clear()
	config['driver'].find_element_by_id("pwd").send_keys(config['pass'])
	config['driver'].find_element_by_css_selector("button.login_submit").click()
	return config

def send(config):
	try:
		sleep(1)
		config['driver'].find_element_by_xpath("(//textarea[@name='sms_text'])").clear()
		config['driver'].find_element_by_xpath("(//textarea[@name='sms_text'])").send_keys(config['message'])
		config['driver'].find_element_by_xpath("(//input[@name='sendto[]'])[2]").clear()
		config['driver'].find_element_by_xpath("(//input[@name='sendto[]'])[2]").send_keys(config['number'])
		config['driver'].find_elements_by_class_name("rounded_button")[0].click()
		sleep(1)
		return True
	except:
		return False
