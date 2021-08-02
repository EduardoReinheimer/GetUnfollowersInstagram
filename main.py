from selenium import webdriver
from time import sleep
from secrets import pw


class Instabot: 
    def __init__(self, username, pw):
        self.username = username
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")
        sleep(2)

        # Digita Login
        self.driver.find_element_by_xpath('//input[@name=\"username\"]')\
            .send_keys(username)
        # Digita Senha
        self.driver.find_element_by_xpath('//input[@name=\"password\"]')\
            .send_keys(pw)
        # Clica login
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()

        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()

        sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        sleep(2)

    def get_unfollowers(self):
        self.driver.find_element_by_xpath("//a[contains(@href, '/{}/')]".format(self.username))\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href, '/following')]")\
            .click()
        following = self._get_names()
        self.driver.find_element_by_xpath("//a[contains(@href, '/followers')]")\
            .click()
        followers = self._get_names()
        not_following_back = [user for user in following if user not in followers]
        print(not_following_back)

    def _get_names(self):
        sleep(5)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[3]")
        last_ht, ht = 0 , 1

        while last_ht != ht:
            last_ht= ht
            sleep(1)
            ht  = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight
            """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name != '']

        #Close Button
        self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button")\
            .click()
        return names

        

meuBot = Instabot('eduardo_reinheimer', pw)
meuBot.get_unfollowers()