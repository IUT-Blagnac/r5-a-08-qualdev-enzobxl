# Created by enzob at 11/12/2023
# language: en
Feature: Is it Friday yet?
  # Enter feature description here

  Scenario: Friday is Friday
    Given today is Friday
    When I ask whether it's Friday yet
    Then I should be told "TGIF"