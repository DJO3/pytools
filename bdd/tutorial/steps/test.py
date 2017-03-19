from behave import *

@given('we have added a second test')
def step_impl(context):
    pass

@when('we implement a second test')
def step_impl(context):
    assert True is not False

@then('behave will run the new test!')
def step_impl(context):
    assert context.failed is False