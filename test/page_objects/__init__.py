class BasePage(object):
    ''' Base page setup with the driver '''
    def __init__(self, driver):
        self.driver = driver