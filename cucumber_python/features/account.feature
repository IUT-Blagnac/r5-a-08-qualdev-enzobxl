# Created by enzob at 13/12/2023
Feature: Account testing

  Scenario: Creating an empty account
    Given John who wants to create an account
    When Creation of the account
    Then The account balance is 0

  Scenario Outline: Deposit money on account
    Given An empty account
    When Deposit <deposit_amount> on the account
    Then After the deposit, the account balance is <balance>
    Examples:
      | deposit_amount | balance |
      | 200            | 200     |
      | 769            | 769     |
      | -8             | 0       |

  Scenario Outline: Withdraw money on account
    Given An account with <initial_amount>
    When Withdraw <withdraw_amount> on the account
    Then After the withdraw, the account balance is <balance>
    Examples:
      | initial_amount | withdraw_amount | balance |
      | 0              | 200             | 0       |
      | 250            | 200             | 50      |
      | 30             | 100             | 30      |
      | 670            | 400             | 270     |