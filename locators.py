from selenium.webdriver.common.by import By

class MainPageLocators(object):
	username = (By.NAME, 'username')
	password = (By.NAME, 'password')
	login = (By.ID, "loginForm")
	
	# Popups locators
	notification_turn_off = (By.XPATH, '/html/body/div[6]/div/div/div/div[3]/button[2]')
	save_login_info_not_now = (By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')

class UserLocators(object):
	# class name of <h2> which display "Sorry, this page isn't available."
	page_is_unavailable = (By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/div/h2')

	# xpath of <span> containing name
	name = (By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/div[2]/span')

	# classname of the <span> containing no of post, followers count, following count
	info = (By.CLASS_NAME, '_ac2a')

	# class name of <h2> which display "This Account is Private"
	isprivate = (By.CLASS_NAME, '_aa_u')

	# class name of <li> of followers and following
	li_follow_cls = (By.CLASS_NAME, '_aaei')

	# close button in the dialoge box of followers and following
	x_btn = (By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[1]/div/div[3]/div/button')

	# used in js script
	# class name of the div containg the list of followers/following
	# used div is immediate parent of the <ul> 
	scroll_list = '_aano'

	scroll_list_loc = (By.CLASS_NAME, scroll_list)

