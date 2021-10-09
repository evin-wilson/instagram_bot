from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

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


class User(object):

	def __init__(self, userId, bot):
		self.userId = userId
		self.driver = bot.driver
		self.driver.get( f'http://www.instagram.com/{self.userId}/')

	def info(self): 
		# -------------returns  details about the user------------- #
		username = self.driver.find_element(*UserLocators.username).text
		followers_count = self.driver.find_element(*UserLocators.followers_count).get_attribute('title')
		following_count = self.driver.find_element(*UserLocators.following_count).text
		no_of_post = self.driver.find_element(*UserLocators.no_of_post).text

		return (username, no_of_post, followers_count, following_count)

	def followers(self):
		# ------------make a file listing the followers of the user------------
		self.driver.find_element(*UserLocators.followers).click()  

		while True:
			self.driver.execute_script("let a = document.getElementsByClassName('isgrP');\
										a[0].scrollTo(0,document.body.scrollHeight)")
			sleep(3)
	
	def following(self):
		# make a file listing followings of the user
		pass
		
	def chat(self):
		pass

	def like(self):
		pass



	
	
