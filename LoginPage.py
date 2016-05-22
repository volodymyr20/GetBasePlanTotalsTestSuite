from selenium import webdriver
from selenium.webdriver.common.by import By
from Base_Page_Object2 import Page
 
class LoginPage(Page):
    #local constants
    USER_EMAIL_ID='user_email'
    USER_PASSWORD_ID='user_password'
    LOGIN_BUTTON_ID='user_new'
    
    USER_NAME='volodymyrbekesha@gmail.com'
    USER_PASSWORD='volo20dymyr'
    
    #Locators
    UserEmail_loc = (By.ID, USER_EMAIL_ID)
    UserPassword_loc = (By.ID, USER_PASSWORD_ID)
    LogInBtn_loc = (By.ID, LOGIN_BUTTON_ID)

    def __init__(self,driver=None):
        self.driver = driver
    
    # Actions
 
    def get_Title(self):
        """Returns the page title"""        
        return self.driver.title
    def LogIn(self):
        self.find_element(*self.UserEmail_loc).send_keys(self.USER_NAME)
        self.find_element(*self.UserPassword_loc).send_keys(self.USER_PASSWORD)  

        self.find_element(*self.LogInBtn_loc).submit()
 
