import time
from data import URBAN_ROUTES_URL, ADDRESS_FROM, ADDRESS_TO, PHONE_NUMBER, CARD_NUMBER, CARD_CODE, MESSAGE_FOR_DRIVER
from helpers import is_url_reachable, retrieve_phone_code
from pages import UrbanRoutesPage
from selenium import webdriver

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        # Do not modify - additional logging enabled to retrieve phone confirmation code
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

        if is_url_reachable(URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

        cls.driver.get(URBAN_ROUTES_URL)
        time.sleep(2)

    def test_set_route(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        time.sleep(2)
        urban_routes_page.enter_from_location(ADDRESS_FROM)
        urban_routes_page.enter_to_location(ADDRESS_TO)

    def test_select_plan(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        time.sleep(3)
        urban_routes_page.click_taxi_button()
        urban_routes_page.click_supportive_checkbox()

    def test_fill_phone_number(self):
        time.sleep(1)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.click_phone_number_button()
        urban_routes_page.enter_phone_number(PHONE_NUMBER)
        urban_routes_page.click_next_button()

        time.sleep(5)
        phone_code = retrieve_phone_code(self.driver)
        urban_routes_page.enter_phone_code(phone_code)
        urban_routes_page.click_confirm_button()

    def test_fill_card(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        time.sleep(2)

        urban_routes_page.click_payment_method()
        urban_routes_page.click_add_card_section()

        urban_routes_page.enter_card_details(CARD_NUMBER, CARD_CODE)
        urban_routes_page.click_link_button()

    def test_close_payment_section(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        time.sleep(2)
        urban_routes_page.close_payment_section()

    def test_comment_for_driver(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        time.sleep(2)
        urban_routes_page.enter_message_to_driver(MESSAGE_FOR_DRIVER)

    def test_order_blanket_and_handkerchiefs(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        time.sleep(2)
        urban_routes_page.click_blanket_checkbox()

    def test_order_2_ice_creams(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        time.sleep(2)
        urban_routes_page.order_ice_cream()

    def test_car_search_model_appears(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        time.sleep(2)
        urban_routes_page.place_order()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
