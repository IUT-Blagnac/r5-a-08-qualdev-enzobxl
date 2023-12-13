# Created by enzob at 13/12/2023
Feature: Account testing

  Scenario: Creating an empty account
    Given John who wants to create an account
    When Creation of the account
    Then The account balance is 0

  Scenario Outline: Deposit money on account
    Given An empty account for deposit
    When Deposit <amount> on the account
    Then The deposit account balance is <balance>
    Examples:
      | amount | balance |
      | 200    | 200     |
      | 769    | 769     |
      | -8     | 0       |

  Scenario Outline: Withdraw money on empty account
    Given An empty account for withdraw
    When Withdraw <amount> on the account
    Then The withdraw account balance is <balance>
    Examples:
      | amount | balance |
      | 200    | 0       |
      | -17    | 0       |