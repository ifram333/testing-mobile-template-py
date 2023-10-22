from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class OnboardingPage(BasePage):
    # Images elements
    img_onboarding = (
        AppiumBy.ANDROID_UIAUTOMATOR, BasePage.no_scroll_id_matches + "boardingImg" + BasePage.no_scroll_wrapper)

    # Label elements
    lbl_vehicle_info = (AppiumBy.ANDROID_UIAUTOMATOR,
                        BasePage.no_scroll_text_matches + "ALL YOUR VEHICLE'S INFO IN ONE PLACE" + BasePage.no_scroll_wrapper)
    lbl_vehicle_info_description = (AppiumBy.ANDROID_UIAUTOMATOR,
                                    BasePage.no_scroll_text_matches + "Manage all your vehicles from the My Garage tab and get access to all the information and services you need to keep them in shape." + BasePage.no_scroll_wrapper)
    lbl_service = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        BasePage.no_scroll_text_matches + "GET THE BEST SERVICE" + BasePage.no_scroll_wrapper)
    lbl_service_description = (AppiumBy.ANDROID_UIAUTOMATOR,
                               BasePage.no_scroll_text_matches + "Explore the services tab to find what we can do for your vehicle." + BasePage.no_scroll_wrapper)
    lbl_all_services = (AppiumBy.ANDROID_UIAUTOMATOR,
                        BasePage.no_scroll_text_matches + "ALL THE SERVICES FOR YOUR CAR, RIGHT AT HOME" + BasePage.no_scroll_wrapper)
    lbl_all_services_description = (AppiumBy.ANDROID_UIAUTOMATOR,
                                    BasePage.no_scroll_text_matches + "Our mobile mechanics and fully-equipped service vans offer 12 different categories of service that you can have performed on your car right on your driveway or parking space." + BasePage.no_scroll_wrapper)
    lbl_deals = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        BasePage.no_scroll_text_matches + "GET THE BEST DEALS" + BasePage.no_scroll_wrapper)
    lbl_deals_description = (AppiumBy.ANDROID_UIAUTOMATOR,
                             BasePage.no_scroll_text_matches + "Explore the Offers tab to find the latest discounts and rebates just for you." + BasePage.no_scroll_wrapper)
    lbl_around = (AppiumBy.ANDROID_UIAUTOMATOR,
                  BasePage.no_scroll_text_matches + "WE'RE JUST AROUND THE CORNER" + BasePage.no_scroll_wrapper)
    lbl_around_description = (AppiumBy.ANDROID_UIAUTOMATOR,
                              BasePage.no_scroll_text_matches + "Find the most convenient store for you in the Stores tab. We'll be happy you visit, and ready to give you the best service." + BasePage.no_scroll_wrapper)
    lbl_every_mile = (AppiumBy.ANDROID_UIAUTOMATOR,
                      BasePage.no_scroll_text_matches + "WITH YOU EVERY MILE OF THE ROAD" + BasePage.no_scroll_wrapper)
    lbl_every_mile_description = (AppiumBy.ANDROID_UIAUTOMATOR,
                                  BasePage.no_scroll_text_matches + "Keep your vehicle's mileage updated to receive the best maintenance recommendations from your preferred manufacturer." + BasePage.no_scroll_wrapper)
    lbl_monitor_vehicle = (AppiumBy.ANDROID_UIAUTOMATOR,
                           BasePage.no_scroll_text_matches + "MONITOR YOUR VEHICLE HISTORY" + BasePage.no_scroll_wrapper)
    lbl_monitor_vehicle_description = (AppiumBy.ANDROID_UIAUTOMATOR,
                                       BasePage.no_scroll_text_matches + "We'll help you keep track of every service performed on your vehicle. A record is easily accessible for your convenience." + BasePage.no_scroll_wrapper)
    lbl_keep_your_car_running = (AppiumBy.ANDROID_UIAUTOMATOR,
                                 BasePage.no_scroll_text_matches + "WE KEEP YOUR CAR RUNNING NEWER LONGER" + BasePage.no_scroll_wrapper)
    lbl_keep_your_car_running_description = (AppiumBy.ANDROID_UIAUTOMATOR,
                                             BasePage.no_scroll_text_matches + "From a new set of tires to an oil change, alignment to brakes, we're committed to helping keep your car running newer longer." + BasePage.no_scroll_wrapper)

    # Button elements
    btn_sign_up = (
        AppiumBy.ANDROID_UIAUTOMATOR, BasePage.no_scroll_text_matches + "SIGN UP" + BasePage.no_scroll_wrapper)
    btn_log_in = (AppiumBy.ANDROID_UIAUTOMATOR, BasePage.no_scroll_text_matches + "LOG IN" + BasePage.no_scroll_wrapper)
    btn_get_started = (
        AppiumBy.ANDROID_UIAUTOMATOR, BasePage.no_scroll_text_matches + "GET STARTED" + BasePage.no_scroll_wrapper)

    # Click functions
    def click_btn_sign_up(self):
        if self.is_element_found(*self.btn_sign_up) is True:
            self.find_element(*self.btn_sign_up).click()

    def click_btn_log_in(self):
        if self.is_element_found(*self.btn_log_in) is True:
            self.find_element(*self.btn_log_in).click()

    def click_btn_get_started(self):
        if self.is_element_found(*self.btn_get_started) is True:
            self.find_element(*self.btn_get_started).click()

    # Validate functions
    def validate_get_started_button(self):
        assert self.is_element_found(*self.btn_get_started) is True

    def validate_vehicle_info_slide(self):
        assert self.is_element_found(*self.lbl_vehicle_info) is True
        assert self.is_element_found(*self.lbl_vehicle_info_description) is True

    def validate_service_slide(self):
        assert self.is_element_found(*self.lbl_service) is True
        assert self.is_element_found(*self.lbl_service_description) is True

    def validate_all_services_slide(self):
        assert self.is_element_found(*self.lbl_all_services) is True
        assert self.is_element_found(*self.lbl_all_services_description) is True

    def validate_deals_slide(self):
        assert self.is_element_found(*self.lbl_deals) is True
        assert self.is_element_found(*self.lbl_deals_description) is True

    def validate_around_slide(self):
        assert self.is_element_found(*self.lbl_around) is True
        assert self.is_element_found(*self.lbl_around_description) is True

    def validate_every_mile_slide(self):
        assert self.is_element_found(*self.lbl_every_mile) is True
        assert self.is_element_found(*self.lbl_every_mile_description) is True

    def validate_monitor_slide(self):
        assert self.is_element_found(*self.lbl_monitor_vehicle) is True
        assert self.is_element_found(*self.lbl_monitor_vehicle_description) is True

    def validate_keep_your_car_running_slide(self):
        assert self.is_element_found(*self.lbl_keep_your_car_running) is True
        assert self.is_element_found(*self.lbl_keep_your_car_running_description) is True

    # Swipe functions
    def swipe_onboarding_slide_left(self):
        self.android_swipe('left', self.img_onboarding)

    def swipe_onboarding_slide_right(self):
        self.android_swipe('right', self.img_onboarding)
