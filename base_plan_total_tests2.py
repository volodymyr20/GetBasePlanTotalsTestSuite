##########################################################################################
#Background: getbase.com provides different plan types and time periods combinations to choose from, depending on that total sum will be calculated.

#This is a test suite to check that the total sum is calculated correctly for different plan type & time period combinations.

#Pre-requisites:
#1) a user registered at getbase.com with the trial period expired

#Disclaimer: This is rather an educational sample than a real life example, not a complete suite neither. Its purpose it to illustrate how Selenium+Python 
#can be used for test automation of web sites, and also use of Page Object design pattern which makes maintenance a lot easier. 

##########################################################################################

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

#test suite specific modules
import const
import PricingHomePage
import LoginPage
import PlanTypeSelectionPage

class WebDriverTestCase(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Firefox()
    self.driver.implicitly_wait(20)
  def tearDown(self):
    self.driver.quit()

class MyTests(WebDriverTestCase):

  def testPlanTotals(self):
    #local constants 
    HOME_PAGE_TITLE="Plans and Pricing | Base CRM"
    LOGIN_PAGE_TITLE="Login to Base"
    PLAN_SELECTION_PAGE_TITLE="Base CRM"
  
    STARTER_MONTHLY_TOTAL_SUM="25"
    #...
	#the rest of totals should be added for other test cases
  
    # pre-requisites for all test cases: 1) open pricing home page 2) log in
    pricing_home_page = PricingHomePage.PricingHomePage(self.driver)
    pricing_home_page.openpage()
    self.assertIn(HOME_PAGE_TITLE, pricing_home_page.get_Title())
    pricing_home_page.goto_LogIn()  

    login_page = LoginPage.LoginPage(self.driver)
    self.assertIn(LOGIN_PAGE_TITLE, login_page.get_Title())
    login_page.LogIn()  
    
    #test case #1: checking Starter + Monthly combination total sum
    plan_type_selection_page = PlanTypeSelectionPage.PlanTypeSelectionPage(self.driver)
    self.assertIn(PLAN_SELECTION_PAGE_TITLE, plan_type_selection_page.get_Title())
    plan_type_selection_page.ChoosePlanType(const.STARTER_PLAN_TYPE) 
    plan_type_selection_page.ChoosePlanTimePeriod(const.MONTHLY_PLAN_TIME_PERIOD) 
    self.assertIn(STARTER_MONTHLY_TOTAL_SUM, plan_type_selection_page.TotalSum())
    
    #test case post action: go back to the plan type selection form
    self.driver.back();
    self.driver.forward();
	
	#test case #2: checking Starter + Annually combination total sum, the same pattern as above, just different values
	#...
	#test case #9: checking Enterprise + Every Two Years combination total sum   

if __name__ == '__main__':
    unittest.main()
