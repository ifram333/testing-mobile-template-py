from behave import *


@When('I click the login button')
def step_impl(context):
    context.login_page.click_login_button()


@When('I click the to payment button')
def step_impl(context):
    context.checkout_address_page.click_to_payment_button()
