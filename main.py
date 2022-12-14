from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from secrets import pw


class Instabot: 
    def __init__(self, username, pw):
        self.username = username
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")
        sleep(2)

        # Digita Login
        self.driver.find_element(By.XPATH,'//input[@name=\"username\"]')\
            .send_keys(username)
        # Digita Senha
        self.driver.find_element(By.XPATH,'//input[@name=\"password\"]')\
            .send_keys(pw)
        # Clica login
        self.driver.find_element(By.XPATH,'//button[@type="submit"]')\
            .click()
        
        sleep(4)
        self.driver.find_element(By.XPATH,"//button[contains(text(), 'Agora não')]")\
            .click()

        sleep(2)
        self.driver.find_element(By.XPATH,"//button[contains(text(), 'Agora não')]")\
            .click()
        sleep(2)

    def get_unfollowers(self):
        id_following = 3
        id_followers = 2
        self.driver.find_element(By.XPATH,"//a[contains(@href, '/{}/')]".format(self.username))\
            .click()
        sleep(2)
        self.driver.find_element(By.XPATH,"//a[contains(@href, '/{}/following')]".format(self.username))\
            .click()
        following = self._get_names(id_following)
        self.driver.find_element(By.XPATH,"//a[contains(@href, '/{}/followers')]".format(self.username))\
            .click()
        followers = self._get_names(id_followers)
        not_following_back = [user for user in following if user not in followers]

        for name in not_following_back:
            print(name)

    def _get_names(self,id):
        sleep(5)
        scroll_box = self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[{}]".format(id))
        last_ht, ht = 0 , 1

        while last_ht != ht:
            last_ht= ht
            sleep(1)
            ht  = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight
            """, scroll_box)
        links = scroll_box.find_elements(By.TAG_NAME,'a')
        names = [name.text for name in links if name != '']

        #Close Button
        self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/button")\
            .click()
        return names

        

meuBot = Instabot('username', pw)
meuBot.get_unfollowers()
