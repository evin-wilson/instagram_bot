import time

from exception import IsPrivateError
from exception import UserNotFoundError
from locators import *
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


class User():

    def __init__(self, username, driver):
        self.username = username
        self.driver = driver
        self.driver.get( f'http://www.instagram.com/{self.username}/')
        self.__isvalid()

    def __isvalid(self):
        """check if the given username is valid or not"""
        try:
            self.driver.find_element(*UserLocators.page_is_unavailable)
            raise UserNotFoundError(f'{self.username} not found !!')
        except NoSuchElementException:
            pass

    def __page_is_loading(self):
        while True:
            x = self.driver.execute_script("return document.readyState")
            if x == "complete":
                return True
            else:
                yield False

    def isprivate(self):
        """Return a boolean based on whether the account is private or not"""
        while not self.__page_is_loading():
            continue

        try:
            self.driver.find_element(*UserLocators.isprivate)
            return True
        except (TimeoutException, NoSuchElementException):
            return False

    def info(self): 
        """Return a dict of info about the user"""
        try: 
            name = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(UserLocators.name)
                ).find_element(*UserLocators.name).text
        except NoSuchElementException as e:
            name = None
        except TimeoutException as e:
            print('---Took too long to load---')
            name = None

        is_private = self.isprivate()

        details = self.driver.find_elements(*UserLocators.info)
        no_of_post = details[0].text.replace(',','')
        followers_count = details[1].get_attribute('title').replace(',','')
        following_count= details[2].text.replace(',','')

        info = dict({'username': self.username,
                     'name':name, 
                     'no_of_post': int(no_of_post),
                     'followers_count':int(followers_count),
                     'following_count':int(following_count),
                     'is_private' :is_private
                     })

        return info

    def __getlist(self, count):
        ls = {}
        li_list = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(UserLocators.scroll_list_loc)
            ).find_elements_by_tag_name('li')

        if count==0:
            return None
 
        sleep(2)
        while len(li_list) < count:
            self.driver.execute_script('''
                let pop_up = document.getElementsByClassName(arguments[0]);
                pop_up[0].scrollTo(0, pop_up[0].scrollHeight);
                pop_up[0].scrollTop = pop_up[0].scrollHeight;
                ''', UserLocators.scroll_list)
            sleep(3)
            before = len(li_list)
            li_list = self.driver.find_elements(*UserLocators.li_follow_cls)
            after = len(li_list)
            if before == after :
                break

        for elem in li_list:
            a = elem.text.split('\n')
           
            # this return a list of [<username>, ?verfied, <name>, 'Follow'] for other accounts
            # this return a list of [<username>, ?'.', ?'Follow', <name>, '?Remove:Follow'] for self.user
            username = a[0]

            if len(a) == 5:
                ls[username] = a[3]
            elif len(a)==4:
                # swaping the verifed and name field
                a[2], a[1] = a[1], a[2]
                ls[username] = a[1:3]
            elif len(a)==3:
                ls[username] = a[1]
            else:
                ls[username] = None
        self.driver.find_element(*UserLocators.x_btn).click()
        return ls

    def get_followers_list(self, count='max'):
        """Returns a dict of the followers with key as username and value as [name, ?verified]"""
        if self.isprivate():
            raise IsPrivateError(f'{self.username} is Private...')

        if count=='max':
            count=self.info()['followers_count']

        self.driver.find_element_by_partial_link_text("follower").click() 
        return self.__getlist(count)

    
    def get_following_list(self, count='max'):
        """Returns a dict of the followings with key as username and value as [name, ?verified]"""

        if self.isprivate():
            raise IsPrivateError(f'{self.username} is Private...')

        if count=='max':
            count=self.info()['following_count']

        self.driver.find_element_by_partial_link_text("following").click() 
        return self.__getlist(count)
