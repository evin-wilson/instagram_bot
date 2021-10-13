from selenium.webdriver.common.by import By

class MainPageLocators(object):
	username = (By.NAME, 'username')
	password = (By.NAME, 'password')
	login = (By.ID, "loginForm")
	
	notification_turn_off = (By.XPATH, '/html/body/div[4]/div/div/div/div[3]/button[2]')
	not_now = (By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')

	search = (By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
	first_one_search_list = (By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div')


class UserLocators(object):
	name = (By.CLASS_NAME, 'rhpdm')
	no_of_post = (By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[1]/span/span')

	ul_of_noPost_folower_folowi = (By.CLASS_NAME, 'g47SY ')

	followers = (By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
	
	following = (By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')

	# class name of h2 tag which display "This Account is Private"
	isprivate = 'rkEop'

	# class name of li of followers
	li_followers = (By.CLASS_NAME, 'wo9IH')
	                         

class Message(object):
	pass
	
		


