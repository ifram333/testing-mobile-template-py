import os

from appium import webdriver


def start_driver(context, appium_url, capabilities, app):
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    app_path = root_dir + '/apps/' + app
    desired_capabilities = capabilities
    context.platform = desired_capabilities.get('platformName')
    desired_capabilities['app'] = app_path
    print(desired_capabilities)

    context.driver = webdriver.Remote(appium_url, desired_capabilities)

    if context.platform == 'Android':
        from pages.android.login_page import LogInPage
    elif context.platform == 'iOS':
        from pages.android.login_page import LogInPage

    context.login_page = LogInPage(context.driver)


def stop_driver(context):
    context.driver.quit()
    pass
