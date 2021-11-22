from time import sleep
from locators import *

class User():

    def __init__(self, username, driver):
        self.username = username
        self.driver = driver
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

        is_private = self.isprivate()

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
        ls = []
        li_list = self.driver.find_elements(*UserLocators.li_follow_cls)

        sleep(2)
        while len(li_list) < count:
            self.driver.execute_script('''
                let a = document.getElementsByClassName(arguments[0]);
                a[0].scrollTo(0, a[0].scrollHeight);
                a[0].scrollTop = a[0].scrollHeight;
                ''', UserLocators.div_cls)
            sleep(3)
            li_list = self.driver.find_elements(*UserLocators.li_follow_cls)

        for elem in li_list:
            a = elem.text.split('\n')
            # this return a list of [<username>, ?verfied, <name>, 'Follow']
            # this return a list of [<username>, ?'.', ?'Follow', <name>, '?Remove:Follow'] for bot

            if len(a) == 5:
                del a[1:3]
                ls.append(a[:2])
            elif len(a)==4:
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
