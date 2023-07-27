import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from base.base_driver import BaseDriver


class ResultSearchFlightsPage(BaseDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    ONE_STEP_TRAVEL = "/html/body/fsr-app/fsr-flights-search-result/fsr-qsf-layout/section/div/flights-list/div/div[1]/filters-wrapper/div[2]/div[3]/esky-filter-multichoice[1]/div[2]/ul/li[2]/label/div/span/span"
    CHEAPEST_TRAVEL_BUTTON = "/html/body/fsr-app/fsr-flights-search-result/fsr-qsf-layout/section/div/flights-list/div/div[2]/div/div/div[4]/flights-sorters/div/ul/li[1]/a"


    def change_filters(self):
        time.sleep(15)
        one_step_travel = self.wait_until_element_is_clickable(By.XPATH, self.ONE_STEP_TRAVEL)
        one_step_travel.click()
        time.sleep(5)
        cheapest_travel = self.wait_until_element_is_clickable(By.XPATH, self.CHEAPEST_TRAVEL_BUTTON)
        cheapest_travel.click()
        time.sleep(5)


    def resultsOnResultPage(self):
        self.change_filters()
