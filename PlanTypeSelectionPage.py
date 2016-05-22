from selenium import webdriver
from selenium.webdriver.common.by import By
from Base_Page_Object2 import Page
 
class PlanTypeSelectionPage(Page):
    #Locators

    StarterPlanBtn_loc = (By.CSS_SELECTOR, 'div[rel="Starter 2014"]')
    ProfessionalPlanBtn_loc = (By.CSS_SELECTOR, 'div[rel="Professional 2014"]')
    EnterprisePlanBtn_loc = (By.CSS_SELECTOR, 'div[rel="Enterprise 2014"]')
    
    MonthlyBtn_loc = (By.ID, 'period1')
    AnnuallyBtn_loc = (By.ID, 'period2')
    EveryTwoYearsBtn_loc = (By.ID, 'period3')
    
    TotalSum_loc = (By.CSS_SELECTOR, 'span[class="current-sum"]')
    
    def __init__(self,driver=None):
        self.driver = driver
    
    # Actions
 
    def get_Title(self):
        """Returns the page title"""        
        return self.driver.title
        
    def ChoosePlanType(self,PlanType):
        if PlanType == 'Starter 2014':     
            self.find_element(*self.StarterPlanBtn_loc).click() 
        elif PlanType == 'Professional 2014':     
            self.find_element(*self.ProfesionalPlanBtn_loc).click()
        elif PlanType == 'Enterprise 2014':     
            self.find_element(*self.EnterprisePlanBtn_loc).click()
 
    def ChoosePlanTimePeriod(self,PlanTimePeriod):
        if PlanTimePeriod == 'Monthly':     
            self.find_element(*self.MonthlyBtn_loc).click() 
        elif PlanTimePeriod == 'Annually':     
            self.find_element(*self.AnnuallyPlanBtn_loc).click()
        elif PlanTimePeriod == 'Every Two Years':     
            self.find_element(*self.EveryTwoYearsBtn_loc).click()
        
    def TotalSum(self):
        return self.find_element(*self.TotalSum_loc).text