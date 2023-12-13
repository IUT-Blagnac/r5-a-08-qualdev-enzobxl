from behave import *

from account import Account


@given("{name} who wants to create an account")
def step_init_given(context, name):
    """
    :type name:
    :type context: behave.runner.Context
    """
    context.name = name


@when("Creation of the account")
def step_init_when(context):
    """
    :type context: behave.runner.Context
    """
    context.account = Account(context.name)


@then("The account balance is 0")
def step_init_then(context):
    """
    :type context: behave.runner.Context
    """
    assert context.account.get_balance() == 0


@given("An empty account")
def step_deposit_given(context):
    """
    :type context: behave.runner.Context
    """
    context.account = Account('test')


@when("Deposit {amount:n} on the account")
def step_deposit_when(context, amount):
    """
    :type amount: int
    :type context: behave.runner.Context
    """
    context.account.deposit(amount)


@then("After the deposit, the account balance is {balance:n}")
def step_deposit_then(context, balance):
    """
    :type balance: int
    :type context: behave.runner.Context
    """
    assert context.account.get_balance() == balance


@given("An account with {initial_amount:g}")
def step_withdraw_given(context, initial_amount):
    """
    :type initial_amount: float
    :type context: behave.runner.Context
    """
    context.account = Account('test', initial_amount)


@when("Withdraw {amount:n} on the account")
def step_withdraw_when(context, amount):
    """
    :type amount: int
    :type context: behave.runner.Context
    """
    context.account.withdraw(amount)


@then("After the withdraw, the account balance is {balance:n}")
def step_withdraw_then(context, balance):
    """
    :type context: behave.runner.Context
    :type balance: int
    """
    assert context.account.get_balance() == balance
