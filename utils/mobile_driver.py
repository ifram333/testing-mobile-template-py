import os

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions


def start_driver(context, appium_url, capabilities, app):
    global options

    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    app_path = root_dir + '/apps/' + app
    desired_capabilities = capabilities
    context.platform = desired_capabilities.get('platformName')
    desired_capabilities['app'] = app_path

    if context.platform == 'Android':
        options = UiAutomator2Options()
        options.load_capabilities(desired_capabilities)

        from features.pages.android.login_page import LogInPage
    elif context.platform == 'iOS':
        options = XCUITestOptions()
        options.load_capabilities(desired_capabilities)

        from features.pages.android.login_page import LogInPage

    context.driver = webdriver.Remote(appium_url, options=options)
    context.login_page = LogInPage(context.driver)


def stop_driver(context):
    context.driver.quit()
    pass
