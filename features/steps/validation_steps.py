from behave import *


@Given('The Login screen is displayed')
def step_impl(context):
    context.login_page.validate_page()


@Then('The Checkout Shipping Address screen is displayed')
def step_impl(context):
    pass
