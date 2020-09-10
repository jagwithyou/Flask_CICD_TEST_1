from selenium.webdriver.common.by import By

class GooglePageLocator(object):
    ''' all the locators of the page '''
    SEARCH_BAR = (By.NAME, "q")     #this line means we want to find a element whose NAME is q
    SUBMIT_BUTTON = (By.ID, "tsf")  #this line means we want to find a element whose ID is tsf
    SEARCH_BAR_FAILED = (By.NAME, "i")     #this line means we want to find a element whose NAME is q
