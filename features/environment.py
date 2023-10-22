from allure_commons.types import AttachmentType
from appium.webdriver.appium_service import AppiumService
from utils import mobile_driver, mobile_capabilities

import allure

appium_service = AppiumService()


# Hooks
def before_all(context):
    host = context.config.userdata.get('appium_host', '0.0.0.0')
    port = context.config.userdata.get('appium_port', '4723')
    base_path = context.config.userdata.get('appium_base_path', '/wd/hub')
    execute_driver = context.config.userdata.get('appium_driver', 'execute-driver')

    appium_url = f'http://{host}:{port}{base_path}'

    appium_service.start(args=['-a', host, '-p', port, '-pa', base_path, '--use-plugins', execute_driver])
    print(f'Appium server started on <{appium_url}>')


def after_all(context):
    appium_service.stop()
    print('Appium server stopped')


def before_feature(context, feature):
    pass


def after_feature(context, feature):
    pass


def before_scenario(context, scenario):
    host = context.config.userdata.get('appium_host', '0.0.0.0')
    port = context.config.userdata.get('appium_port', '4723')
    base_path = context.config.userdata.get('appium_base_path', '/wd/hub')
    app_name = context.config.userdata.get('app_name', 'unknown')
    device_caps = context.config.userdata.get('device_caps', 'unknown')

    appium_url = f'http://{host}:{port}{base_path}'

    mobile_driver.start_driver(context, appium_url, getattr(mobile_capabilities, device_caps), app_name)
    print(f'{context.platform} driver started')


def after_scenario(context, scenario):
    mobile_driver.stop_driver(context)
    print(f'{context.platform} driver stopped')


def before_step(context, step):
    pass


def after_step(context, step):
    if step.status == "failed":
        allure.attach(context.driver.get_screenshot_as_png(), name=step.name, attachment_type=AttachmentType.PNG)


def before_tag(context, tag):
    pass


def after_tag(context, tag):
    pass
