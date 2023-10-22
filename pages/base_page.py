from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WAIT_TIMER = 20
DIRECTIONS = {'up', 'down', 'left', 'right'}


class BasePage:
    # UiSelectors locators scrollable
    scroll_id = "new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().resourceId(\""
    scroll_id_matches = "new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector(" \
                        ").resourceIdMatches(\"(?i).*"

    scroll_text = "new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text(\""
    scroll_text_contains = "new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector(" \
                           ").textContains(\""
    scroll_text_matches = "new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector(" \
                          ").textMatches(\"(?i)"
    scroll_text_starts_with = "new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector(" \
                              ").textStartsWith(\""

    scroll_description = "new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector(" \
                         ").description(\""
    scroll_description_contains = "new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector(" \
                                  ").descriptionContains(\""
    scroll_description_matches = "new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector(" \
                                 ").descriptionMatches(\"(?i)"
    scroll_description_starts_with = "new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new " \
                                     "UiSelector().descriptionStartsWith(\""

    scroll_class = "new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().className(\""
    scroll_class_matches = "new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector(" \
                           ").classNameMatches(\"(?i)"

    scroll_wrapper = "\"))"

    # UiSelectors locators non scrollable
    no_scroll_id = "new UiSelector().resourceId(\""
    no_scroll_id_matches = "new UiSelector().resourceIdMatches(\"(?i).*"

    no_scroll_text = "new UiSelector().text(\""
    no_Scroll_text_contains = "new UiSelector().textContains(\""
    no_scroll_text_matches = "new UiSelector().textMatches(\"(?i)"
    no_scroll_text_starts_with = "new UiSelector().textStartsWith(\""

    no_scroll_Description = "new UiSelector().description(\""
    no_scroll_description_contains = "new UiSelector().descriptionContains(\""
    no_scroll_description_matches = "new UiSelector().descriptionMatches(\"(?i)"
    no_scroll_description_starts_with = "new UiSelector().descriptionStartsWith(\""

    no_scroll_class = "new UiSelector().className(\""
    no_scroll_class_matches = "new UiSelector().classNameMatches(\"(?i)"

    no_scroll_wrapper = "\")"

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver, WAIT_TIMER).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except Exception as e:
            raise e

    def send_keys(self, value, *loc):
        try:
            self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(value)
        except AttributeError as e:
            raise e

    def is_element_found(self, *loc):
        try:
            WebDriverWait(self.driver, WAIT_TIMER).until(EC.visibility_of_element_located(loc))
            return True
        except TimeoutException:
            return False

    def is_clickable_element(self, *loc):
        try:
            WebDriverWait(self.driver, WAIT_TIMER).until(EC.element_to_be_clickable(loc))
            return True
        except TimeoutException:
            return False

    def send_key(self, key_event):
        try:
            self.driver.keyevent(key_event)
        except Exception as e:
            raise e

    def android_swipe(self, direction, loc=None, percent=80):
        if direction not in DIRECTIONS:
            raise ValueError('directions: value must be one of %r' % DIRECTIONS)

        if percent not in range(0, 100):
            raise ValueError('percent: value must be between 0 - 100')

        params = {'percent': round(percent / 100),
                  'speed': '1100',
                  'direction': direction}

        if loc is not None:
            WebDriverWait(self.driver, WAIT_TIMER).until(EC.visibility_of_element_located(loc))
            element = self.driver.find_element(*loc)
            params['elementId'] = element.id
        else:
            window_screen_dimensions = self.driver.get_window_size()
            width = window_screen_dimensions['width']
            height = window_screen_dimensions['height']
            params['left'] = int(width * 0.1)
            params['top'] = int(height * 0.1)
            params['width'] = width
            params['height'] = height

        self.driver.execute_script('mobile: swipeGesture', params)
