from behave import *


@When('I click the login button')
def step_impl(context):
    context.login_page.click_login_button()
