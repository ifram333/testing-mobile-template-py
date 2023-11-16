from behave import *


@when('I fill the username "{username}"')
def step_impl(context, username):
    context.login_page.send_keys_username_input(username)


@when('I fill the password "{password}"')
def step_impl(context, password):
    context.login_page.send_keys_password_input(password)
