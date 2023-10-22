from appium import webdriver


def start_driver(context, appium_url, capabilities, app, sim=False):
    app_path = '/Users/ivanramirez/PycharmProjects/testing-mobile-template-py/apps/' + app
    desired_capabilities = capabilities

    context.platform = desired_capabilities.get('platformName')

    if context.platform == 'Android':
        app_path = app_path + '.apk'
    elif context.platform == 'iOS':
        if sim:
            app_path = app_path + '.ipa'
        else:
            app_path = app_path + '.app'

    desired_capabilities['app'] = app_path
    print(desired_capabilities)

    context.driver = webdriver.Remote(appium_url, desired_capabilities)

    if context.platform == 'Android':
        from pages.android.onboarding_page import OnboardingPage
    elif context.platform == 'iOS':
        from pages.ios.onboarding_page import OnboardingPage

    context.onboarding_page = OnboardingPage(context.driver)


def stop_driver(context):
    context.driver.quit()
    pass
