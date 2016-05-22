#This is the main test suite, please refer to README.md for more details

from selenium import webdriver
import unittest

#test suite specific modules
import const #those are constants like plan type & name used by more then one module
import PricingHomePage # this is the Page Object for the very first page (getbase.com/prising)
import LoginPage # the Page Object for the next one with the login form
import PlanTypeSelectionPage # the Page Object for the plan type selection page

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
