import logging

from appium.webdriver.common.appiumby import AppiumBy
from assertpy import assert_that, soft_assertions

from features.pages.base_page import BasePage


class LogInPage(BasePage):
    # Label elements
    lbl_login = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="container header"]/android.widget.TextView')
    lbl_select_username_and_password = (AppiumBy.ANDROID_UIAUTOMATOR, BasePage.no_scroll_text + 'Select a username and password from the list below, or click on the usernames to automatically populate the username and password.' + BasePage.no_scroll_wrapper)
    lbl_username = (AppiumBy.XPATH, '//android.widget.EditText[@content-desc="Username input field"]/preceding-sibling::android.widget.TextView[last()]')
    lbl_username_error_message = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Username-error-message"]/android.widget.TextView')
    lbl_password = (AppiumBy.XPATH, '//android.widget.EditText[@content-desc="Password input field"]/preceding-sibling::android.widget.TextView[last()]')
    lbl_password_error_message = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Password-error-message"]/android.widget.TextView')
    lbl_error_message = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="generic-error-message"]/android.widget.TextView')

    # Input elements
    txt_username = (AppiumBy.ANDROID_UIAUTOMATOR, BasePage.no_scroll_description + 'Username input field' + BasePage.no_scroll_wrapper)
    txt_password = (AppiumBy.ANDROID_UIAUTOMATOR, BasePage.no_scroll_description + 'Password input field' + BasePage.no_scroll_wrapper)

    # Button elements
    btn_login = (AppiumBy.ANDROID_UIAUTOMATOR, BasePage.no_scroll_description + 'Login button' + BasePage.no_scroll_wrapper)

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = logging.getLogger(self.__class__.__name__)

    # Click methods
    def click_login_button(self):
        self.click(*self.btn_login)
        self.logger.info('Click "LOGIN" button')

    # Send Keys methods
    def send_keys_username_input(self, username):
        self.send_keys(username, *self.txt_username)
        self.logger.info('Fill "USERNAME" with value ' + username)

    def send_keys_password_input(self, password):
        self.send_keys(password, *self.txt_password)
        self.logger.info('Fill "PASSWORD" with value ' + password)

    # Validation methods
    def validate_page(self):
        with soft_assertions():
            assert_that(self.is_element_value_equal_to('Login', *self.lbl_login)).is_true()
            assert_that(self.is_element_found(*self.lbl_select_username_and_password)).is_true()
            assert_that(self.is_element_value_equal_to('Username', *self.lbl_username)).is_true()
            assert_that(self.is_element_found(*self.txt_username)).is_true()
            assert_that(self.is_element_enabled(*self.txt_username)).is_true()
            assert_that(self.is_element_value_equal_to('Password', *self.lbl_password)).is_true()
            assert_that(self.is_element_found(*self.txt_password)).is_true()
            assert_that(self.is_element_enabled(*self.txt_password)).is_true()
            assert_that(self.is_element_found(*self.btn_login)).is_true()
            assert_that(self.is_element_enabled(*self.btn_login)).is_true()
        self.logger.info('The Login page is loaded correctly')

    def validate_username_error_message(self):
        assert_that(self.is_element_value_equal_to('Username is required', *self.lbl_username_error_message)).is_true()
        self.logger.info('The correct username error message (Username is required) is displayed')

    def validate_password_error_message(self):
        assert_that(self.is_element_value_equal_to('Password is required', *self.lbl_password_error_message)).is_true()
        self.logger.info('The correct username error message (Password is required) is displayed')

    def validate_error_message(self, message):
        assert_that(self.is_element_value_equal_to(message, *self.lbl_error_message)).is_true()
        self.logger.info('The correct username error message ('+message+') is displayed')
