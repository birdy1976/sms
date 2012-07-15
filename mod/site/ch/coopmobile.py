from selenium import webdriver
import getpass, time

def login(config):
	try:
		config['pass']
	except KeyError:
		# enter passwort
		config['pass'] = getpass.getpass()
	# open browser
	driver = webdriver.Firefox()
	# open webpage
	driver.get("http://coop.nth.ch/index/login/lang/de")
	# login to web service
	driver.find_element_by_id("email").clear()
	driver.find_element_by_id("email").send_keys(config['user'])
	driver.find_element_by_id("pwd").clear()
	driver.find_element_by_id("pwd").send_keys(config['pass'])
	driver.find_element_by_css_selector("button.login_submit").click()
	return driver

def send(driver, message, number):
	try:
		time.sleep(1)
		driver.find_element_by_xpath("(//textarea[@name='sms_text'])").clear()
		driver.find_element_by_xpath("(//textarea[@name='sms_text'])").send_keys(message)
		driver.find_element_by_xpath("(//input[@name='sendto[]'])[2]").clear()
		driver.find_element_by_xpath("(//input[@name='sendto[]'])[2]").send_keys(number)
		driver.find_elements_by_class_name("rounded_button")[0].click()
		time.sleep(1)
		return True
	except:
		return False
