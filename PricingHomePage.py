from selenium import webdriver
from selenium.webdriver.common.by import By
from Base_Page_Object2 import Page
 
class PricingHomePage(Page):
    #local constants
    url=''
    LogInLink_text='Log In'
    getBaseURL='https://getbase.com/'
    pricingSuffix='pricing/'
    
    #Locators
    LogInLink_loc = (By.LINK_TEXT, LogInLink_text)
    
    def __init__(self, selenium_driver,base_url=getBaseURL):
        Page.__init__(self, selenium_driver,base_url=self.getBaseURL) 
        self.url=self.pricingSuffix
    
    # Actions
    def openpage(self):
        self.open(self.url)
 
    def get_Title(self):
        """Returns the page title"""        
        return self.driver.title
    def goto_LogIn(self):
        self.find_element(*self.LogInLink_loc).click()
 
