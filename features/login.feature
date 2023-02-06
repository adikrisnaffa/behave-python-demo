Feature: Login Feature

Scenario: Success Login with correct credential;
    Given I am on the homepage
    When I click Sign in
    And I fill my credential
    Then I should be logged in