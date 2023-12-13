from behave import *

from account import Account


@given("{name} who wants to create an account")
def step_given_name_wants_to_create_an_account(context, name):
    """
    :type name:
    :type context: behave.runner.Context
    """
    context.name = name


@when("Creation of the account")
def step_when_creation_of_the_account(context):
    """
    :type context: behave.runner.Context
    """
    context.account = Account(context.name)


@then("The account balance is 0")
def step_then_the_account_balance_is_0(context):
    """
    :type context: behave.runner.Context
    """
    assert context.account.get_balance() == 0


@given("An empty account for deposit")
def step_given_an_empty_account_for_deposit(context):
    """
    :type context: behave.runner.Context
    """
    context.deposit_account = Account('test')


@when("Deposit {amount:n} on the account")
def step_when_add_amount_on_the_account(context, amount):
    """
    :type amount: int
    :type context: behave.runner.Context
    """
    context.deposit_account.deposit(amount)


@then("The deposit account balance is {balance:n}")
def step_then_the_deposit_account_balance_is_balance(context, balance):
    """
    :type balance: int
    :type context: behave.runner.Context
    """
    assert context.deposit_account.get_balance() == balance


@given("An empty account for withdraw")
def step_given_an_empty_account_for_withdraw(context):
    """
    :type context: behave.runner.Context
    """
    context.withdraw_account = Account('test')


@when("Withdraw {amount:n} on the account")
def step_withdraw_amount_on_the_account(context, amount):
    """
    :type amount: int
    :type context: behave.runner.Context
    """
    context.withdraw_account.withdraw(amount)


@then("The withdraw account balance is {balance:n}")
def step_impl(context, balance):
    """
    :type context: behave.runner.Context
    :type balance: int
    """
    assert context.withdraw_account.get_balance() == balance
