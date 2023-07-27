import pytest
import softest
from pages.esky_launch_page import LaunchPage
from pages.esky_search_result_flights import ResultSearchFlightsPage
from ddt import ddt, data, unpack, file_data



@pytest.mark.usefixtures("setup")
@ddt
class TestSearchAndVeryfiFilter(softest.TestCase):


    @pytest.fixture(autouse=True)
    def class_setup(self):

        self.lp = LaunchPage(self.driver)
        self.rfp = ResultSearchFlightsPage(self.driver)



    #@data(("Warszawa","Paryż"))
    #@unpack
    @file_data("../test_data/testdata.json")
    def test_search_flights(self, departlocation, goingtolocation):

        self.lp.searchFlights(departlocation, goingtolocation)
        self.rfp.change_filters()
        self.rfp.resultsOnResultPage()


