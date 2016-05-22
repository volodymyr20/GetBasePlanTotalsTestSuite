from selenium import webdriver
from selenium.webdriver.common.by import By
from Base_Page_Object2 import Page
 
class LoginPage(Page):
    #Locators
    UserEmail_loc = (By.ID, 'user_email')
    UserPassword_loc = (By.ID, 'user_password')
    LogInBtn_loc = (By.ID, 'user_new')
    #LogInBtn_loc = (By.TAG_NAME, 'Log in')

    def __init__(self,driver=None):
        self.driver = driver
    
    # Actions
 
    def get_Title(self):
        """Returns the page title"""        
        return self.driver.title
    def LogIn(self):
        self.find_element(*self.UserEmail_loc).send_keys('volodymyrbekesha@gmail.com')
        self.find_element(*self.UserPassword_loc).send_keys('volo20dymyr')  

        self.find_element(*self.LogInBtn_loc).submit()
 
