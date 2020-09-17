
from selenium.webdriver.support.select import Select
from page_objects.google_page import GooglePage
from tests import BaseClass
from selenium import webdriver
import pytest, config
from selenium.common.exceptions import NoSuchElementException

class TestSimplePage1(BaseClass):
    def test_1_dummy1(self):
        ''' This is a dummy test for CICD.'''
        #Instantiating the logger
        log = self.getLogger()
        log.info(" Test Started")
        #logging the test success
        log.info("Test Success")
        assert False 
    
            

