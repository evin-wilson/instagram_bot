from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from time import sleep
from locators import *

class instagram(object):
	"""docstring for instagram"""

	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.driver = webdriver.Chrome(executable_path = "C:\\webdriver\\chromedriver.exe")
		self.driver.get("http://www.instagram.com")

		try:
		    username = WebDriverWait(self.driver, 10).until(
		        EC.presence_of_element_located(MainPageLocators.username)
		    	).send_keys(self.username)

		    password = WebDriverWait(self.driver, 10).until(
		        EC.presence_of_element_located(MainPageLocators.password)
		    	).send_keys(self.password)

		    login_elm = self.driver.find_element(*MainPageLocators.login).click()  #unpacking the tuple using '*'
		
		except Exception as e:
			print('Exception is: ',e)
			self.driver.quit()

		self.popup_dismiss()

	def popup_dismiss(self):
		#----------Turn off the notifications when opening the instagram----------
		try:
			saveinfo = WebDriverWait(self.driver, 5).until(
			    EC.element_to_be_clickable(MainPageLocators.not_now), 'cannot find save info popup'
				).click()
			notification = WebDriverWait(self.driver, 2).until(
			    EC.element_to_be_clickable(MainPageLocators.notification_turn_off), 'cannot find turn-off info popup'
				).click()
		except :pass
	
	def die(self):
		# close the browser
		print('Bot is dead')
		self.driver.quit()


class User(instagram):

	def __init__(self, username, bot):
		self.username = username
		self.driver = bot.driver
		self.driver.get( f'http://www.instagram.com/{self.username}/')

	def isprivate(self):
		try:
			self.driver.find_element_by_class_name(UserLocators.isprivate)
			return True

		except NoSuchElementException:
			return False

	def info(self): 
		# -------------returns  details about the user------------- #
		try: name = self.driver.find_element(*UserLocators.name).text
		except : name = None

		details = self.driver.find_elements(*UserLocators.ul_of_noPost_folower_folowi)

		no_of_post = details[0].text
		followers_count = details[1].get_attribute('title')
		following_count= details[2].text

		info = dict({'username': self.username,
					 'name':name, 
					 'no_of_post': no_of_post,
					 'followers_count':followers_count,
					 'following_count':following_count})

		return info

	def followers_list(self):
		# ------------make a file listing the followers of the user------------
		self.driver.find_element(*UserLocators.followers).click()  

		while True:
			self.driver.execute_script("let a = document.getElementsByClassName('isgrP');\
										a[0].scrollTo(0, document.body.scrollHeight)")
			sleep(3)
	
	def following_list(self):
		# make a file listing followings of the user
		pass
		
	def chat(self):
		pass

	def like(self):
		pass
	
