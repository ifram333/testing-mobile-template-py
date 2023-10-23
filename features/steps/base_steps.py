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
