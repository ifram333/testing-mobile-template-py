from behave import *


@Given('I swipe from the first slide to the last slide')
def step_impl(context):
    context.onboarding_page.validate_vehicle_info_slide()
    context.onboarding_page.swipe_onboarding_slide_left()
    context.onboarding_page.validate_service_slide()
    context.onboarding_page.swipe_onboarding_slide_left()
    context.onboarding_page.validate_all_services_slide()
    context.onboarding_page.swipe_onboarding_slide_left()
    context.onboarding_page.validate_deals_slide()
    context.onboarding_page.swipe_onboarding_slide_left()
    context.onboarding_page.validate_around_slide()
    context.onboarding_page.swipe_onboarding_slide_left()
    context.onboarding_page.validate_every_mile_slide()
    context.onboarding_page.swipe_onboarding_slide_left()
    context.onboarding_page.validate_monitor_slide()
    context.onboarding_page.swipe_onboarding_slide_left()
    context.onboarding_page.validate_keep_your_car_running_slide()


@Given('I swipe from the last slide to the first slide')
def step_impl(context):
    context.onboarding_page.validate_keep_your_car_running_slide()
    context.onboarding_page.swipe_onboarding_slide_right()
    context.onboarding_page.validate_monitor_slide()
    context.onboarding_page.swipe_onboarding_slide_right()
    context.onboarding_page.validate_every_mile_slide()
    context.onboarding_page.swipe_onboarding_slide_right()
    context.onboarding_page.validate_around_slide()
    context.onboarding_page.swipe_onboarding_slide_right()
    context.onboarding_page.validate_deals_slide()
    context.onboarding_page.swipe_onboarding_slide_right()
    context.onboarding_page.validate_all_services_slide()
    context.onboarding_page.swipe_onboarding_slide_right()
    context.onboarding_page.validate_service_slide()
    context.onboarding_page.swipe_onboarding_slide_right()
    context.onboarding_page.validate_vehicle_info_slide()


@When('The get started button is displayed')
def step_impl(context):
    context.onboarding_page.validate_get_started_button()


@When('I click on get started')
def step_impl(context):
    context.onboarding_page.click_btn_get_started()
