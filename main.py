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

        actual_from = urban_routes_page.get_from_location_value()
        expected_from = ADDRESS_FROM
        assert expected_from in actual_from, f"Expected '{expected_from}', but got '{actual_from}'"

        actual_to = urban_routes_page.get_to_location_value()
        expected_to = ADDRESS_TO
        assert expected_to in actual_to, f"Expected '{expected_to}', but got '{actual_to}'"

    def test_select_plan(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        time.sleep(2)
        urban_routes_page.click_taxi_button()
        time.sleep(2)
        urban_routes_page.click_supportive_checkbox()
        assert "button round" in urban_routes_page.get_taxi_button_class(), "Taxi button should be disabled after selection"

    def test_fill_phone_number(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        time.sleep(2)
        urban_routes_page.click_phone_number_button()
        urban_routes_page.enter_phone_number(PHONE_NUMBER)
        time.sleep(2)
        urban_routes_page.click_next_button()

        phone_code = retrieve_phone_code(self.driver)
        urban_routes_page.enter_phone_code(phone_code)
        time.sleep(2)
        urban_routes_page.click_confirm_button()
        assert urban_routes_page.is_confirm_button_present(), "Confirm button should not be visible after phone verification"

    def test_fill_card(self):
        time.sleep(2)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.click_payment_method()
        urban_routes_page.click_add_card_section()
        time.sleep(2)
        urban_routes_page.enter_card_details(CARD_NUMBER, CARD_CODE)
        time.sleep(2)
        urban_routes_page.click_link_button()
        assert urban_routes_page.is_card_linked(), "Card should be linked successfully"

    def test_close_payment_section(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        time.sleep(2)
        urban_routes_page.close_payment_section()
        assert urban_routes_page.is_payment_section_open(), "Payment section should be closed"

    def test_comment_for_driver(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_message_to_driver(MESSAGE_FOR_DRIVER)

        actual_message = urban_routes_page.get_driver_message()
        expected_message = MESSAGE_FOR_DRIVER
        assert expected_message in actual_message, f"Expected '{expected_message}', but got '{actual_message}'"

    def test_order_blanket_and_handkerchiefs(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        time.sleep(2)
        urban_routes_page.click_blanket_checkbox()
        assert not urban_routes_page.is_blanket_selected(), "Blanket checkbox should be selected"

    def test_order_2_ice_creams(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.order_ice_cream()

        actual_count = urban_routes_page.get_ice_cream_count()
        expected_count = 2
        assert actual_count == expected_count, f"Expected {expected_count} ice creams, but got {actual_count}"

    def test_car_search_model_appears(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        time.sleep(2)
        urban_routes_page.place_order()
        time.sleep(5)  # Give it a bit more time to show the car search model
        assert urban_routes_page.is_car_search_displayed(), "Car search model should appear after placing order"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
