import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class LaunchPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    COOKIES_BUTTON = "/html/body/div[1]/div/div[4]/div[1]/div[2]/button[4]"
    DEPART_FROM_FIELD = "departureRoundtrip0"
    GOING_TO_FIELD = "arrivalRoundtrip0"
    DATE1_FIELD = "departureDateRoundtrip0"
    DATE2_FIELD = "departureDateRoundtrip1"
    DATE1_ON_CALLENDAR = "/html/body/div[11]/table/tbody/tr[5]/td[1]/a"
    DATE2_ON_CALLENDAR = "/html/body/div[11]/table/tbody/tr[5]/td[7]/a"
    NUMBERS_OF_PASSENGERS_BUTTON = "/html/body/div[2]/div/div[3]/div[2]/div/form/section[2]/div[2]/fieldset[1]/div[1]"
    ADDING_PASSEGNERS_BUTTON = "/html/body/div[23]/div/div[2]/div[1]/div/a[2]"
    CLICK_SEARCH_BUTTON = "/html/body/div[2]/div/div[3]/div[2]/div/form/section[2]/div[2]/fieldset[2]/button"

    def accept_cookies(self):
        cookies_button = self.wait_until_element_is_clickable(By.XPATH, self.COOKIES_BUTTON)
        cookies_button.click()


    def getDepartFromField(self):
        return self.wait_until_element_is_clickable(By.ID, self.DEPART_FROM_FIELD)

    def enterDepartFromLocation(self, departlocation):
        self.getDepartFromField().click()
        self.getDepartFromField().send_keys(departlocation)
        self.getDepartFromField().send_keys(Keys.ENTER)


    def getGoingToLocation(self):
        return self.wait_until_element_is_clickable(By.ID, self.GOING_TO_FIELD)

    def enterGoingToLocation(self, goingtolocation):
        self.getGoingToLocation().click()
        self.getGoingToLocation().send_keys(goingtolocation)
        self.getGoingToLocation().send_keys(Keys.ENTER)



    def enter_Departure_Date(self):
        departure_date1_field = self.wait_until_element_is_clickable(By.ID, self.DATE1_FIELD)
        departure_date1_field.click()
        date1_on_callendar = self.wait_until_element_is_clickable(By.XPATH, self.DATE1_ON_CALLENDAR)
        date1_on_callendar.click()


    def enter_Arrival_Date(self):
        departure_date2_field = self.wait_until_element_is_clickable(By.ID, self.DATE2_FIELD)
        departure_date2_field.click()
        date2_on_callendar = self.wait_until_element_is_clickable(By.XPATH, self.DATE2_ON_CALLENDAR)
        date2_on_callendar.click()


    def providingPassengers(self):
        number_of_passengers_button = self.wait_until_element_is_clickable(By.XPATH, self.NUMBERS_OF_PASSENGERS_BUTTON)
        number_of_passengers_button.click()
        add_passenger = self.wait_until_element_is_clickable(By.XPATH, self.ADDING_PASSEGNERS_BUTTON)
        add_passenger.click()



    def click_Search(self):
        search_button = self.wait_until_element_is_clickable(By.XPATH, self.CLICK_SEARCH_BUTTON)
        search_button.click()


    def searchFlights(self, departlocation, goingtolocation):
        self.accept_cookies()
        self.enterDepartFromLocation(departlocation)
        self.enterGoingToLocation(goingtolocation)
        self.enter_Departure_Date()
        self.enter_Arrival_Date()
        self.providingPassengers()
        self.click_Search()





        time.sleep(5)

