from behave import *


@when('I click the login button')
def step_impl(context):
    context.login_page.click_login_button()


@when('I click the to payment button')
def step_impl(context):
    context.checkout_address_page.click_to_payment_button()
