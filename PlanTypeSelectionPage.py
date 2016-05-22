from selenium import webdriver
from selenium.webdriver.common.by import By

from Base_Page_Object2 import Page #generic Page Object
import const #those are constants like plan type & name used by more then one module
 
class PlanTypeSelectionPage(Page):
    #local constants
    STARTER_PLAN_BTN_CSS='div[rel="Starter 2014"]'
    PROFESSIONAL_PLAN_BTN_CSS='div[rel="Professional 2014"]'
    ENTERPRISE_PLAN_BTN_CSS='div[rel="Enterprise 2014"]'
    
    MONTHLY_BTN_ID='period1'
    ANNUALLY_BTN_ID='period2'
    EVERY_TWO_YEARS_BTN_ID='period3'
    
    TOTAL_SUM_CSS='span[class="current-sum"]'
    
    #Locators

    StarterPlanBtn_loc = (By.CSS_SELECTOR, STARTER_PLAN_BTN_CSS)
    ProfessionalPlanBtn_loc = (By.CSS_SELECTOR, PROFESSIONAL_PLAN_BTN_CSS)
    EnterprisePlanBtn_loc = (By.CSS_SELECTOR, ENTERPRISE_PLAN_BTN_CSS)
    
    MonthlyBtn_loc = (By.ID, MONTHLY_BTN_ID)
    AnnuallyBtn_loc = (By.ID, ANNUALLY_BTN_ID)
    EveryTwoYearsBtn_loc = (By.ID, EVERY_TWO_YEARS_BTN_ID)
    
    TotalSum_loc = (By.CSS_SELECTOR, TOTAL_SUM_CSS)
    
    def __init__(self,driver=None):
        self.driver = driver
    
    # Actions
 
    def get_Title(self):
        """Returns the page title"""        
        return self.driver.title
        
    def ChoosePlanType(self,PlanType):
        if PlanType == const.STARTER_PLAN_TYPE:     
            self.find_element(*self.StarterPlanBtn_loc).click() 
        elif PlanType == const.ANNUAL_PLAN_TYPE:     
            self.find_element(*self.ProfesionalPlanBtn_loc).click()
        elif PlanType == const.ENTERPRISE_PLAN_TYPE:     
            self.find_element(*self.EnterprisePlanBtn_loc).click()
 
    def ChoosePlanTimePeriod(self,PlanTimePeriod):
        if PlanTimePeriod == const.MONTHLY_PLAN_TIME_PERIOD:     
            self.find_element(*self.MonthlyBtn_loc).click() 
        elif PlanTimePeriod == const.ANNUALY_PLAN_TIME_PERIOD:     
            self.find_element(*self.AnnuallyPlanBtn_loc).click()
        elif PlanTimePeriod == const.EVERY_TWO_YEARS_PLAN_TIME_PERIOD:     
            self.find_element(*self.EveryTwoYearsBtn_loc).click()
        
    def TotalSum(self):
        return self.find_element(*self.TotalSum_loc).text