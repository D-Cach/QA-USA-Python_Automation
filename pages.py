import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class UrbanRoutesPage:
    # Locators as class attributes
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    supportive_checkbox_locator = (By.XPATH, '//img[@alt="Supportive"]')
    taxi_button_locator = (By.XPATH, '//button[@type="button" and contains(@class, "button round") and text()="Call a taxi"]')
    phone_number_button_locator = (By.XPATH, "//div[@class='np-button']//div[text()='Phone number']")
    phone_number_field = (By.XPATH, '//div[@class="input-container"]/input[@id="phone"]')
    next_button_locator = (By.XPATH, '//button[@type="submit" and contains(@class, "button full") and text()="Next"]')
    phone_code_field = (By.ID, 'code')
    confirm_button_locator = (By.XPATH, '//button[@type="submit" and contains(@class, "button full") and text()="Confirm"]')

    # Payment-related locators
    payment_method_locator = (By.CSS_SELECTOR, '.pp-text')
    add_card_locator = (By.CSS_SELECTOR, '.pp-row.disabled')
    card_input_locator = (By.ID, 'number')
    card_code_locator = (By.XPATH, '//input[@class="card-input" and @id="code"]')
    link_button = (By.XPATH, '//div[@class="pp-buttons"]//button[@type="submit"]')
    payment_close_button = (By.XPATH, '//div[@class="payment-picker open"]//button[@class="close-button section-close"]')

    # Other locators
    message_to_driver_field = (By.ID, 'comment')
    blanket_checkbox_locator = (By.XPATH, '(//span[@class="slider round"])[1]')
    ice_cream_plus_button = (By.XPATH, '(//div[@class="counter-plus"])[1]')
    ice_cream_counter = (By.XPATH, '(//div[@class="counter-value"])[1]')
    place_order_button = (By.XPATH, '//button[@class="smart-button"]')
    car_search_model_locator = (By.XPATH, '//div[contains(@class, "searching-car")]')

    def __init__(self, driver):
        self.driver = driver  # Initialize the driver

    # Methods to interact with the page

    def enter_from_location(self, from_text):
        from_field = self.driver.find_element(*self.from_field)
        from_field.send_keys(from_text)

    def enter_to_location(self, to_text):
        to_field = self.driver.find_element(*self.to_field)
        to_field.send_keys(to_text)

    def get_from_location_value(self):
        from_field = self.driver.find_element(*self.from_field)
        return from_field.get_attribute("value")

    def get_to_location_value(self):
        to_field = self.driver.find_element(*self.to_field)
        return to_field.get_attribute("value")

    def get_taxi_button_class(self):
        taxi_button = self.driver.find_element(*self.taxi_button_locator)
        return taxi_button.get_attribute("class")

    def is_payment_section_open(self):
        payment_section = self.driver.find_elements(*self.payment_method_locator)
        return len(payment_section) > 0

    def click_taxi_button(self):
        self.driver.find_element(*self.taxi_button_locator).click()

    def click_supportive_checkbox(self):
        supportive_checkbox = self.driver.find_element(*self.supportive_checkbox_locator)
        if not supportive_checkbox.is_selected():
            supportive_checkbox.click()
        if not supportive_checkbox.is_selected():
            supportive_checkbox.click()

    def click_phone_number_button(self):
        self.driver.find_element(*self.phone_number_button_locator).click()

    def enter_phone_number(self, phone_number):
        self.driver.find_element(*self.phone_number_field).send_keys(phone_number)

    def click_next_button(self):
        self.driver.find_element(*self.next_button_locator).click()

    def enter_phone_code(self, phone_code):
        self.driver.find_element(*self.phone_code_field).send_keys(phone_code)

    def click_confirm_button(self):
        self.driver.find_element(*self.confirm_button_locator).click()

    def is_confirm_button_present(self):
        confirm_button = self.driver.find_elements(*self.confirm_button_locator)
        return len(confirm_button) > 0

    def click_payment_method(self):
        self.driver.find_element(*self.payment_method_locator).click()

    def click_add_card_section(self):
        self.driver.find_element(*self.add_card_locator).click()

    def enter_card_details(self, card_number, card_code):
        self.driver.find_element(*self.card_input_locator).send_keys(card_number)
        self.driver.find_element(*self.card_input_locator).send_keys(Keys.TAB)

        card_code_field = self.driver.find_element(*self.card_code_locator)
        card_code_field.click()
        card_code_field.send_keys(card_code)

    def click_link_button(self):
        self.driver.find_element(*self.link_button).click()

    def is_card_linked(self):
        linked_card_section = self.driver.find_elements(*self.card_input_locator)
        return len(linked_card_section) > 0

    def close_payment_section(self):
        self.driver.find_element(*self.payment_close_button).click()

    def enter_message_to_driver(self, message):
        self.driver.find_element(*self.message_to_driver_field).send_keys(message)

    def get_driver_message(self):
        message_field = self.driver.find_element(*self.message_to_driver_field)
        return message_field.get_attribute('value')

    def click_blanket_checkbox(self):
        self.driver.find_element(*self.blanket_checkbox_locator).click()

    def is_blanket_selected(self):
        # Find the span element that represents the checkbox toggle
        slider = self.driver.find_element(*self.blanket_checkbox_locator)

        # Check if the class contains 'checked' or another indicator of being selected
        return 'checked' in slider.get_attribute('class')

    def order_ice_cream(self):
        plus_button = self.driver.find_element(*self.ice_cream_plus_button)
        for i in range(2):
            plus_button.click()

    def get_ice_cream_count(self):
        counter = self.driver.find_element(*self.ice_cream_counter)
        return int(counter.text)

    def place_order(self):
        self.driver.find_element(*self.place_order_button).click()

    def is_car_search_displayed(self):
        elements = self.driver.find_elements(By.CLASS_NAME, "order-subbody")
        return len(elements) > 0



