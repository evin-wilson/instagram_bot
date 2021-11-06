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
		except: print('No saveinfo')
		try: 
			notification = WebDriverWait(self.driver, 2).until(
			    EC.element_to_be_clickable(MainPageLocators.notification_turn_off), 'cannot find turn-off info popup'
				).click()
		except :print('No notification')
	
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
			self.driver.find_element(*UserLocators.isprivate)
			return True

		except NoSuchElementException:
			return False

	def info(self): 
		# -------------returns a dict about the user------------- #
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

	def __getlist(self, count):
		ls = []
		li_list = self.driver.find_elements(*UserLocators.li_follow_cls)

		while len(li_list) < count:
			self.driver.execute_script('''
				let a = document.getElementsByClassName(arguments[0]);
				a[0].scrollTo(0, a[0].scrollHeight);
				a[0].scrollTop = a[0].scrollHeight;
				''', UserLocators.div_cls)
			sleep(3)
			li_list = self.driver.find_elements(*UserLocators.li_follow_cls)

		for elem in li_list:
			# name = elem.find_element_by_class_name('wFPL8 ').text
			# username = elem.find_element_by_class_name('FPmhX').text

			a = elem.text.split('\n')
			# this return a list of [<username>, ?verfied, <name>, 'Follow']

			if len(a)==4:
				# swaping the verifed and name field
				a[2], a[1] = a[1], a[2]
				ls.append(a[:3])
			elif len(a)==3:
				ls.append(a[:2])
			else:
				a[1] = None
				ls.append(a)

		return ls

	def followers_list(self, count=10):
		# Returns a list of list of username, name, ?verified of the followers
		self.driver.find_element_by_partial_link_text("follower").click() 
		return self.__getlist(count)
	
	def following_list(self, count=12):
		# Returns a list of list of username,name, ?verified of the followings
		self.driver.find_element_by_partial_link_text("following").click() 

		return self.__getlist(count)
		
	def chat(self):
		pass

	def like(self):
		pass
	
