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
    place_order_button = (By.XPATH, '//button[@class="smart-button"]')

    def __init__(self, driver):
        self.driver = driver  # Initialize the driver

    # Methods to interact with the page

    def enter_from_location(self, from_text):
        from_field = self.driver.find_element(*self.from_field)
        from_field.send_keys(from_text)

    def enter_to_location(self, to_text):
        to_field = self.driver.find_element(*self.to_field)
        to_field.send_keys(to_text)

    def click_taxi_button(self):
        time.sleep(1)
        self.driver.find_element(*self.taxi_button_locator).click()

    def click_supportive_checkbox(self):
        time.sleep(2)
        supportive_checkbox = self.driver.find_element(*self.supportive_checkbox_locator)
        if not supportive_checkbox.is_selected():
            supportive_checkbox.click()
        time.sleep(1)
        if not supportive_checkbox.is_selected():
            supportive_checkbox.click()

    def click_phone_number_button(self):
        time.sleep(1)
        self.driver.find_element(*self.phone_number_button_locator).click()

    def enter_phone_number(self, phone_number):
        time.sleep(1)
        self.driver.find_element(*self.phone_number_field).send_keys(phone_number)

    def click_next_button(self):
        time.sleep(1)
        self.driver.find_element(*self.next_button_locator).click()

    def enter_phone_code(self, phone_code):
        time.sleep(1)
        self.driver.find_element(*self.phone_code_field).send_keys(phone_code)

    def click_confirm_button(self):
        time.sleep(1)
        self.driver.find_element(*self.confirm_button_locator).click()

    def click_payment_method(self):
        time.sleep(1)
        self.driver.find_element(*self.payment_method_locator).click()

    def click_add_card_section(self):
        time.sleep(1)
        self.driver.find_element(*self.add_card_locator).click()

    def enter_card_details(self, card_number, card_code):
        time.sleep(1)

        self.driver.find_element(*self.card_input_locator).send_keys(card_number)
        time.sleep(1)

        self.driver.find_element(*self.card_input_locator).send_keys(Keys.TAB)
        time.sleep(1)

        card_code_field = self.driver.find_element(*self.card_code_locator)
        card_code_field.click()
        card_code_field.send_keys(card_code)

    def click_link_button(self):
        time.sleep(1)
        self.driver.find_element(*self.link_button).click()

    def close_payment_section(self):
        time.sleep(1)
        self.driver.find_element(*self.payment_close_button).click()

    def enter_message_to_driver(self, message):
        time.sleep(1)
        self.driver.find_element(*self.message_to_driver_field).send_keys(message)

    def click_blanket_checkbox(self):
        time.sleep(1)
        self.driver.find_element(*self.blanket_checkbox_locator).click()

    def order_ice_cream(self):
        time.sleep(1)
        plus_button = self.driver.find_element(*self.ice_cream_plus_button)
        for i in range(2):
            plus_button.click()

    def place_order(self):
        time.sleep(1)
        self.driver.find_element(*self.place_order_button).click()
