@Onboarding
Feature: Onboarding
  The purpose of this feature is to test the functionalities of the Onboarding screen

  @Test
  Scenario: 01. Navigate through the onboarding slides and allow notifications
    Given I swipe from the first slide to the last slide
    And I swipe from the last slide to the first slide
    And I swipe from the first slide to the last slide
    When The get started button is displayed
    And I click on get started