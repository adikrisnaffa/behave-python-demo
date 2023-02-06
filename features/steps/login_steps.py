from behave import *
from selenium.webdriver.common.by import By

@given(u'I am on the homepage')
def step_impl(context):
    context.browser.get('https://demoqa.com/books')

@when(u'I click Sign in')
def step_impl(context):
    context.browser.find_element(By.ID, 'login').click()

@when(u'I fill my credential')
def step_impl(context):
    context.browser.find_element(By.ID, 'userName').send_keys('AdiUnoAdiUno')
    context.browser.find_element(By.ID, 'password').send_keys('07021996@Adiuno')
    context.browser.find_element(By.ID, 'login').click()

@then(u'I should be logged in')
def step_impl(context):
    print(context.browser.find_element(By.ID, 'userName-value').text)

    # assert(context.browser.find_element(By.ID, 'userName-value').text) == 'AdiUnoAdiUno'
