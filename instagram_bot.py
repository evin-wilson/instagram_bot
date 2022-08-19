from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from time import sleep

from locators import *
from user import User


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

		# self._popup_dismiss()


	def _popup_dismiss(self):
		"""Turn off the notifications when opening the instagram"""
		try:
			saveinfo = WebDriverWait(self.driver, 5).until(
			    EC.element_to_be_clickable(MainPageLocators.save_login_info_not_now), 'cannot find save info popup'
				).click()
		except TimeoutException as e: pass
	
		try:
			notification = WebDriverWait(self.driver, 2).until(
			    EC.element_to_be_clickable(MainPageLocators.notification_turn_off), 'cannot find turn-off info popup'
				).click()
		except TimeoutException as e: pass

	def die(self):
		"""close the browser"""
		print('Bot is dead')
		self.driver.quit()
		
	def get_followers_list(self, count=100):
		"""Return a dict of followers of the bot"""
		me = User(self.username, self.driver)
		return me.get_followers_list(count)

	def get_following_list(self):
		"""Return a dict of following of the bot"""
		me = User(self.username, self.driver)
		return me.get_following_list()

	def user(self, username):
		"""Return the User Obj"""
		return User(username, self.driver)
