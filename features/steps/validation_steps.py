from behave import *


@Given('The Login screen is displayed')
def step_impl(context):
    context.login_page.validate_page()


@Then('The user message "{message}" is displayed')
def step_impl(context, message):
    context.login_page.validate_error_message(message)


@Then('The username is required message is displayed')
def step_impl(context):
    context.login_page.validate_username_error_message()


@Then('The password is required message is displayed')
def step_impl(context):
    context.login_page.validate_password_error_message()


@Given('The Checkout Shipping Address screen is displayed')
def step_impl(context):
    context.checkout_address_page.validate_page()


@Then('The checkout shipping address error messages are displayed')
def step_impl(context):
    context.checkout_address_page.validate_full_name_error_message()
    context.checkout_address_page.validate_address_line_1_error_message()
    context.checkout_address_page.validate_city_error_message()
    context.checkout_address_page.validate_zip_code_error_message()
    context.checkout_address_page.validate_country_error_message()
