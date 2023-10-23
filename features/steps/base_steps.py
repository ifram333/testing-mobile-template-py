import subprocess

from behave import *


@Given('The app loads the "{page}" page')
def step_impl(context, page):
    if page.upper() == 'LOGIN':
        subprocess.Popen(
            'adb shell am start -W -a android.intent.action.VIEW -d "mydemoapprn://login" com.saucelabs.mydemoapp.rn',
            shell=True)
    elif page.upper() == 'STORE':
        subprocess.Popen(
            'adb shell am start -W -a android.intent.action.VIEW -d "mydemoapprn://store-overview" com.saucelabs.mydemoapp.rn',
            shell=True)


@Given('I log in to the app with username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.login_page.validate_page()
    context.login_page.send_keys_username_input(username)
    context.login_page.send_keys_password_input(password)
    context.login_page.click_login_button()
