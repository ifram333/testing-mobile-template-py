import logging

from appium.webdriver.common.appiumby import AppiumBy
from assertpy import assert_that, soft_assertions

from features.pages.base_page import BasePage


class CheckoutAddressPage(BasePage):
    # Label elements
    lbl_checkout = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="container header"]/android.widget.TextView')
    lbl_enter_a_shipping_address = (AppiumBy.XPATH, '//android.widget.ScrollView[@content-desc="checkout address screen"]/android.view.ViewGroup/android.widget.TextView[1]')
    lbl_full_name = (AppiumBy.XPATH, '//android.widget.ScrollView[@content-desc="checkout address screen"]/android.view.ViewGroup/android.widget.TextView[2]')
    lbl_full_name_error_message = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Full Name*-error-message"]/android.widget.TextView')
    lbl_address_line_1 = (AppiumBy.XPATH, '//android.widget.ScrollView[@content-desc="checkout address screen"]/android.view.ViewGroup/android.widget.TextView[3]')
    lbl_address_line_1_error_message = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Address Line 1*-error-message"]/android.widget.TextView')
    lbl_address_line_2 = (AppiumBy.XPATH, '//android.widget.ScrollView[@content-desc="checkout address screen"]/android.view.ViewGroup/android.widget.TextView[4]')
    lbl_address_line_2_error_message = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Address Line 2-error-message"]/android.widget.TextView')
    lbl_city = (AppiumBy.XPATH, '//android.widget.ScrollView[@content-desc="checkout address screen"]/android.view.ViewGroup/android.widget.TextView[5]')
    lbl_city_error_message = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="City*-error-message"]/android.widget.TextView')
    lbl_state_region = (AppiumBy.XPATH, '//android.widget.ScrollView[@content-desc="checkout address screen"]/android.view.ViewGroup/android.widget.TextView[6]')
    lbl_state_region_error_message = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="State/Region-error-message"]/android.widget.TextView')
    lbl_zip_code = (AppiumBy.XPATH, '//android.widget.ScrollView[@content-desc="checkout address screen"]/android.view.ViewGroup/android.widget.TextView[7]')
    lbl_zip_code_error_message = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Zip Code*-error-message"]/android.widget.TextView')
    lbl_country = (AppiumBy.XPATH, '//android.widget.ScrollView[@content-desc="checkout address screen"]/android.view.ViewGroup/android.widget.TextView[8]')
    lbl_country_error_message = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Country*-error-message"]/android.widget.TextView')

    # Input elements
    txt_full_name = (AppiumBy.ANDROID_UIAUTOMATOR, BasePage.no_scroll_description + 'Full Name* input field' + BasePage.no_scroll_wrapper)
    txt_address_line_1 = (AppiumBy.ANDROID_UIAUTOMATOR, BasePage.no_scroll_description + 'Address Line 1* input field' + BasePage.no_scroll_wrapper)
    txt_address_line_2 = (AppiumBy.ANDROID_UIAUTOMATOR, BasePage.no_scroll_description + 'Address Line 2 input field' + BasePage.no_scroll_wrapper)
    txt_city = (AppiumBy.ANDROID_UIAUTOMATOR, BasePage.no_scroll_description + 'City* input field' + BasePage.no_scroll_wrapper)
    txt_state_region = (AppiumBy.ANDROID_UIAUTOMATOR, BasePage.no_scroll_description + 'State/Region input field' + BasePage.no_scroll_wrapper)
    txt_zip_code = (AppiumBy.ANDROID_UIAUTOMATOR, BasePage.no_scroll_description + 'Zip Code* input field' + BasePage.no_scroll_wrapper)
    txt_country = (AppiumBy.ANDROID_UIAUTOMATOR, BasePage.no_scroll_description + 'Country* input field' + BasePage.no_scroll_wrapper)

    # Button elements
    btn_to_payment = (AppiumBy.ANDROID_UIAUTOMATOR, BasePage.no_scroll_description + 'To Payment button' + BasePage.no_scroll_wrapper)

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = logging.getLogger(self.__class__.__name__)

    # Click methods
    def click_to_payment_button(self):
        self.click(*self.btn_to_payment)
        self.logger.info('Click "TO PAYMENT" button')

    # Send Keys methods
    def send_keys_full_name_input(self, full_name):
        self.send_keys(full_name, *self.txt_full_name)
        self.logger.info('Fill "FULL NAME" with value ' + full_name)

    def send_keys_address_line_1_input(self, address_line_1):
        self.send_keys(address_line_1, *self.txt_address_line_1)
        self.logger.info('Fill "ADDRESS LINE 1" with value ' + address_line_1)

    def send_keys_address_line_2_input(self, address_line_2):
        self.send_keys(address_line_2, *self.txt_address_line_2)
        self.logger.info('Fill "ADDRESS LINE 2" with value ' + address_line_2)

    def send_keys_city_input(self, city):
        self.send_keys(city, *self.txt_city)
        self.logger.info('Fill "CITY" with value ' + city)

    def send_keys_state_region_input(self, state_region):
        self.send_keys(state_region, *self.txt_state_region)
        self.logger.info('Fill "STATE/REGION" with value ' + state_region)

    def send_keys_zip_code_input(self, zip_code):
        self.send_keys(zip_code, *self.txt_zip_code)
        self.logger.info('Fill "ZIP CODE" with value ' + zip_code)

    def send_keys_country_input(self, country):
        self.send_keys(country, *self.txt_country)
        self.logger.info('Fill "COUNTRY" with value ' + country)

    # Validation methods
    def validate_page(self):
        with soft_assertions():
            assert_that(self.is_element_found(*self.lbl_checkout)).is_true()
            assert_that(self.is_element_value_equal_to('Checkout', *self.lbl_checkout)).is_true()
            assert_that(self.is_element_found(*self.lbl_enter_a_shipping_address)).is_true()
            assert_that(self.is_element_value_equal_to('Enter a shipping address', *self.lbl_enter_a_shipping_address)).is_true()
            assert_that(self.is_element_found(*self.lbl_full_name)).is_true()
            assert_that(self.is_element_value_equal_to('Full Name*', *self.lbl_full_name)).is_true()
            assert_that(self.is_element_found(*self.txt_full_name)).is_true()
            assert_that(self.is_element_found(*self.lbl_address_line_1)).is_true()
            assert_that(self.is_element_value_equal_to('Address Line 1*', *self.lbl_address_line_1)).is_true()
            assert_that(self.is_element_found(*self.txt_address_line_1)).is_true()
            assert_that(self.is_element_found(*self.lbl_address_line_2)).is_true()
            assert_that(self.is_element_value_equal_to('Address Line 2', *self.lbl_address_line_2)).is_true()
            assert_that(self.is_element_found(*self.txt_address_line_2)).is_true()
            assert_that(self.is_element_found(*self.lbl_city)).is_true()
            assert_that(self.is_element_value_equal_to('City*', *self.lbl_city)).is_true()
            assert_that(self.is_element_found(*self.txt_city)).is_true()
            assert_that(self.is_element_found(*self.lbl_state_region)).is_true()
            assert_that(self.is_element_value_equal_to('State/Region', *self.lbl_state_region)).is_true()
            assert_that(self.is_element_found(*self.txt_state_region)).is_true()
            assert_that(self.is_element_found(*self.lbl_zip_code)).is_true()
            assert_that(self.is_element_value_equal_to('Zip Code*', *self.lbl_zip_code)).is_true()
            assert_that(self.is_element_found(*self.txt_zip_code)).is_true()
            assert_that(self.is_element_found(*self.lbl_country)).is_true()
            assert_that(self.is_element_value_equal_to('Country*', *self.lbl_country)).is_true()
            assert_that(self.is_element_found(*self.txt_country)).is_true()
        self.logger.info('The Checkout page is loaded correctly')

    def validate_full_name_error_message(self):
        assert_that(self.is_element_value_equal_to('Please provide your full name.', *self.lbl_full_name_error_message)).is_true()
        self.logger.info('The correct full name error message (Please provide your full name.) is displayed')

    def validate_address_line_1_error_message(self):
        assert_that(self.is_element_value_equal_to('Please provide your address.', *self.lbl_address_line_1_error_message)).is_true()
        self.logger.info('The correct address line 1 error message (Please provide your address.) is displayed')

    def validate_address_line_2_error_message(self):
        assert_that(self.is_element_value_equal_to('Please provide your address.', *self.lbl_address_line_2_error_message)).is_true()
        self.logger.info('The correct address line 2 error message (Please provide your address.) is displayed')

    def validate_city_error_message(self):
        assert_that(self.is_element_value_equal_to('Please provide your city.', *self.lbl_city_error_message)).is_true()
        self.logger.info('The correct city error message (Please provide your city.) is displayed')

    def validate_state_region_error_message(self):
        assert_that(self.is_element_value_equal_to('Please provide your state/region.', *self.lbl_state_region_error_message)).is_true()
        self.logger.info('The correct state/region error message (Please provide your state/region.) is displayed')

    def validate_zip_code_error_message(self):
        assert_that(self.is_element_value_equal_to('Please provide your zip code.', *self.lbl_zip_code_error_message)).is_true()
        self.logger.info('The correct zip code error message (Please provide your zip code.) is displayed')

    def validate_country_error_message(self):
        assert_that(self.is_element_value_equal_to('Please provide your country.', *self.lbl_country_error_message)).is_true()
        self.logger.info('The correct country error message (Please provide your country.) is displayed')
