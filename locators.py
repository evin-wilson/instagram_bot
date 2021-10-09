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
	username = (By.TAG_NAME, 'h1')
	no_of_post = (By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[1]/span/span')

	followers_count = (By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span')
	
	followers = (By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
	
	following_count = (By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span')
	following = (By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')

	# the dialogue box which popup when followers is clicked
	followers_dialogue_box = (By.XPATH, "/html/body/div[5]")
	first_follower = (By.XPATH, "/html/body/div[6]/div/div/div[2]/ul")
	                           # /html/body/div[4]/div/div/div[2]/ul/div/li[1]
	                           # /html/body/div[6]/div/div/div[2]/ul



class Message(object):
	pass
	
		


