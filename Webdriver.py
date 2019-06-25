from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.chrome.options import Options

'''
In order to use this, you will have to download the following...
sudo -H pip3 install -U selenium
sudo -H pip3 install urllib3
sudo easy_install selenium
'''

usernameStr = 'INPUT YOUR USERNAME HERE'
passwordStr = 'YOUR PASSWORD'

options = Options()
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
print("\n ==================[Opening Webpage...]=================== \n")
browser = webdriver.Chrome(chrome_options=options)

def getPage():

    browser.get("INPUT YOUR BROWSER HERE")
    username = browser.find_element_by_id('INPUT YOUR USERNAME HERE')
    password = browser.find_element_by_id('YOUR PASSWORD')
    ## USERNAME INFORMATION
    username.send_keys(usernameStr)
    password.send_keys(passwordStr)

    ## SENDING INFORMATION AND PROCEEDING TO THE NEXT PAGE
    submit_button = browser.find_elements_by_xpath('FIND XPATH OF ELEM')[0]
    submit_button.click()
    # time.sleep(2)
    # sub_button = browser.find_elements_by_xpath('//*[@id="auth_methods"]/fieldset[1]/div[1]/button')[0]
    # print(type(sub_button))
    # submit_button.click()

if __name__ == '__main__':
    print(" =========================================================")
    getPage()
