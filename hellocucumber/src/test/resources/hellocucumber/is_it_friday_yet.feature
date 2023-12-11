# Created by enzob at 11/12/2023
# language: en
Feature: Is it Friday yet?
  # Enter feature description here

  Scenario Outline: Friday is Friday
    Given today is "<day>"
    When I ask whether it's Friday yet
    Then I should be told "<answer>"
    Examples:
      | day            | answer |
      | Friday         | TGIF   |
      | Sunday         | Nope   |
      | anything else! | Nope   |